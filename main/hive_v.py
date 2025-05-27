import configparser
import re
import json
import os
import mysql.connector
from django.http import JsonResponse
from hdfs import InsecureClient
from pyhive import hive
import csv
from util.configread import config_read
from util.CustomJSONEncoder import CustomJsonEncoder
from util.codes import normal_code, system_error_code
# 获取当前文件路径的根目录
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
m_username = "Administrator"
hadoop_client = InsecureClient('http://localhost:9870')
dbtype, host, port, user, passwd, dbName, charset,hasHadoop = config_read(os.path.join(parent_directory,"config.ini"))

#将mysql里的相关表转成hive库里的表
def migrate_to_hive():

    mysql_conn = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=passwd,
        database=dbName
    )
    cursor = mysql_conn.cursor()

    hive_conn = hive.Connection(
        host='localhost',
        port=10000,
        username=m_username,
    )
    hive_cursor = hive_conn.cursor()
    #创建Hive数据库（如果不存在）
    hive_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbName}")
    hive_cursor.execute(f"USE {dbName}")

    monthlysalesofmanufacturers_table_path=f'/user/hive/warehouse/{dbName}.db/monthlysalesofmanufacturers'
    #删除已有的hive表
    if hadoop_client.status(monthlysalesofmanufacturers_table_path,strict=False):
        hadoop_client.delete(monthlysalesofmanufacturers_table_path, recursive=True)
    # 在Hive中删除表
    monthlysalesofmanufacturers_drop_table_query = f"""DROP TABLE monthlysalesofmanufacturers"""
    hive_cursor.execute(monthlysalesofmanufacturers_drop_table_query)
    cursor.execute("SELECT * FROM monthlysalesofmanufacturers")
    monthlysalesofmanufacturers_column_info = cursor.fetchall()
    #将数据写入 CSV 文件
    with open(os.path.join(parent_directory, "monthlysalesofmanufacturers.csv"), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入数据行
        for row in monthlysalesofmanufacturers_column_info:
            writer.writerow(row)
    cursor.execute("DESCRIBE monthlysalesofmanufacturers")
    monthlysalesofmanufacturers_column_info = cursor.fetchall()
    create_table_query = "CREATE TABLE IF NOT EXISTS monthlysalesofmanufacturers ("
    for column, data_type, _, _, _, _ in monthlysalesofmanufacturers_column_info:
        match = re.match(r'(\w+)(\(\d+\))?', data_type)
        mysql_type = match.group(1)
        hive_data_type = get_hive_type(mysql_type)
        create_table_query += f"{column} {hive_data_type}, "
    monthlysalesofmanufacturers_create_table_query = create_table_query[:-2] + ") row format delimited fields terminated by ','"
    hive_cursor.execute(monthlysalesofmanufacturers_create_table_query)
    # 上传映射文件
    monthlysalesofmanufacturers_hdfs_csv_path = f'/user/hive/warehouse/{dbName}.db/monthlysalesofmanufacturers'
    hadoop_client.upload(monthlysalesofmanufacturers_hdfs_csv_path, os.path.join(parent_directory, "monthlysalesofmanufacturers.csv"))
    monthlysalesofcarmodels_table_path=f'/user/hive/warehouse/{dbName}.db/monthlysalesofcarmodels'
    #删除已有的hive表
    if hadoop_client.status(monthlysalesofcarmodels_table_path,strict=False):
        hadoop_client.delete(monthlysalesofcarmodels_table_path, recursive=True)
    # 在Hive中删除表
    monthlysalesofcarmodels_drop_table_query = f"""DROP TABLE monthlysalesofcarmodels"""
    hive_cursor.execute(monthlysalesofcarmodels_drop_table_query)
    cursor.execute("SELECT * FROM monthlysalesofcarmodels")
    monthlysalesofcarmodels_column_info = cursor.fetchall()
    #将数据写入 CSV 文件
    with open(os.path.join(parent_directory, "monthlysalesofcarmodels.csv"), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入数据行
        for row in monthlysalesofcarmodels_column_info:
            writer.writerow(row)
    cursor.execute("DESCRIBE monthlysalesofcarmodels")
    monthlysalesofcarmodels_column_info = cursor.fetchall()
    create_table_query = "CREATE TABLE IF NOT EXISTS monthlysalesofcarmodels ("
    for column, data_type, _, _, _, _ in monthlysalesofcarmodels_column_info:
        match = re.match(r'(\w+)(\(\d+\))?', data_type)
        mysql_type = match.group(1)
        hive_data_type = get_hive_type(mysql_type)
        create_table_query += f"{column} {hive_data_type}, "
    monthlysalesofcarmodels_create_table_query = create_table_query[:-2] + ") row format delimited fields terminated by ','"
    hive_cursor.execute(monthlysalesofcarmodels_create_table_query)
    # 上传映射文件
    monthlysalesofcarmodels_hdfs_csv_path = f'/user/hive/warehouse/{dbName}.db/monthlysalesofcarmodels'
    hadoop_client.upload(monthlysalesofcarmodels_hdfs_csv_path, os.path.join(parent_directory, "monthlysalesofcarmodels.csv"))
    cursor.close()
    mysql_conn.close()
    hive_cursor.close()
    hive_conn.close()

#转换成hive的类型
def get_hive_type(mysql_type):
    type_mapping = {
        'INT': 'INT',
        'BIGINT': 'BIGINT',
        'FLOAT': 'FLOAT',
        'DOUBLE': 'DOUBLE',
        'DECIMAL': 'DECIMAL',
        'VARCHAR': 'STRING',
        'TEXT': 'STRING',
    }
    if isinstance(mysql_type, str):
        mysql_type = mysql_type.upper()
    return type_mapping.get(str(mysql_type), 'STRING')

#执行hive查询
def hive_query():
    # 连接到Hive服务器
    conn = hive.Connection(host='localhost', port=10000, username=m_username,database=dbName)
    # 创建一个游标对象
    cursor = conn.cursor()
    try:

        #定义Hive查询语句
        model_query = "SELECT COUNT(*) AS total, model FROM monthlysalesofcarmodels GROUP BY model"
        # 执行Hive查询语句
        cursor.execute(model_query)
        # 获取查询结果
        model_results = cursor.fetchall()
        model_json_list=[]
        for row in model_results:
            model_json_list.append({"model":row[1],"total":row[0]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "monthlysalesofcarmodels_groupmodel.json"), 'w', encoding='utf-8') as f:
            json.dump(model_json_list, f, ensure_ascii=False, indent=4)


        #定义Hive查询语句
        shareofsales_query = "SELECT COUNT(*) AS total, shareofsales FROM monthlysalesofcarmodels GROUP BY shareofsales"
        # 执行Hive查询语句
        cursor.execute(shareofsales_query)
        # 获取查询结果
        shareofsales_results = cursor.fetchall()
        shareofsales_json_list=[]
        for row in shareofsales_results:
            shareofsales_json_list.append({"shareofsales":row[1],"total":row[0]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "monthlysalesofcarmodels_groupshareofsales.json"), 'w', encoding='utf-8') as f:
            json.dump(shareofsales_json_list, f, ensure_ascii=False, indent=4)

        where = ' WHERE 1 = 1 '
        year_query = f'''SELECT `year`, ROUND(SUM(`manufacturer`), 2) AS `total`
            FROM monthlysalesofmanufacturers {where} GROUP BY `year`'''
        #执行Hive查询语句
        cursor.execute(year_query)
        # 获取查询结果
        year_results = cursor.fetchall()
        year_json_list=[]
        for row in year_results:
            year_json_list.append({"year":row[0],"total":row[1]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "monthlysalesofmanufacturers_valueyearmanufacturer.json"), 'w', encoding='utf-8') as f:
            json.dump(year_json_list, f, ensure_ascii=False, indent=4)
        where = ' WHERE 1 = 1 '
        month_query = f'''SELECT `month`, ROUND(SUM(`manufacturer`), 2) AS `total`
            FROM monthlysalesofmanufacturers {where} GROUP BY `month`'''
        #执行Hive查询语句
        cursor.execute(month_query)
        # 获取查询结果
        month_results = cursor.fetchall()
        month_json_list=[]
        for row in month_results:
            month_json_list.append({"month":row[0],"total":row[1]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "monthlysalesofmanufacturers_valuemonthmanufacturer.json"), 'w', encoding='utf-8') as f:
            json.dump(month_json_list, f, ensure_ascii=False, indent=4)
        where = ' WHERE 1 = 1 '
        shareofsales_query = f'''SELECT `shareofsales`, ROUND(SUM(`manufacturer`), 2) AS `total`
            FROM monthlysalesofmanufacturers {where} GROUP BY `shareofsales`'''
        #执行Hive查询语句
        cursor.execute(shareofsales_query)
        # 获取查询结果
        shareofsales_results = cursor.fetchall()
        shareofsales_json_list=[]
        for row in shareofsales_results:
            shareofsales_json_list.append({"shareofsales":row[0],"total":row[1]})
        #将JSON数据写入文件
        with open(os.path.join(parent_directory, "monthlysalesofmanufacturers_valueshareofsalesmanufacturer.json"), 'w', encoding='utf-8') as f:
            json.dump(shareofsales_json_list, f, ensure_ascii=False, indent=4)
        pass
    except Exception as e:
         print(f"An error occurred: {e}")
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()

    # hive分析
def hive_analyze(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        try:
            migrate_to_hive()
            hive_query()
            return JsonResponse(msg, encoder=CustomJsonEncoder)
        except Exception as e:
            msg['code'] = system_error_code
            msg['msg'] = f"发生错误：{e}"
            return JsonResponse(msg, encoder=CustomJsonEncoder)



