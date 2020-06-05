# _*_ coding:utf-8 _*_
# Author： zizle
# Created:2020-06-05
# ------------------------
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from frames import WelcomePage, DeliveryClient

app = QApplication(sys.argv)
splash = WelcomePage()
splash.show()
app.processEvents()  # non-blocking
splash.import_packages()
splash.make_client_existed()
# splash.getCurrentAdvertisements()
base_window = DeliveryClient()  # main window
# base_window.running_auto_login()
base_window.module_clicked()
# base_window.module_clicked(module_id=0, module_text=u'首页')  # 启动后显示首页
base_window.show()
splash.finish(base_window)
sys.exit(app.exec_())

