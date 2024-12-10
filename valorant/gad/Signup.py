import sys
from random import randint
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QWidget,QLineEdit, QToolButton, QGroupBox, QMessageBox)
from PyQt5.QtCore import pyqtSignal,Qt 
from PyQt5.QtGui import QIcon,QFont
import func
import Login
import FirstPage
class Signup(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('注册')
        self.Title=QLabel()
        self.Title.setText('注册账号')
        self.Title.setAlignment(Qt.AlignCenter)  # 设置标签文本居中
        self.Title.setFont(QFont("Arial", 20))  # 设置标签字体大小为20
        self.Title.setFixedSize(400,40)

        self.button=QToolButton()
        self.button.setText('注册')
        self.button.setFixedSize(400,40)
        self.button.setStyleSheet("""
    QToolButton {
        text-align: center;
        background-color: #4CAF50; /* 绿色背景 */
        color: white; /* 白色文字 */
        border-radius: 10px; /* 圆角边框 */
    }
    QToolButton:hover {
        background-color: #45a049; /* 鼠标悬停时的背景颜色 */
    }
""")

        self.button.clicked.connect(self.submitFunction)
        self.setFixedSize(440,500)

#gmae_id 
        self.In_Gmae_id=QLineEdit()
        self.In_Gmae_id.setFixedSize(400,40)
        st=''
        for i in range(7):
            st+=str(randint(0,9))
        self.In_Gmae_id.initText=st
        self.In_Gmae_id.setTextMargins(5,5,5,5)
        self.In_Gmae_id.setText(self.In_Gmae_id.initText)
        self.In_Gmae_id.setEnabled(False)
    #

# 姓名框
        self.In_Name=QLineEdit()
        self.In_Name.setFixedSize(400,40)
        self.In_Name.initText='请输入真实姓名'
        self.In_Name.setTextMargins(5,5,5,5)
        self.In_Name.setText(self.In_Name.initText)
        self.In_Name.mousePressEvent=lambda x:self.input_click(self.In_Name)

# 游戏姓名框
        self.In_GameName=QLineEdit()
        self.In_GameName.setFixedSize(400,40)
        self.In_GameName.initText='请输入游戏昵称'
        self.In_GameName.setTextMargins(5,5,5,5)
        self.In_GameName.setText(self.In_GameName.initText)
        self.In_GameName.mousePressEvent=lambda x:self.input_click(self.In_GameName)
# 密码框 
        self.In_GamePwd=QLineEdit()
        self.In_GamePwd.setFixedSize(400,40)
        self.In_GamePwd.initText='请输入密码'
        self.In_GamePwd.setTextMargins(5,5,5,5)
        self.In_GamePwd.setText(self.In_GamePwd.initText)
        self.In_GamePwd.mousePressEvent=lambda x:self.input_click(self.In_GamePwd)
# 确认密码框
        self.In_GamePwd2=QLineEdit()
        self.In_GamePwd2.setFixedSize(400,40)
        self.In_GamePwd2.initText='请再次输入密码'
        self.In_GamePwd2.setTextMargins(5,5,5,5)
        self.In_GamePwd2.setText(self.In_GamePwd2.initText)
        self.In_GamePwd2.mousePressEvent=lambda x:self.input_click(self.In_GamePwd2)
        

        # self.In_GamePwd2.mouse
    


        self.Box=QVBoxLayout()
        self.Box.addWidget(self.Title)
        self.Box.addWidget(self.In_Gmae_id)
        self.Box.addWidget(self.In_Name)
        self.Box.addWidget(self.In_GameName)
        self.Box.addWidget(self.In_GamePwd)
        self.Box.addWidget(self.In_GamePwd2)
        self.Box.addWidget(self.button)
        

        self.setLayout(self.Box)
        
    def input_click(self,Input):
        for i in range(2,6):
            item=self.Box.itemAt(i).widget()
            if item.text()=='':
                item.setText(item.initText)
        if Input.text()==Input.initText:
            Input.setText('')
    def submitFunction(self):
        if self.In_GamePwd.text()=='请输入密码':
            QMessageBox.warning(self, '警告', '请输入密码', QMessageBox.Ok)
            return
        if self.In_GamePwd2.text()=='请再次输入密码':
            QMessageBox.warning(self, '警告', '请再次输入密码', QMessageBox.Ok)
            return
        if self.In_GamePwd.text()!=self.In_GamePwd2.text() :
            QMessageBox.warning(self, '警告', '两次输入的密码不一致，请重新输入', QMessageBox.Ok)
            return
        
        
        
        data=[
            self.In_Gmae_id.text(),self.In_Name.text(),
            self.In_GameName.text(),
            self.In_GamePwd.text()]
        func.insert_data(data)
        QMessageBox.information(self, '成功', '注册成功', QMessageBox.Ok)
        self.close()
        login=Login.Login()
        login.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    signup=Signup()
    signup.show()
    sys.exit(app.exec_())
    
