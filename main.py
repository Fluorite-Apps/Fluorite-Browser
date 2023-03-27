import os
import sys
from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtWebEngineCore import *
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PySide6.QtCore import Qt, QPoint, QRect
import sys
from PySide6 import QtWidgets
import threading
from ui_settings import Ui_MainWindow
from py_toggle import *
from PySide6.QtWebEngineWidgets import QWebEngineView

from BlurWindow.blurWindow import blur

from BlurWindow.blurWindow import GlobalBlur


global counter_for_tabs
counter_for_tabs = 1

current_dir = os.getcwd()
cookie_path = os.path.join(current_dir, "cookies")
settings_path = os.path.join(current_dir, "settings")
cookies_settings_path = (settings_path + "\\cookieson.txt")

global use_cookies
with open(cookies_settings_path, 'r+') as cookies_on:
    use_cookies = cookies_on.read()

class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Webview
        self.profile = QWebEngineProfile.defaultProfile()
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.NoPersistentCookies)  # Set default policy
        self.web_view = QWebEngineView(self)
        self.web_view.setPage(QWebEnginePage(self.profile, self.web_view))
        self.web_view.load(QUrl('https://www.google.com/'))
        self.web_view.urlChanged.connect(self.update_url_bar)
        self.web_view.titleChanged.connect(self.update_tab_name)

        # Set the background color to RGB(33, 37, 45)
        self.web_view.setStyleSheet("background-color: rgb(33, 37, 45);")

        # Back button
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.back)
        self.back_button.setMinimumHeight(25)
        self.back_button.setStyleSheet("""color: gray;
background-color: rgb(33, 37, 45);
font: 700 10pt "Montserrat";
""")
        
        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate)
        self.url_bar.setMinimumHeight(25)
        self.url_bar.setMinimumWidth(1800)  # Set the minimum width (1800)
        self.url_bar.setStyleSheet("""border: 1px solid rgb(33, 37, 45);""")

        # Apply dark mode to every loaded page
        dark_mode_script = """
            var style = document.createElement('style');
            style.textContent = 'html { filter: invert(1) hue-rotate(180deg); background-color: #1a1a1a; } img:not([src*=".svg"]), video { filter: invert(1) hue-rotate(180deg); }';
            document.head.appendChild(style);
        """
        dark_mode_qscript = QWebEngineScript()
        dark_mode_qscript.setName('dark_mode')
        dark_mode_qscript.setInjectionPoint(QWebEngineScript.DocumentReady)
        dark_mode_qscript.setRunsOnSubFrames(True)
        dark_mode_qscript.setWorldId(QWebEngineScript.MainWorld)
        dark_mode_qscript.setSourceCode(dark_mode_script)
        self.web_view.page().scripts().insert(dark_mode_qscript)

        # Layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.back_button)
        hbox.addWidget(self.url_bar)
        hbox.addStretch()
        layout = QVBoxLayout()
        layout.addLayout(hbox)
        layout.addWidget(self.web_view)
        self.setLayout(layout)

        # Check if cookies should be used
        if str(use_cookies) == str(1):
            self.profile.setPersistentCookiesPolicy(QWebEngineProfile.AllowPersistentCookies)

    def back(self):
        self.web_view.back()

    def navigate(self):
        url = self.url_bar.text()
        self.web_view.load(QUrl(url))
        if str(use_cookies) == str(1):
            cookie_store = self.profile.cookieStore()
            cookie_store.setCookie(QUrl(url), bytes("cookie_name=cookie_value", encoding="utf-8"))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

    def update_tab_name(self, title):
        parent = self.parentWidget().parentWidget()  # Get the TabbedBrowser
        index = parent.indexOf(self)  # Get index of current tab
        # Truncate title to 20 characters if it is longer than that
        truncated_title = (title[:17] + '...') if len(title) > 20 else title
        parent.setTabText(index, truncated_title)  # Set tab name to truncated title

class TabbedBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Title Bar
        if sys.platform == 'win32':
            self.setWindowFlag(Qt.FramelessWindowHint)

        # Set background color of main window
        self.setStyleSheet("""background-color: #3C4052;
                        color: gray;""")
        self.setGeometry(0, 0, 800, 600)

        # Tab widget
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        # Tab stylesheet
        self.tab_widget.setStyleSheet("""QTabBar::tab { height: 25px; width: 150px; }
        QTabBar::tab:selected { background-color: rgb(70, 74, 95); }
        QTabBar::tab { background-color: #3C4052; }
        """)

        # Set the background color and shadow
        palette = self.tab_widget.palette()
        palette.setColor(self.tab_widget.backgroundRole(), QColor(60, 64, 82))  # RGB values for #3C4052
        self.tab_widget.setPalette(palette)

        self.setCentralWidget(self.tab_widget)

        # Create first tab
        self.add_tab()

        # Add "+" button to add new tabs
        self.plus_button = QPushButton("+")
        self.plus_button.clicked.connect(self.add_tab)
        self.tab_widget.setCornerWidget(self.plus_button)
        self.plus_button.setStyleSheet("""color: gray;
background-color: rgb(33, 37, 45);
font: 700 12pt "Montserrat";
""")
        self.plus_button.setShortcut("Ctrl+T")

        # Create "Settings", "History", "Saved" and "Exit" buttons in menu bar
        settings_button = QAction("Settings", self)
        settings_button.triggered.connect(self.show_settings_page)
        self.menuBar().addAction(settings_button)
        settings_button.setShortcut("Ctrl+,")

        history_button = QAction("History", self)
        history_button.triggered.connect(self.show_history_page)
        self.menuBar().addAction(history_button)
        history_button.setShortcut("Ctrl+H")

        saved_button = QAction("Saved", self)
        saved_button.triggered.connect(self.show_saved_page)
        self.menuBar().addAction((saved_button))

        exit_button = QAction("Exit", self)
        exit_button.triggered.connect(self.exit_function)
        self.menuBar().addAction((exit_button))

    def show_settings_page(self):
        global settings_window
        settings_window = SettingsWindow()
        settings_window.show()
        return settings_window

    def show_history_page(self):
        # Create new tab with the history page
        browser = Browser()
        browser.web_view.setHtml("""<h1>History page hasn't been implemented yet</h1>
        <p>This page will allow you to view your history in the future</p>""")
        self.tab_widget.addTab(browser, "History")

        # Switch to the new tab
        self.tab_widget.setCurrentWidget(browser)

    def show_saved_page(self):
        # Create new tab with the saved page
        browser = Browser()
        browser.web_view.setHtml("""<h1>Saved page hasn't been implemented yet</h1>
        <p>This page will allow you to quickly access websites you've saved in the future</p>""")
        self.tab_widget.addTab(browser, "Saved")

        # Switch to the new tab
        self.tab_widget.setCurrentWidget(browser)

    def exit_function(self):
        sys.exit()

    def add_tab(self):
        # Create new tab
        browser = Browser()
        self.tab_widget.addTab(browser, "New Tab")
        self.tab_widget.setCurrentWidget(browser)

    def close_tab(self, index):
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)


class SettingsWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None , *args, obj=None, **kwargs):
        super(SettingsWindow, self).__init__(*args, **kwargs, parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(" ")
        GlobalBlur(self.winId(), Dark=True, QWidget=self)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        if sys.platform == 'win32':
            self.setWindowFlag(Qt.FramelessWindowHint)

        self.cookies_on_toggle = PyToggle(
            width=50
        )

        self.apply_button = QPushButton('Apply', parent=self)
        self.apply_button.setMinimumHeight(71)
        self.apply_button.setFixedWidth(281)
        self.apply_button.setStyleSheet('color: gray')
        self.apply_button.clicked.connect(self.settings_apply)

        self.back_button = QPushButton('Back', parent=self)
        self.back_button.setMinimumHeight(71)
        self.back_button.setFixedWidth(131)
        self.back_button.setStyleSheet('color: gray')
        self.back_button.clicked.connect(self.close)

        self.ui.cookies_toggle_layout.addWidget(self.cookies_on_toggle, Qt.AlignCenter, Qt.AlignCenter)
        self.ui.apply_button_layout.addWidget(self.apply_button, Qt.AlignCenter, Qt.AlignCenter)
        self.ui.settings_back_button_layout.addWidget(self.back_button, Qt.AlignCenter, Qt.AlignCenter)

        if use_cookies == str(0):
            self.cookies_on_toggle.setCheckState(Qt.Unchecked)
        else:
            self.cookies_on_toggle.setCheckState(Qt.Checked)

    def settings_apply(self):
        global use_cookies
        with open('settings/cookieson.txt', 'w+') as file:
            file.truncate(0)
            if self.cookies_on_toggle.isChecked() == True:
                file.write("1")
                use_cookies = str("1")
            else:
                file.write("0")
                use_cookies = str("0")

        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_pixmap = QPixmap("browsericon.ico")
    my_icon = QIcon(my_pixmap)
    app.setWindowIcon(my_icon)
    browser = TabbedBrowser()
    browser.showMaximized()
    browser.setWindowTitle("Fluorite Browser")
    if str(use_cookies) == '1':
        profile = QWebEngineProfile.defaultProfile()
        profile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        profile.setPersistentStoragePath(cookie_path)
    else:
        pass
    sys.exit(app.exec())
