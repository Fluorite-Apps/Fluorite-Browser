import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QPoint, QRect

global counter_for_tabs
counter_for_tabs = 1

current_dir = os.getcwd()
cookie_path = os.path.join(current_dir, "cookies")

class Browser(QWidget):
    def __init__(self):
        super().__init__()

        # Webview
        self.profile = QWebEngineProfile.defaultProfile()
        self.web_view = QWebEngineView()
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
        self.url_bar.setMinimumWidth(1800)  # Set the minimum width
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

    def back(self):
        self.web_view.back()

    def navigate(self):
        url = self.url_bar.text()
        self.web_view.load(QUrl(url))
        cookie_store = profile.cookieStore()
        cookie_store.setCookie(QUrl(url), bytes("cookie_name=cookie_value", encoding="utf-8"))
        print(url)

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

        # Set fixed tab size
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
        exit_button.triggered.connect(exit)
        self.menuBar().addAction((exit_button))

    def show_settings_page(self):
        # Create new tab with the settings page
        browser = Browser()
        browser.web_view.setHtml("""<h1>Settings page hasn't been implemented yet</h1>
        <p>This page will allow you to change settings in the future</p>""")
        self.tab_widget.addTab(browser, "Settings")

        # Switch to the new tab
        self.tab_widget.setCurrentWidget(browser)

    def show_history_page(self):
        # Create new tab with the settings page
        browser = Browser()
        browser.web_view.setHtml("""<h1>History page hasn't been implemented yet</h1>
        <p>This page will allow you to view your history in the future</p>""")
        self.tab_widget.addTab(browser, "History")

        # Switch to the new tab
        self.tab_widget.setCurrentWidget(browser)

    def show_saved_page(self):
        # Create new tab with the settings page
        browser = Browser()
        browser.web_view.setHtml("""<h1>Saved page hasn't been implemented yet</h1>
        <p>This page will allow you to quickly access websites you've saved in the future</p>""")
        self.tab_widget.addTab(browser, "Saved")

        # Switch to the new tab
        self.tab_widget.setCurrentWidget(browser)

    def add_tab(self):
        # Create new tab
        browser = Browser()
        self.tab_widget.addTab(browser, "New Tab")
        self.tab_widget.setCurrentWidget(browser)

    def close_tab(self, index):
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_pixmap = QPixmap("browsericon.ico")
    my_icon = QIcon(my_pixmap)
    app.setWindowIcon(my_icon)
    browser = TabbedBrowser()
    browser.showMaximized()
    browser.setWindowTitle("Fluorite Browser")
    profile = QWebEngineProfile.defaultProfile()
    profile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
    profile.setPersistentStoragePath(cookie_path)
    sys.exit(app.exec_())
