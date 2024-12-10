import pymysql 
import sys
from typing import Optional
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton,
    QLineEdit, QStackedWidget
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from person import *

config={
    'host':'127.0.0.1',
    'user':'root',
    'password':'jxH051114.',
    'database':'valorant',
    'port':3306,
    'charset':'utf8'
}

# 连接数据库 func 
def connect_db():
    try:
        conn=pymysql.connect(host=config['host'],user=config['user'],database=config['database'],password=config['password'],port=config['port'],charset=config['charset'])
        print("成功连接到数据库")
        cursor=conn.cursor()
        conn.autocommit(True)
        return conn,cursor
    except Exception as e:
        print('数据库连接失败，报错信息如下：')
        print(e)

# second 插入数据 
def insert_data(data:list):
    conn,cursor=connect_db()
    cursor.execute("insert into user_info values(%s,%s,%s,%s)",data)
    conn.commit()
    print("插入成功")
# 关闭数据库
def close_db(conn):
   
    if conn:
        conn.close()
        print("关闭数据库")


def Check_data(data):
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM user_info WHERE game_id=%s", (str(data[0])))  # 注意参数是一个元组
    result = cursor.fetchall()
    close_db(conn)
    if result:
        
        for i in range(len(data)):
            print(result[0][i])
            
            if str(data[i])!=str(result[0][i]) and i!=1:
                return False
        return True 
        
    else:
        QMessageBox.information(None, '提示', '信息错误，请重新输入', QMessageBox.Ok)
def check_data_gun_name(name):
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM user_info WHERE game_name=%s", (name))  
        
    return True 
def show_person_info(msg):
    ex=PersonInfo(msg)
    ex.show()
if __name__=="__main__":
    
    
    result=Check_data(['0521372','1','1','1'])
    print(result)
    if 1=='1':
        print("yes")
   

    
        