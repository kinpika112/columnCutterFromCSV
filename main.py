#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
# ぼやけ防止（windowsのコンテンツサイズの拡大に合わせてGUIの文字を拡大してくれる）
import ctypes
import executors

# ぼやけ防止（windowsのコンテンツサイズの拡大に合わせてGUIの文字を拡大してくれる）
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# GUIメインモジュール
_root = tk.Tk()
_root.title(u'ColumnCutterFromCSV')
_root.geometry('500x200')

# 概要
_overview_label = tk.Label(text=u'CSVから項目そのもの（もしくは項目の値）を削除します（複数項目指定可能）。')
_overview_label.pack()
_overview_label.place(x=5, y=10)

# ラベル
_1_label = tk.Label(text=u'列番号（ , 区切りで複数指定）：')
_1_label.pack()
_1_label.place(x=10, y=40)
_2_label = tk.Label(text=u'csvファイル　　　　　　　　　：')
_2_label.pack()
_2_label.place(x=10, y=73)

# 列番号入力フォーム
_entry = tk.Entry()
_entry.pack()
_entry.place(x=190, y=43)
# ファイル参照ボタン
_select_button = tk.Button(text=u'ファイルを選択', width=10,
                           command=lambda: executors.ExecuteMain(_entry.get(), _file_entry.get()))
_select_button.pack()
_select_button.place(x=190, y=70)

# ファイル名
_file_entry = tk.Entry(width=40)
_file_entry.pack()
_file_entry.place(x=190, y=103)

# 実行ボタン
_do_button = tk.Button(text=u'削除を実行する', width=20,
                       command=lambda: executors.ExecuteMain(_entry.get(), _file_entry.get()))
# _do_button.bind("<Button-1>", executors.ExecuteMain(_entry.get()))
_do_button.pack()
_do_button.place(x=320, y=160)

# 描画
_root.mainloop()
