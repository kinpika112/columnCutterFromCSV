# -*- coding: utf8 -*-
import sys
import pandas
import tkinter.messagebox as tkm
import os.path


# ボタンを押したとき実行される
def ExecuteMain(arg_string, file_path):
    """
    処理のmain制御です。
    :param arg_string: 列番号が,区切りでInputされます。
    :param file_path: 読み込むcsvファイル名
    """
    # 値チェック
    column_list = Validation(arg_string, file_path)
    if not column_list:  # リストの長さをみたい
        return

    # 実行
    _continue_flag = tkm.askyesno(u'実行確認', u'実行しますか？（ファイルを上書きします）')
    if _continue_flag:
        DoCut(column_list, file_path)
        tkm.showinfo(u'正常終了', u'ファイルを上書き保存しました')
    else:
        tkm.showinfo(u'正常終了', u'実行がキャンセルされました')


def Validation(arg_string, file_path):
    """
    入力値チェックを行います。
    　　NGの場合、何も返却しません。OKの場合、列番号のlistを返却します。
    :param arg_string: 列番号が,区切りでInputされます。
    :param file_path: 読み込むcsvファイル名
    """
    if arg_string == '' or file_path == '':
        tkm.showerror(u'実行エラー', u'列番号もしくはファイルが指定されていません。')
        return False

    # ,区切りを分割してすべてが半角数字であることをチェックする
    list_ = arg_string.split(',')
    #    print(list_)
    for str_ in list_:
        if str_ == '' or not str_.isdecimal():
            tkm.showerror(u'実行エラー', u'列番号の指定は半角英数字のみです。\r\n複数指定する場合は,区切りとしてください。\r\n例：[1,2,3]')
            return False

    # ファイルの存在チェック
    if not os.path.exists(file_path):
        tkm.showerror(u'実行エラー', u'指定したファイルが存在しませんでした。\r\nファイルパス:[' + file_path + ']')
        return False

    return list_


def DoCut(column_list, file_path):
    """
    削除main処理です。
    　　失敗したらダイアログを表示して終了します。
    :param column_list: 列番号（半角数字）のリスト
    :param file_path: 読み込むcsvファイル名
    """
    f = pandas.read_csv(file_path)

    for i in column_list:
        f[f.columns[(int(i) - 1)]] = f.mask(f[f.columns[(int(i) - 1)]] != '', '***')

    f.to_csv(file_path)
