#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter.messagebox as tkm


# ボタンを押したとき実行される
def ExecuteMain(arg_string, file_name):
    """
    処理のmain制御です。
    :param arg_string: 列番号が,区切りでInputされます。
    :param file_name: 読み込むcsvファイル名
    """
    # 値チェック
    column_list = Validation(arg_string, file_name)
    if not column_list:  # リストの長さをみたい
        return

    # 実行
    _continue_flag = tkm.askyesno(u'実行確認', u'実行しますか？')
    if _continue_flag:
        DoCut(column_list, file_name)
    else:
        tkm.showinfo(u'正常終了', u'実行がキャンセルされました')
        return


def Validation(arg_string, file_name):
    """
    入力値チェックを行います。NGの場合、何も返却しません。OKの場合、列番号のlistを返却します。
    :param arg_string: 列番号が,区切りでInputされます。
    :param file_name: 読み込むcsvファイル名
    """
    if arg_string == '' or file_name == '':
        tkm.showerror(u'実行エラー', u'列番号もしくはファイルが指定されていません。')
        return

    # ,区切りを分割してすべてが半角数字であることをチェックする

    # ファイルの存在チェック

    return '分割したリストを返却'


def DoCut(column_list, file_name):
    """
    削除main処理です。失敗したらダイアログを表示して終了します。
    :param column_list: 列番号（半角数字）のリスト
    :param file_name: 読み込むcsvファイル名
    """
    print(u'test')
