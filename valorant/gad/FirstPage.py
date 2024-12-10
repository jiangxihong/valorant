import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import MainWindow
from PyQt5.QtCore import QTimer
from typing import Optional


class MyWidget(QWidget):
    def __init__(self,person_info:Optional[dict]=None):
        super().__init__()
        self.person_info=person_info
        self.initUI(self.person_info)
        

    def initUI(self,person_info:Optional[dict]=None):
        # 创建主布局
        main_layout = QVBoxLayout()
        self.setFixedSize(1100, 600)


        # 创建水平布局
        box1 = QHBoxLayout()

        # 标题
        title_label = QLabel("今日在售")
        title_label.setFixedSize(1050, 30)
        in_btn = QPushButton("进入")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        in_btn.setFixedSize(70, 30)
        in_btn.clicked.connect(self.enter_clicked)
    
        # 将标题和按钮添加到水平布局
        box1.addWidget(title_label)
        box1.addWidget(in_btn)

        # 将水平布局添加到主布局
        main_layout.addLayout(box1)

        # 图片展示区域的布局
        image_layout = QHBoxLayout()

        # 左侧切换按钮
        self.prev_button = QPushButton("<")
        self.prev_button.setFixedSize(50, 50)
        self.prev_button.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.prev_button.clicked.connect(self.handle_prev_click)

        # 图片展示区域
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setScaledContents(True)
        self.image_label.setFixedSize(950, 500)
        self.image_label.mousePressEvent=self.image_clicked

        # 右侧切换按钮
        self.next_button = QPushButton(">")
        self.next_button.setFixedSize(50, 50)
        self.next_button.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.next_button.clicked.connect(self.handle_next_click)

        # 添加按钮和图片到布局
        image_layout.addWidget(self.prev_button)
        image_layout.addWidget(self.image_label)
        image_layout.addWidget(self.next_button)

        # 将图片布局添加到主布局
        main_layout.addLayout(image_layout)

        # 设置主布局
        self.setLayout(main_layout)

        # 图片列表
        self.image_list = [
            'pic/双城之战 狂徒.jpg',
            'pic/堕天遗武 冥驹.jpg'
        ]

        self.current_index = 0

        # 加载第一张图片
        self.update_image()

        # 定时器，用于定期切换图片
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_image)
        self.timer.start(5000)  # 默认每3秒切换一次图片
    def update_image(self):
        """更新当前图片"""
        pixmap = QPixmap(self.image_list[self.current_index])
        if pixmap.isNull():
            print(f"无法加载图片: {self.image_list[self.current_index]}")
        else:
            self.image_label.setPixmap(pixmap)

    def next_image(self):
        """切换到下一张图片"""
        self.current_index = (self.current_index + 1) % len(self.image_list)
        self.update_image()

    def prev_image(self):
        """切换到上一张图片"""
        self.current_index = (self.current_index - 1) % len(self.image_list)
        self.update_image()

    def handle_next_click(self):
        """处理点击右侧按钮的事件"""
        self.next_image()
        self.reset_timer(10000)  # 将定时器时间改为10秒

    def handle_prev_click(self):
        """处理点击左侧按钮的事件"""
        self.prev_image()
        self.reset_timer(10000)  # 将定时器时间改为10秒

    def reset_timer(self, interval):
        """重置定时器的超时时间"""
        self.timer.stop()
        self.timer.start(interval)
    def image_clicked(self,event):
        """处理图片被点击的事件"""
        print("图片被点击")
    def enter_clicked(self):
        """处理进入按钮被点击的事件"""
        print("进入按钮被点击")
        self.hide()
        self.window=MainWindow.MyWidget(self.person_info)
        self.window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
