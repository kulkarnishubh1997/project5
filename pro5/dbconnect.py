import pymysql
dbconn=pymysql.connect(user="root",password="root",host="localhost",port=3306,db="pro5")
cus=dbconn.cursor()