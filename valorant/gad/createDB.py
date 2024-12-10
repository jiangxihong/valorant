import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'jxH051114.',
    'database': 'valorant',
    'port': 3306,
    'charset': 'utf8'
}

class createDB:
    def __init__(self):
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor()
        print("创建数据库")
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS valorant")
        self.conn.select_db('valorant')
        self.cursor.execute('''create table if not exists 
                            user_info(
                            
                            game_id varchar(20) primary key ,
                            name varchar(20),
                            game_name varchar(20),
                            game_pwd varchar(20));
                            ''')
        self.cursor.execute('''create table if not exists  transcation(
                            owner_name varchar(20),
                            price varchar(10),
                            gun_name varchar(20),
                            gun_derma varchar(20),
                            buyer_name varchar(20),
                            time varchar(20),
                            pay_or_not varchar(10)
                            
                            
                            
                            
                            )''')
        print("创建表")
        self.conn.commit()
        print("数据库和表创建完成")

    def close_db(self):
        if self.conn:
            self.conn.close()
def drop_db():
    try:
        conn = pymysql.connect(host=config['host'], user=config['user'], password=config['password'], port=config['port'], charset=config['charset'])
        print("成功连接到数据库")
        cursor = conn.cursor()
        conn.autocommit(True)
        cursor.execute("DROP DATABASE `{}`".format(config['database']))
        conn.autocommit(False)
    except Exception as e:
        print('数据库删除失败，报错信息如下：')
        print(e)
def drop_table():
    try:
        conn = pymysql.connect(host=config['host'], user=config['user'], password=config['password'], port=config['port'], charset=config['charset'])
        print("成功连接到数据库")
        cursor = conn.cursor()
        conn.select_db(config['database'])
        conn.autocommit(True)
        cursor.execute("DROP TABLE `{}`".format('transcation'))
        conn.autocommit(False)
    except Exception as e:
        print('表删除失败，报错信息如下：')
        print(e)


if __name__=='__main__':
    createDB()
    
    

