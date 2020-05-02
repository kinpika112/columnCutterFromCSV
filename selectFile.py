# -*- coding: utf8 -*-
import sys
import os
import tkinter
import tkinter.filedialog
import tkinter.messagebox


def selectFile(form: tkinter.Entry):
    root = tkinter.Tk()
    root.withdraw()

    # ファイルタイプの指定
    file_type = [('csvファイル', '*.csv')]
    # 初期フォルダの設定
    init_path = os.path.abspath(os.path.dirname(__file__))
    # パス取得
    file_path = tkinter.filedialog.askopenfilename(initialdir=init_path, filetypes=file_type)
    # フォームに反映
    form.delete(0, tkinter.END)
    form.insert(tkinter.END, file_path)
    form.icursor(tkinter.END)
