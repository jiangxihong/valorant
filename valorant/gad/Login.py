import sys
from random import randint
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QWidget,QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal,Qt 
from PyQt5.QtGui import QIcon,QFont
import func
import Signup
import FirstPage


class Login(QGroupBox):
    
    def __init__(self):
        super().__init__()
        # 接受信息，信息哪里来 
        
        self.initUI()
    def inputclick(self,input):
        for i in range(3):
            item=self.bodyLayout.itemAt(i+1).widget()
            if item.text()=='':
                item.setText(item.initText)
        if input.text()==input.initText:
            input.setText('')
        
    def signup(self):
        self.signup=Signup.Signup()
        self.signup.show()
        self.close()

        
    def submitFunction(self):

        data=[
            str(self.Game_id.text()),
            '',
            str(self.GameName.text()),
            str(self.GamePwd.text())]
        if func.Check_data(data):
            
            
            self.close()
            print("登陆成功")
            dic={}
            dic['Id_card']=str(self.Game_id.text())
            dic['game_name']=str(self.GameName.text())
            dic['game_pwd']=str(self.GamePwd.text())

            Firstpage=FirstPage.MyWidget(dic)
            Firstpage.show()
        else:
            QMessageBox.information(self, '提示', '信息错误，请重新输入', QMessageBox.Ok)
        
        

    def initUI(self):
        self.Title=QLabel()
        self.Title.setText("登陆")
        self.Title.setAlignment(Qt.AlignCenter)  # 设置标签文本居中
        self.Title.setFont(QFont("Arial", 20))  # 设置标签字体大小为20

        # 姓名输入框 
        self.Game_id=QLineEdit()
        self.Game_id.setFixedSize(400,40)
        self.Game_id.initText='请输入游戏Id'
        self.Game_id.setText(self.Game_id.initText)
        self.Game_id.setTextMargins(5,5,5,5)
        self.Game_id.mousePressEvent=lambda x:self.inputclick(self.Game_id)

        # 游戏内名称
        self.GameName=QLineEdit()
        self.GameName.setFixedSize(400,40)
        
        self.GameName.initText='请输入游戏昵称'
        self.GameName.setText(self.GameName.initText)
        self.GameName.setTextMargins(5,5,5,5)
        self.GameName.mousePressEvent=lambda x:self.inputclick(self.GameName)
        # 游戏密码
        self.GamePwd=QLineEdit()
        self.GamePwd.setFixedSize(400,40)
        
        self.GamePwd.initText='请输入游戏密码'
        self.GamePwd.setText(self.GamePwd.initText)
        self.GamePwd.setTextMargins(5,5,5,5)
        self.GamePwd.mousePressEvent=lambda x:self.inputclick(self.GamePwd)
        
    # 提交
        self.submit = QToolButton()
        self.submit.setText('登陆')
        self.submit.setFixedSize(400, 40)
        self.submit.clicked.connect(self.submitFunction)

    # 注册
        self.back = QToolButton()
        self.back.setText('注册')
        self.back.setFixedSize(400, 40)
        self.back.clicked.connect(self.signup)

        self.bodyLayout = QVBoxLayout()
        self.bodyLayout.addWidget(self.Title)
        
        self.btnList = [self.Game_id,
                        self.GameName,self.GamePwd]
        for i in self.btnList:
            self.bodyLayout.addWidget(i)
        self.bodyLayout.addWidget(self.submit)
        self.bodyLayout.addWidget(self.back)

        self.setLayout(self.bodyLayout)
    def setMyStyle(self):
        self.setStyleSheet('''
        QWidget{
            background-color: white;
        }
        QLineEdit{
            border:0px;
            border-bottom: 1px solid rgba(229, 229, 229, 1);
            color: grey;
        }
        QToolButton{
            border: 0px;
            background-color:rgba(52, 118, 176, 1);
            color: white;
            font-size: 25px;
            font-family: 微软雅黑;
        }
        QGroupBox{
            border: 1px solid rgba(229, 229, 229, 1);
            border-radius: 5px;
        }
        ''')
        self.title.setStyleSheet('''
        *{
            color: rgba(113, 118, 121, 1);
            font-size: 30px;
            font-family: 微软雅黑;
        }
        ''')
        self.subTitle.setStyleSheet('''
        *{
            color: rgba(184, 184, 184, 1);
        }
        ''')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())