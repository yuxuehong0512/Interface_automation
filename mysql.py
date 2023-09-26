# @Time:2023/9/26 11:20
# @Author:yuxh
# @File:mysql.py

import pymysql

#打开数据库连接

db = pymysql.connect(host= "shop-xo.hctestedu.com",
                     port= 3306, # 注意：端口必须是int类型
                     user= "api_test",
                     password= "Aa9999!",
                     database= "shopxo_hctested")
#使用cursor()方法创建一个游标对象
cursor = db.cursor()

#使用execute()方法执行SQL查询
cursor.execute("SELECT VERSION()")

#使用fetchone()方法获取单条数据
data= cursor.fetchone()

print("Database version: %s" % data)

#关闭数据库

db.close()