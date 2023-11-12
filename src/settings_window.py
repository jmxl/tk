import tkinter as tk
import tkinter.ttk as ttk


class SettingsWindow(tk.Toplevel):
    def __init__(self, width=400, height=300, center_x=0, center_y=0):
        super().__init__()
        self.__setup_ui()
        self.title('设置')
        self.geometry('%dx%d+%d+%d' % (width, height, center_x - width / 2, center_y - height / 2))

    def __setup_ui(self):
        frame_buttons = tk.Frame(self)
        self.ui_button_cancel = ttk.Button(frame_buttons, text='取消', command=self.__button_cancel_clicked)
        self.ui_button_save = ttk.Button(frame_buttons, text='保存')
        self.ui_button_cancel.pack(side=tk.LEFT, anchor=tk.CENTER, padx=10, pady=10)
        self.ui_button_save.pack(side=tk.RIGHT, anchor=tk.CENTER, padx=10, pady=10)
        frame_buttons.pack(side=tk.BOTTOM)

    def __button_cancel_clicked(self):
        self.destroy()
