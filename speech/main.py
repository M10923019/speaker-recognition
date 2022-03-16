# -*- coding:utf-8 -*-

from Speaker_Recognition.register import train_model
from Speaker_Recognition.speakerrecog import speakerRecog


if __name__ == "__main__":
    while 1:
        args = input("輸入： 1--註冊 2--辨識 0--退出：")
        flag = int(args)
        if  flag == 1:
            print("開始音頻註冊錄製(10s)....\n")
            train_model()
        elif flag == 2:
            print("開始音頻辨識錄製(10s)\n")
            print("識別說話的為：%s " % speakerRecog())
        elif flag == 0:
            break
        else:
            print("指令錯誤，重新開始.......")
            continue