# -*- coding: utf-8 -*-
#  author: andrew budzan
# project: vf-corp-auto
#  script: classes.py
#    date: 22.01.2020
""" SAP GUI architecture

root
    |- application
        |- connections
            |- sessions
                |- main_window
                    |- menu_bar
                    |- tool_bar1
                    |- title_bar
                    |- tool_bar2
                    |- user_area
                    |- status_bar
"""


from pysap.base import ComObject, SapContainer


class MenuBar(SapContainer):
    def __init__(self, com):
        super().__init__(com)


class ToolBar(SapContainer):
    def __init__(self, com):
        super().__init__(com)


class TitleBar(SapContainer):
    def __init__(self, com):
        super().__init__(com)


class UserArea(SapContainer):
    def __init__(self, com):
        super().__init__(com)


class StatusBar(SapContainer):
    def __init__(self, com):
        super().__init__(com)


class MainWindow(SapContainer):
    def __init__(self, com):
        super().__init__(com)


class Session(SapContainer):
    def __init__(self, com):
        super().__init__(com)


class Connection(SapContainer):
    def __init__(self, com):
        super().__init__(com)


class Application(SapContainer):
    def __init__(self, com):
        super().__init__(com)



if __name__ == '__main__':
    pass