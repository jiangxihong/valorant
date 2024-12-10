# person_infomation 
import sys
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
# import func
# import database

class PersonInfo(QGroupBox):
    def __init__(self,Per_info:dict):
        super().__init__()
        # 接受信息，信息哪里来 
        self.Per_info=Per_info 

        self.title=QLabel()
        self.title.setText("个人信息")

        self.subTitle=QLabel()
        self.subTitle.setText("编辑个人信息")

        #身份证号输入框  防止小学生进行游戏  所以设置为不可编辑
        self.Id_Input=QLineEdit()
        self.Id_Input.setFixedSize(400,40)
        self.Id_Input.setText(self.Per_info['Id_card'])
        self.Id_Input.initText='请输入身份证号'
        self.Id_Input.setEnabled(False)

        # 姓名输入框 
        self.Name_Input=QLineEdit()
        self.Name_Input.setFixedSize(400,40)
        self.Name_Input.setText(self.Per_info['name'])
        self.Name_Input.initText='请输入姓名'
        self.Name_Input.setTextMargins(5,5,5,5)
        self.Name_Input.mousePressEvent=lambda x:self.inputclick(self.Name_Input)

        # 游戏内名称
        self.GameName_Input=QLineEdit()
        self.GameName_Input.setFixedSize(400,40)
        self.GameName_Input.setText(self.Per_info['game_name'])
        self.GameName_Input.initText='请输入游戏名称'
        self.GameName_Input.setTextMargins(5,5,5,5)
        self.GameName_Input.mousePressEvent=lambda x:self.inputclick(self.GameName_Input)
        # 游戏密码
        self.GamePwd_Input=QLineEdit()
        self.GamePwd_Input.setFixedSize(400,40)
        self.GamePwd_Input.setText(self.Per_info['game_pwd'])
        self.GamePwd_Input.initText='请输入游戏密码'
        self.GamePwd_Input.setTextMargins(5,5,5,5)
        self.GamePwd_Input.mousePressEvent=lambda x:self.inputclick(self.GamePwd_Input)
        #再次输入密码
        self.GamePwd_Input2=QLineEdit()
        self.GamePwd_Input2.setFixedSize(400,40)
        self.GamePwd_Input2.setText(self.Per_info['game_pwd'])
        self.GamePwd_Input2.initText='请再次输入密码'
        self.GamePwd_Input2.setTextMargins(5,5,5,5)
        self.GamePwd_Input2.mousePressEvent=lambda x:self.inputclick(self.GamePwd_Input2)

    # 提交
        self.submit = QToolButton()
        self.submit.setText('提交')
        self.submit.setFixedSize(400, 40)
        self.submit.clicked.connect(self.submitFunction)

    # 退出
        self.back = QToolButton()
        self.back.setText('退出')
        self.back.setFixedSize(400, 40)
        self.back.clicked.connect(self.close)

        self.bodyLayout = QVBoxLayout()
        self.bodyLayout.addWidget(self.title)
        self.bodyLayout.addWidget(self.subTitle)
        self.btnList = [self.Id_Input,self.Name_Input,
                        self.GameName_Input,self.GamePwd_Input,
                        self.GamePwd_Input2]
        for i in self.btnList:
            self.bodyLayout.addWidget(i)
        self.bodyLayout.addWidget(self.submit)
        self.bodyLayout.addWidget(self.back)

        self.setLayout(self.bodyLayout)
        self.initUI()
    def inputclick(self,input):
        
        if input.text()==input.initText:
            input.setText('')
        
    def submitFunction(self):
        pass 

    def initUI(self):
        pass
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
    stu_msg = temp = {
        'name': 'jiang',
        'Id_card': '123456789123456789',
        'game_name': '花落人断肠',
        'game_pwd': 'jxH051114.'
    }
    app = QApplication(sys.argv)
    ex = PersonInfo(stu_msg)
    ex.show()
    sys.exit(app.exec_())