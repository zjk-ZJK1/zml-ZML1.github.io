#coding:utf-8
import base64, copy, logging, os, sys, time, xlrd, json, datetime, configparser
from django.http import JsonResponse
from django.apps import apps
import numbers
from django.db.models.aggregates import Count,Sum
from django.db.models import Case, When, IntegerField, F
from django.forms import model_to_dict
import requests
from util.CustomJSONEncoder import CustomJsonEncoder
from .models import monthlysalesofcarmodelsforecast
from util.codes import *
from util.auth import Auth
from util.common import Common
import util.message as mes
from django.db import connection
import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Q
from util.baidubce_api import BaiDuBce
from .config_model import config
import pandas as pd

import joblib
import pymysql
import numpy as np
import matplotlib
matplotlib.use('Agg')  # 在导入pyplot之前设置
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
from util.configread import config_read
import os
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,accuracy_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import classification_report, confusion_matrix,confusion_matrix, mean_squared_error, mean_absolute_error, r2_score
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import seaborn as sns
pd.options.mode.chained_assignment = None  # default='warn'

#获取当前文件路径的根目录
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dbtype, host, port, user, passwd, dbName, charset,hasHadoop = config_read(os.path.join(parent_directory,"config.ini"))
#MySQL连接配置
mysql_config = {
    'host': host,
    'user':user,
    'password': passwd,
    'database': dbName,
    'port':port
}

