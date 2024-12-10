import sys
from typing import Optional
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton,
    QLineEdit, QStackedWidget
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from person import *
from func import *

class MyWidget(QWidget):
    # 需要传入的信息 字典类型
    info={
            'owner_name':None,
            'gun_derma':None,
            'price':None,
            'gun_name':None,
            'pry_or_not':None
        }
    gun_name=['近战','标配','短炮','狂怒','鬼魅','正义','蜂刺','骇灵','雄鹿','判官','獠犬',
              '戍卫','幻影','狂徒','飞将','莽侠','冥驹','战神','奥丁']

    
    def __init__(self,person_info:Optional[dict]=None):
        super().__init__()
        self.initUI(person_info)
        print("MainWindow")
        print(person_info)
    def initUI(self,person_info:Optional[dict]=None):
        # 创建主布局
        main_layout = QVBoxLayout()
        self.setFixedSize(1000, 700)

        # 第一个盒子
        box1 = QWidget()
        box1.setStyleSheet("background-color: #AA9B39;")  # 盒子背景色
        box1_layout = QHBoxLayout(box1)
        box1_layout.setContentsMargins(10, 10, 10, 10)
        box1_layout.setSpacing(10)
        label = QLabel("Welcome to Valorant交易平台")
        label.setAlignment(Qt.AlignCenter)  # 居中对齐
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        box1_layout.addWidget(label)
        main_layout.addWidget(box1)

        # 导航栏（水平布局）
        navbar = QWidget()
        navbar_layout = QHBoxLayout(navbar)
        navbar_layout.setContentsMargins(10, 10, 10, 10)
        navbar_layout.setSpacing(20)

        
        #在售按钮 
        buy_button = QPushButton("在售")
        #卖出
        sell_button = QPushButton("出售")
        trade_button = QPushButton("交易记录")
        settings_button = QPushButton("账户设置")
        for btn in [buy_button,sell_button, trade_button, settings_button]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #6C757D;
                    color: white;
                    border-radius: 5px;
                    padding: 8px 15px;
                }
                QPushButton:hover {
                    background-color: #5A6268;
                }
            """)
            navbar_layout.addWidget(btn)

        # 将导航栏添加到主布局
        main_layout.addWidget(navbar)

        # 页面切换容器,修改页面储存点击按钮进行修改页面设置。
        self.stack = QStackedWidget()
        self.stack.addWidget(self.createHomePage())  # 首页
        self.stack.addWidget(self.createTradePage())  # 交易记录
        self.stack.addWidget(self.createSettingsPage())  # 账户设置

        # 绑定导航栏按钮点击事件
        
        trade_button.clicked.connect(lambda: self.switchToTradePage())
        settings_button.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        # 将页面切换容器添加到主布局
        main_layout.addWidget(self.stack)
         # 
# 第六个盒子（主要内容区）
        self.box6 = QWidget()
        self.box6_main_layout = QVBoxLayout()

        # 创建标题行（水平布局）
        title_layout = QHBoxLayout()
        label_0 = QLabel('样式')
        label_0.setFixedWidth(181)  # 设置固定宽度
        label_0.setAlignment(Qt.AlignCenter)  # 居中对齐
        label_1 = QLabel('拥有者')
        label_1.setFixedWidth(180)  # 设置固定宽度
        label_1.setAlignment(Qt.AlignCenter)  # 居中对齐
        label_2 = QLabel('皮肤名')
        label_2.setFixedWidth(150)  # 设置固定宽度
        label_2.setAlignment(Qt.AlignCenter)  # 居中对齐
        label_3 = QLabel('价格')
        label_3.setFixedWidth(150)  # 设置固定宽度
        label_3.setAlignment(Qt.AlignCenter)  # 居中对齐
        label_4 = QLabel('枪名')
        label_4.setFixedWidth(150)  # 设置固定宽度
        label_4.setAlignment(Qt.AlignCenter)  # 居中对齐
        label_5 = QLabel('状态')
        label_5.setFixedWidth(150)  # 设置固定宽度
        label_5.setAlignment(Qt.AlignCenter)  # 居中对齐

        # 设置标题样式
        for label in [label_0, label_1, label_2, label_3, label_4, label_5]:
            label.setStyleSheet("font-size: 16px; color: white;")
            label.setFixedHeight(40)  # 设置固定高度
            title_layout.addWidget(label)
        #   调用函数进行内容的添加
        
        content_layout=self.create_box6_content()
        

        # 将两个子布局添加到 box6 的主布局
        self.box6_main_layout.addLayout(title_layout)  # 添加标题行
        self.box6_main_layout.addLayout(content_layout)  # 添加内容行

        # 添加一个拉伸占位符，避免内容被挤压到底部
        self.box6_main_layout.addStretch(1)

        # 设置主布局为 box6 的布局
        self.box6.setLayout(self.box6_main_layout)
        self.box6.setStyleSheet("background-color: lightblue;")  # 设置背景色
        self.box6.setMinimumHeight(550)  # 占主窗口高度一半

        # 将 box6 添加到主布局
        main_layout.addWidget(self.box6)
        # 设置主布局
        self.setLayout(main_layout)


    def create_box6_content(self,dic: Optional[dict] = None):
        """创建box6的内容"""
        # 创建内容行（第二个水平布局）
        if dic is not None:
            
            owner=dic['owner_name']
            skin_name=dic['gun_derma']
            price=dic['price']
            gun_name=dic['gun_name']
            status=dic['pry_or_not']

            pic_path = f'/pic/{skin_name}.jpg'
            content_layout = QHBoxLayout()
            image_1 = QLabel()
            pixmap = QPixmap(pic_path)
            image_1.setPixmap(pixmap)
            image_1.setScaledContents(True)
            image_1.setFixedSize(181, 100)

            content_layout.addWidget(image_1)
            label_1_1=QLabel(owner)
            label_1_1.setFixedWidth(150)  # 设置固定宽度
            label_1_1.setAlignment(Qt.AlignCenter)  # 居中对齐
            content_layout.addWidget(label_1_1)
            label_2_1=QLabel(skin_name)
            label_2_1.setFixedWidth(140)  # 设置固定宽度
            label_2_1.setAlignment(Qt.AlignCenter)  # 居中对齐
            content_layout.addWidget(label_2_1)
            label_3_1=QLabel(price)
            label_3_1.setFixedWidth(140)  # 设置固定宽度
            label_3_1.setAlignment(Qt.AlignCenter)  # 居中对齐
            content_layout.addWidget(label_3_1)
            label_4_1=QLabel(gun_name)
            label_4_1.setFixedWidth(170)  # 设置固定宽度
            label_4_1.setAlignment(Qt.AlignCenter)  # 居中对齐
            content_layout.addWidget(label_4_1)
            label_5_1=QLabel(status)
            label_5_1.setFixedWidth(160)  # 设置固定宽度
            label_5_1.setAlignment(Qt.AlignCenter)  # 居中对齐
            content_layout.addWidget(label_5_1)
        else:
            content_layout=QHBoxLayout()
        return content_layout
    def switchToTradePage(self):
        """切换到交易记录页面并更新box6内容"""
        # 更新box6内容
        self.updateBox6WithTradePage()
        self.stack.setCurrentIndex(1)

    def updateBox6WithTradePage(self):
        """更新box6以显示交易记录相关内容"""
        # 清空box6当前的布局
        for i in reversed(range(self.box6_main_layout.count())):
            widget = self.box6_main_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # 新内容布局（交易记录内容）
        trade_title_layout = QHBoxLayout()
        label_0 = QLabel("交易号")
        label_1 = QLabel("交易金额")

        label_2 = QLabel("状态")
        for label in [label_0, label_1, label_2]:
            label.setStyleSheet("font-size: 16px; color: white;")
            label.setFixedHeight(40)  # 设置固定高度
            trade_title_layout.addWidget(label)

        trade_content_layout = QHBoxLayout()
        trade_content_layout.addWidget(QLabel("交易123"))
        trade_content_layout.addWidget(QLabel("1000元"))
        trade_content_layout.addWidget(QLabel("完成"))
        
        # 添加新的内容到box6布局
        self.box6_main_layout.addLayout(trade_title_layout)
        self.box6_main_layout.addLayout(trade_content_layout)

        self.box6_main_layout.addStretch(1)  # 保证显示区域不被挤压

    def createHomePage(self):
        """创建首页内容"""
        page = QWidget()
        layout = QHBoxLayout(page)
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("搜索在售商品")
        select_bt=QPushButton("筛选")
        search_bt=QPushButton("搜索")

        search_bar.setFixedHeight(50)
        select_bt.setFixedHeight(50)
        search_bt.setFixedHeight(50)
        layout.addWidget(search_bar)
        layout.addWidget(select_bt)
        layout.addWidget(search_bt)

        select_bt.clicked.connect(self.select_clicked)
        search_bt.clicked.connect(self.search_clicked)
        

        return page
    def select_clicked(self):
        pass 
    def search_clicked(self):
        search_name=self.sender().parent().findChild(QLineEdit)
        if search_name.text() in self.gun_name:
            self.info['gun_name']=search_name.text()
    def createTradePage(self):
        """创建交易记录页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("交易记录页面"))
        layout.addWidget(QLineEdit("输入交易号进行查询"))
        layout.addWidget(QPushButton("查询"))
        return page

    def createSettingsPage(self):
        """创建账户设置页面"""
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("账户设置页面"))
        layout.addWidget(QPushButton("修改密码"))
        layout.addWidget(QPushButton("退出登录"))
        return page


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
