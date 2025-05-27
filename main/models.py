#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class monthlysalesofmanufacturers(BaseModel):
    __doc__ = u'''monthlysalesofmanufacturers'''
    __tablename__ = 'monthlysalesofmanufacturers'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    year=models.CharField ( max_length=255, null=True, unique=False, verbose_name='年份' )
    month=models.CharField ( max_length=255, null=True, unique=False, verbose_name='月份' )
    ranking=models.IntegerField  (  null=True, unique=False, verbose_name='排行' )
    shareofsales=models.CharField ( max_length=255, null=True, unique=False, verbose_name='厂商' )
    manufacturer=models.IntegerField  (  null=True, unique=False, verbose_name='销量(辆)' )
    shareofsalesvolume=models.CharField ( max_length=255, null=True, unique=False, verbose_name='占销量份额' )
    '''
    year=VARCHAR
    month=VARCHAR
    ranking=Integer
    shareofsales=VARCHAR
    manufacturer=Integer
    shareofsalesvolume=VARCHAR
    '''
    class Meta:
        db_table = 'monthlysalesofmanufacturers'
        verbose_name = verbose_name_plural = '厂商每月销售'
class monthlysalesofcarmodels(BaseModel):
    __doc__ = u'''monthlysalesofcarmodels'''
    __tablename__ = 'monthlysalesofcarmodels'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    year=models.CharField ( max_length=255, null=True, unique=False, verbose_name='年份' )
    month=models.CharField ( max_length=255, null=True, unique=False, verbose_name='月份' )
    ranking=models.CharField ( max_length=255, null=True, unique=False, verbose_name='排名' )
    model=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车型' )
    shareofsales=models.CharField ( max_length=255, null=True, unique=False, verbose_name='厂商' )
    manufacturer=models.IntegerField  (  null=True, unique=False, verbose_name='销量(辆)' )
    sales=models.IntegerField  (  null=True, unique=False, verbose_name='售价(万元)' )
    '''
    year=VARCHAR
    month=VARCHAR
    ranking=VARCHAR
    model=VARCHAR
    shareofsales=VARCHAR
    manufacturer=Integer
    sales=Integer
    '''
    class Meta:
        db_table = 'monthlysalesofcarmodels'
        verbose_name = verbose_name_plural = '车型每月销量'
class overallsalesofcars(BaseModel):
    __doc__ = u'''overallsalesofcars'''
    __tablename__ = 'overallsalesofcars'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    time=models.CharField ( max_length=255, null=True, unique=False, verbose_name='时间' )
    manufacturer=models.IntegerField  (  null=True, unique=False, verbose_name='销量(辆)' )
    yearonyear=models.CharField ( max_length=255,null=False, unique=False, verbose_name='同比' )
    '''
    time=VARCHAR
    manufacturer=Integer
    yearonyear=VARCHAR
    '''
    class Meta:
        db_table = 'overallsalesofcars'
        verbose_name = verbose_name_plural = '汽车总体销量'
class monthlysalesofcarmodelsforecast(BaseModel):
    __doc__ = u'''monthlysalesofcarmodelsforecast'''
    __tablename__ = 'monthlysalesofcarmodelsforecast'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    month=models.CharField ( max_length=255, null=True, unique=False, verbose_name='月份' )
    model=models.CharField ( max_length=255, null=True, unique=False, verbose_name='车型' )
    shareofsales=models.CharField ( max_length=255, null=True, unique=False, verbose_name='厂商' )
    sales=models.IntegerField  (  null=True, unique=False, verbose_name='售价(万元)' )
    manufacturer=models.IntegerField  (  null=True, unique=False, verbose_name='需求量(辆)' )
    '''
    month=VARCHAR
    model=VARCHAR
    shareofsales=VARCHAR
    sales=Integer
    manufacturer=Integer
    '''
    class Meta:
        db_table = 'monthlysalesofcarmodelsforecast'
        verbose_name = verbose_name_plural = '销量预测'
