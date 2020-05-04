# -*- coding: utf8 -*-
import sys
import tkinter as tk
# ぼやけ防止（windowsのコンテンツサイズの拡大に合わせてGUIの文字を拡大してくれる）
import ctypes
import executors
import selectFile

# ぼやけ防止（windowsのコンテンツサイズの拡大に合わせてGUIの文字を拡大してくれる）
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# GUIメインモジュール
_root = tk.Tk()
_root.title(u'ColumnCutterFromCSV - csv項目削除ツール')
_root.geometry('800x250')

# 概要
_overview_label = tk.Label(text=u'CSVから指定した項目の値を削除（空値に置換）します（複数項目指定可能）。')
_overview_label.pack()
_overview_label.place(x=5, y=10)

# ラベル
####################################
_1_label = tk.Label(text=u'列番号（1から , 区切りで複数指定）：')
_1_label.pack()
_1_label.place(x=10, y=70)
_2_label = tk.Label(text=u'csvファイル                       ：')
_2_label.pack()
_2_label.place(x=10, y=123)

# フォーム
####################################
# 列番号入力フォーム
_entry = tk.Entry()
_entry.pack()
_entry.place(x=310, y=73)
# ファイル名
_file_entry = tk.Entry(width=40)
_file_entry.pack()
_file_entry.place(x=310, y=123)

# ボタン
####################################
# ファイル参照ボタン
_select_button = tk.Button(text=u'・・・', width=3,
                           command=lambda: selectFile.selectFile(_file_entry))
_select_button.pack()
_select_button.place(x=720, y=115)
# 実行ボタン
_do_button = tk.Button(text=u'削除を実行する', width=20,
                       command=lambda: executors.ExecuteMain(_entry.get(), _file_entry.get()))
# _do_button.bind("<Button-1>", executors.ExecuteMain(_entry.get()))
_do_button.pack()
_do_button.place(x=570, y=190)


# 描画
_root.mainloop()
