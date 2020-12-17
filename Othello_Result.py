from tkinter import *
from tkinter import ttk
class Othello_Result():
    
    def result_check(self,array,label,locate_num): # result_check(self, ボタンの配列情報,ラベル,おける数)
        b_num = 0 #黒石の数
        w_num = 0 #白石の数
        # if文で全部埋まったときと、全部埋まってないけど終了するパターンを分ける
        for i in len(array):
            if array[i] == "●":
                b_num = b_num + 1
            if array[i] == "○":
                w_num = w_num + 1

        sum = b_num + w_num

        if sum == 64 or locate_num == 2: #盤上全てが埋まったときまたは両方置けないとき
            if (b_num > w_num):
                label["text"] = "黒の勝ちです"

            elif (b_num < w_num):
                label["text"] = "白の勝ちです"

            else:
                label["text"] = "引き分けです"

        elif (b_num == 0 or w_num == 0): #盤上が埋まってないけど終了するとき
            if (b_num == 0):
                label["text"] = "白の勝ちです"
            else:
                label["text"] = "黒の勝ちです"

        else: #継続するとき 
            if label["text"][0] == "○":
                label["text"][0] == "●"
                label["text"] = f'{label["text"][0]}のターンです'
            else:
                label["text"][0] == "○"
                label["text"] = f'{label["text"][0]}のターンです'