#获取预测可视化图表接口
def monthlysalesofcarmodelsforecast_forecastimgs(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, 'message': 'success'}
        # 指定目录
        directory = os.path.join(parent_directory, "templates", "front", "monthlysalesofcarmodelsforecast")
        # 获取目录下的所有文件和文件夹名称
        all_items = os.listdir(directory)
        # 过滤出文件（排除文件夹）
        files = [f'upload/monthlysalesofcarmodelsforecast/{item}' for item in all_items if os.path.isfile(os.path.join(directory, item))]
        msg["data"] = files
        fontlist=[]
        for font in fm.fontManager.ttflist:
            fontlist.append(font.name)
        msg["message"]=fontlist
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_forecast(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        #1.获取数据集
        req_dict = request.session.get("req_dict")
        connection = pymysql.connect(**mysql_config)
        query = "SELECT month,model,shareofsales,sales, manufacturer FROM monthlysalesofcarmodels"
        #2.处理缺失值
        data = pd.read_sql(query, connection).dropna()
        id = req_dict.pop('id',None)
        df = to_forecast(data,req_dict,None)
        #9.创建数据库连接,将DataFrame 插入数据库
        connection_string = f"mysql+pymysql://{mysql_config['user']}:{mysql_config['password']}@{mysql_config['host']}:{mysql_config['port']}/{mysql_config['database']}"
        engine = create_engine(connection_string)
        try:
            if req_dict :
                #遍历 DataFrame，并逐行更新数据库
                with engine.connect() as connection:
                    for index, row in df.iterrows():
                        sql = """
                        INSERT INTO monthlysalesofcarmodelsforecast (id
                        ,manufacturer
                        )
                        VALUES (%(id)s
                    ,%(manufacturer)s
                        )
                        ON DUPLICATE KEY UPDATE
                        manufacturer = VALUES(manufacturer)
                        """
                        connection.execute(sql, {'id': id
                            , 'manufacturer': row['manufacturer']
                        })
            else:
                df.to_sql('monthlysalesofcarmodelsforecast', con=engine, if_exists='append', index=False)
            print("数据更新成功！")
        except Exception as e:
            print(f"发生错误: {e}")
        finally:
            engine.dispose()  # 关闭数据库连接
        return JsonResponse(msg, encoder=CustomJsonEncoder)
def to_forecast(data,req_dict,value):
    if len(data) < 5:
        print(f"的样本数量不足: {len(data)}")
        return pd.DataFrame()
    #3.处理特征值和目标值
    labels={}
    for key in data.keys():
        if pd.api.types.is_string_dtype(data[key]):
            label_encoder = LabelEncoder()
            labels[key] = label_encoder
            data[key] = label_encoder.fit_transform(data[key])
    #4.数据集划分
    X = data[[
        'month',
        'model',
        'shareofsales',
        'sales',
    ]]
    y = data[[
        'manufacturer',
    ]]
    x_train, x_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=22)
    #5.构建预测特征值
    #根据输入的特征值去预测
    if req_dict:
        req_dict.pop('addtime',None)
        future_df = pd.DataFrame([req_dict])
        for key in future_df.keys():
           if key in labels:
               encoder = labels[key]
               values = future_df[key][0]
               try:
                   values = encoder.transform([values])[0]
               except ValueError as e: #处理未见过的标签
                   values = np.array([encoder.transform([v])[0] if v in encoder.classes_ else -1 for v in values]).sum()
               future_df[key][0] = values
    else:
        future_df = x_test
    #特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    future_df = transfer.transform(future_df)
    estimator_file = os.path.join(parent_directory, "monthlysalesofcarmodelsforecast.pkl")
    #6.训练调用模型-线性回归(正规方程)
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)
    #生成散点图
    y_predict = estimator.predict(x_test)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体 SimHei
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_predict, color='blue', edgecolor='k', alpha=0.7)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
    plt.xlabel('真实值')
    plt.ylabel('预测值')
    plt.title('真实值vs预测值')
    if value!=None:
        directory =os.path.join(parent_directory, "templates","front","monthlysalesofcarmodelsforecast","{value}_distribution.png")
        os.makedirs(os.path.dirname(directory), exist_ok=True)
        plt.savefig(directory, format='png', dpi=300)
    else:
        directory =os.path.join(parent_directory,"templates","front","monthlysalesofcarmodelsforecast","residual_distribution.png")
        os.makedirs(os.path.dirname(directory), exist_ok=True)
        plt.savefig(directory, format='png', dpi=300)
    plt.clf()
    #保存模型
    joblib.dump(estimator, estimator_file)
    y_pred  = estimator.predict(x_test)

    comparison_df = pd.DataFrame({'实际值': y_test.values.flatten(), '预测值': y_pred.flatten()})
    comparison_df = comparison_df.sort_values(by='实际值')  # 按实际销量排序，方便可视化

    # 绘制实际值 vs 预测值散点图
    plt.figure(figsize=(10, 6))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体 SimHei
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题
    sns.scatterplot(x=comparison_df['实际值'], y=comparison_df['预测值'], color='blue', label='预测值')
    plt.plot([comparison_df['实际值'].min(), comparison_df['实际值'].max()],
             [comparison_df['实际值'].min(), comparison_df['实际值'].max()],
             color='red', linestyle='--', label='完美预测线')
    plt.xlabel('实际值')
    plt.ylabel('预测值')
    plt.title('实际值 vs 预测值')
    plt.legend()
    directory =os.path.join(parent_directory, "templates","front","monthlysalesofcarmodelsforecast","figure.png")
    os.makedirs(os.path.dirname(directory), exist_ok=True)
    plt.savefig(directory)
    plt.clf()
    plt.close()
    #7.进行预测
    y_predict = estimator.predict(future_df)
    if isinstance(y_predict[0], numbers.Number) or len(y_predict[0])<2:
        y_predict = np.mean(y_predict, axis=0)
        if not isinstance(y_predict, np.ndarray):
            y_predict = np.expand_dims(y_predict, axis=0)
    df = pd.DataFrame(y_predict, columns=[
        'manufacturer',
    ])
    df['manufacturer']=df['manufacturer'].astype(int)
    return df

