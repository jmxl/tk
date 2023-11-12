import tkinter as tk
from app_attributes import AppAttributes
from settings_window import SettingsWindow


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes = AppAttributes()
        self.__setup_ui()

    def __setup_ui(self):
        self.title('{} - {}'.format(self.attributes.title, self.attributes.version))
        self.minsize(width=600, height=480)
        width = 800
        height = 600
        center_x = (self.winfo_screenwidth() - width) / 2
        center_y = (self.winfo_screenheight() - height) / 2
        self.geometry('%dx%d+%d+%d' % (width, height, center_x, center_y))

        self.menubar = tk.Menu(self)
        about_menu = tk.Menu(self.menubar, tearoff=0)
        about_menu.add_command(label='帮助', command=None)
        about_menu.add_command(label='关于', command=None)
        set_menu = tk.Menu(self.menubar, tearoff=0)
        set_menu.add_command(label='设置', command=self.__menu_settings)
        set_menu.add_command(label='恢复默认设置', command=None)
        file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='文件', menu=file_menu)
        self.menubar.add_cascade(label='选项', menu=set_menu)
        self.menubar.add_cascade(label='帮助', menu=about_menu)
        self.config(menu=self.menubar)

    def __menu_settings(self):
        settings = SettingsWindow(center_x=self.winfo_width() / 2 + self.winfo_x(),
                                  center_y=self.winfo_height() / 2 + self.winfo_y())
        settings.mainloop()