def monthlysalesofcarmodelsforecast_register(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")


        error = monthlysalesofcarmodelsforecast.createbyreq(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, req_dict)
        if error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = "用户已存在,请勿重复注册!"
        else:
            msg['data'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_login(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")
        datas = monthlysalesofcarmodelsforecast.getbyparams(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, req_dict)
        if not datas:
            msg['code'] = password_error_code
            msg['msg'] = mes.password_error_code
            return JsonResponse(msg, encoder=CustomJsonEncoder)

        try:
            __sfsh__= monthlysalesofcarmodelsforecast.__sfsh__
        except:
            __sfsh__=None

        if  __sfsh__=='是':
            if datas[0].get('sfsh')!='是':
                msg['code']=other_code
                msg['msg'] = "账号已锁定，请联系管理员审核!"
                return JsonResponse(msg, encoder=CustomJsonEncoder)
                
        req_dict['id'] = datas[0].get('id')


        return Auth.authenticate(Auth, monthlysalesofcarmodelsforecast, req_dict)


def monthlysalesofcarmodelsforecast_logout(request):
    if request.method in ["POST", "GET"]:
        msg = {
            "msg": "登出成功",
            "code": 0
        }

        return JsonResponse(msg, encoder=CustomJsonEncoder)


def monthlysalesofcarmodelsforecast_resetPass(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}

        req_dict = request.session.get("req_dict")

        columns=  monthlysalesofcarmodelsforecast.getallcolumn( monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast)

        try:
            __loginUserColumn__= monthlysalesofcarmodelsforecast.__loginUserColumn__
        except:
            __loginUserColumn__=None
        username=req_dict.get(list(req_dict.keys())[0])
        if __loginUserColumn__:
            username_str=__loginUserColumn__
        else:
            username_str=username
        if 'mima' in columns:
            password_str='mima'
        else:
            password_str='password'

        init_pwd = '123456'
        recordsParam = {}
        recordsParam[username_str] = req_dict.get("username")
        records=monthlysalesofcarmodelsforecast.getbyparams(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, recordsParam)
        if len(records)<1:
            msg['code'] = 400
            msg['msg'] = '用户不存在'
            return JsonResponse(msg, encoder=CustomJsonEncoder)

        eval('''monthlysalesofcarmodelsforecast.objects.filter({}='{}').update({}='{}')'''.format(username_str,username,password_str,init_pwd))
        
        return JsonResponse(msg, encoder=CustomJsonEncoder)



def monthlysalesofcarmodelsforecast_session(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}

        req_dict={"id":request.session.get('params').get("id")}
        msg['data']  = monthlysalesofcarmodelsforecast.getbyparams(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, req_dict)[0]

        return JsonResponse(msg, encoder=CustomJsonEncoder)


def monthlysalesofcarmodelsforecast_default(request):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        req_dict.update({"isdefault":"是"})
        data=monthlysalesofcarmodelsforecast.getbyparams(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, req_dict)
        if len(data)>0:
            msg['data']  = data[0]
        else:
            msg['data']  = {}
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_page(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        global monthlysalesofcarmodelsforecast

        #获取全部列名
        columns=  monthlysalesofcarmodelsforecast.getallcolumn( monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast)

        if "vipread" in req_dict and "vipread" not in columns:
          del req_dict["vipread"]

        #当前登录用户所在表
        tablename = request.session.get("tablename")

        '''__authSeparate__此属性为真，params添加userid，后台只查询个人数据'''
        try:
            __authSeparate__=monthlysalesofcarmodelsforecast.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns and 'userid' not in req_dict:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        #当项目属性hasMessage为”是”，生成系统自动生成留言板的表messages，同时该表的表属性hasMessage也被设置为”是”,字段包括userid（用户id），username(用户名)，content（留言内容），reply（回复）
        #接口page需要区分权限，普通用户查看自己的留言和回复记录，管理员查看所有的留言和回复记录
        try:
            __hasMessage__=monthlysalesofcarmodelsforecast.__hasMessage__
        except:
            __hasMessage__=None
        if  __hasMessage__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict["userid"]=request.session.get("params").get("id")

        # 判断当前表的表属性isAdmin,为真则是管理员表
        # 当表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
        __isAdmin__ = None

        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        # 当前表也是有管理员权限的表
        if  __isAdmin__ == "是" and 'monthlysalesofcarmodelsforecast' != 'forum' :
            if req_dict.get("userid") and 'monthlysalesofcarmodelsforecast' != 'chat' and 'monthlysalesofcarmodelsforecast' != 'examrecord':
                del req_dict["userid"]
        else:
            if tablename!="users" and tablename!="jdfnl" and 'monthlysalesofcarmodelsforecast'[:7]!='discuss' and "userid" in monthlysalesofcarmodelsforecast.getallcolumn(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast):
                req_dict["userid"] = request.session.get("params").get("id")

        #当列属性authTable有值(某个用户表)[该列的列名必须和该用户表的登陆字段名一致]，则对应的表有个隐藏属性authTable为”是”，那么该用户查看该表信息时，只能查看自己的
        try:
            __authTables__=monthlysalesofcarmodelsforecast.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __isAdmin__ == "是":
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break
        q = Q()

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  =monthlysalesofcarmodelsforecast.page(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, req_dict, request, q)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_autoSort(request):
    '''
    ．智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
主要信息列表（如商品列表，新闻列表）中使用，显示最近点击的或最新添加的5条记录就行
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if "clicknum"  in monthlysalesofcarmodelsforecast.getallcolumn(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast):
            req_dict['sort']='clicknum'
        elif "browseduration"  in monthlysalesofcarmodelsforecast.getallcolumn(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast):
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        req_dict['order']='desc'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = monthlysalesofcarmodelsforecast.page(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast, req_dict)

        return JsonResponse(msg, encoder=CustomJsonEncoder)

#分类列表
def monthlysalesofcarmodelsforecast_lists(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":[]}
        msg['data'],_,_,_,_  = monthlysalesofcarmodelsforecast.page(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, {})
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_query(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        try:
            query_result = monthlysalesofcarmodelsforecast.objects.filter(**request.session.get("req_dict")).values()
            msg['data'] = query_result[0]
        except Exception as e:

            msg['code'] = crud_error_code
            msg['msg'] = f"发生错误：{e}"
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_list(request):
    '''
    前台分页
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        #获取全部列名
        columns=  monthlysalesofcarmodelsforecast.getallcolumn( monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast)
        if "vipread" in req_dict and "vipread" not in columns:
          del req_dict["vipread"]
        #表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
        try:
            __foreEndList__=monthlysalesofcarmodelsforecast.__foreEndList__
        except:
            __foreEndList__=None
        try:
            __foreEndListAuth__=monthlysalesofcarmodelsforecast.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        #authSeparate
        try:
            __authSeparate__=monthlysalesofcarmodelsforecast.__authSeparate__
        except:
            __authSeparate__=None

        if __foreEndListAuth__ =="是" and __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and request.session.get("params") is not None:
                req_dict['userid']=request.session.get("params").get("id")

        tablename = request.session.get("tablename")
        if tablename == "users" and req_dict.get("userid") != None:#判断是否存在userid列名
            del req_dict["userid"]
        else:
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            if __isAdmin__ == "是":
                if req_dict.get("userid"):
                    # del req_dict["userid"]
                    pass
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if "userid" in columns:
                    try:
                        pass
                    except:
                        pass
        #当列属性authTable有值(某个用户表)[该列的列名必须和该用户表的登陆字段名一致]，则对应的表有个隐藏属性authTable为”是”，那么该用户查看该表信息时，只能查看自己的
        try:
            __authTables__=monthlysalesofcarmodelsforecast.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __foreEndListAuth__=="是":
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    try:
                        del req_dict['userid']
                    except:
                        pass
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break
        
        if monthlysalesofcarmodelsforecast.__tablename__[:7]=="discuss":
            try:
                del req_dict['userid']
            except:
                pass


        q = Q()
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = monthlysalesofcarmodelsforecast.page(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, req_dict, request, q)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_save(request):
    '''
    后台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys():
            del req_dict['clicktime']
        tablename=request.session.get("tablename")
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        #获取全部列名
        columns=  monthlysalesofcarmodelsforecast.getallcolumn( monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast)
        if tablename!='users' and req_dict.get("userid")!=None and 'userid' in columns  and __isAdmin__!='是':
            params=request.session.get("params")
            req_dict['userid']=params.get('id')


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']

        idOrErr= monthlysalesofcarmodelsforecast.createbyreq(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast, req_dict)
        if idOrErr is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = idOrErr
        else:
            msg['data'] = idOrErr

        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_add(request):
    '''
    前台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        tablename=request.session.get("tablename")

        #获取全部列名
        columns=  monthlysalesofcarmodelsforecast.getallcolumn( monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast)
        try:
            __authSeparate__=monthlysalesofcarmodelsforecast.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        try:
            __foreEndListAuth__=monthlysalesofcarmodelsforecast.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params").get("id")


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']
        error= monthlysalesofcarmodelsforecast.createbyreq(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast, req_dict)
        if error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_thumbsup(request,id_):
    '''
     点赞：表属性thumbsUp[是/否]，刷表新增thumbsupnum赞和crazilynum踩字段，
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=monthlysalesofcarmodelsforecast.getbyid(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = monthlysalesofcarmodelsforecast.updatebyparams(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)


def monthlysalesofcarmodelsforecast_info(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data = monthlysalesofcarmodelsforecast.getbyid(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= monthlysalesofcarmodelsforecast.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"  and  "clicknum"  in monthlysalesofcarmodelsforecast.getallcolumn(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}
            ret=monthlysalesofcarmodelsforecast.updatebyparams(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_detail(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data =monthlysalesofcarmodelsforecast.getbyid(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= monthlysalesofcarmodelsforecast.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"   and  "clicknum"  in monthlysalesofcarmodelsforecast.getallcolumn(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}

            ret=monthlysalesofcarmodelsforecast.updatebyparams(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def monthlysalesofcarmodelsforecast_update(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys() and req_dict['clicktime']=="None":
            del req_dict['clicktime']
        if req_dict.get("mima") and "mima" not in monthlysalesofcarmodelsforecast.getallcolumn(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast) :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in monthlysalesofcarmodelsforecast.getallcolumn(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast) :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = monthlysalesofcarmodelsforecast.updatebyparams(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def monthlysalesofcarmodelsforecast_delete(request):
    '''
    批量删除
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        error=monthlysalesofcarmodelsforecast.deletes(monthlysalesofcarmodelsforecast,
            monthlysalesofcarmodelsforecast,
             req_dict.get("ids")
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def monthlysalesofcarmodelsforecast_vote(request,id_):
    '''
    浏览点击次数（表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1）
统计商品或新闻的点击次数；提供新闻的投票功能
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}


        data= monthlysalesofcarmodelsforecast.getbyid(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=monthlysalesofcarmodelsforecast.updatebyparams(monthlysalesofcarmodelsforecast,monthlysalesofcarmodelsforecast,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return JsonResponse(msg)

def monthlysalesofcarmodelsforecast_importExcel(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}

        excel_file = request.FILES.get("file", "")
        file_type = excel_file.name.split('.')[1]
        
        if file_type in ['xlsx', 'xls']:
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            table = data.sheets()[0]
            rows = table.nrows
            
            try:
                for row in range(1, rows):
                    row_values = table.row_values(row)
                    req_dict = {}
                    monthlysalesofcarmodelsforecast.createbyreq(monthlysalesofcarmodelsforecast, monthlysalesofcarmodelsforecast, req_dict)
                    
            except:
                pass
                
        else:
            msg = {
                "msg": "文件类型错误",
                "code": 500
            }
                
        return JsonResponse(msg)

def monthlysalesofcarmodelsforecast_autoSort2(request):
    return JsonResponse({"code": 0, "msg": '',  "data":{}})













