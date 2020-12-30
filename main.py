from tkinter import *
from tkinter import ttk
from Othello_CanPutDown import Othello_CanPutDown as CP
from Othello_Result import Othello_Result as OR
once = 0
judge = 0
next_str = "○"
def run_once():
    global once
    if once == 0:
        button23["text"] = "x"
        button32["text"] = "x"
        button45["text"] = "x"
        button54["text"] = "x"
        judge = 1

def set_text2b(b):
    global judge
    global next_str
    next_str=label1["text"][0]
    if(eval(b)['text'] == 'x'):
        #ボタンの識別番号を調べる 
        buttonNumber(b)
        eval(b)["text"]=next_str
        next_str="●" if next_str == "○" else "○"
        label1["text"] = f'{next_str}のターンです'
        array = CP().reverse_check(kiban(), next_str)
        array_button = button()
        for i in range(len(array)):
            array_button[i]["text"] = array[i]
        a = 0
        for i in kiban():
            if i == "x":
                a = a + 1
        if a == 0 and judge == 1:
            judge = judge + 1
            next_str="●" if next_str == "○" else "○"
            label1["text"] = f'{next_str}のターンです'
            array = CP().reverse_check(kiban(), next_str)
            array_button = button()
            for i in range(len(array)):
                array_button[i]["text"] = array[i]
                for i in range(len(array)):
                    array_button[i]["text"] = array[i]
                a = 0
            for i in kiban():
                if i == "x":
                    a = a + 1
        if a != 0:
            judge = 1
        OR().result_check(kiban(), label1, judge)

def button():
    return [button0, button1, button2, button3, button4, button5, button6, button7,
                    button10, button11, button12, button13, button14, button15, button16, button17,
                    button20, button21, button22, button23, button24, button25, button26, button27,
                    button30, button31, button32, button33, button34, button35, button36, button37,
                    button40, button41, button42, button43, button44, button45, button46, button47,
                    button50, button51, button52, button53, button54, button55, button56, button57,
                    button60, button61, button62, button63, button64, button65, button66, button67,
                    button70, button71, button72, button73, button74, button75, button76, button77]
def kiban():

    return [button0['text'], button1['text'], button2['text'],button3['text'],button4['text'],button5['text'],button6['text'],button7['text'],
                   button10['text'], button11['text'], button12['text'],button13['text'],button14['text'],button15['text'],button16['text'],button17['text'],
                   button20['text'], button21['text'], button22['text'],button23['text'],button24['text'],button25['text'],button26['text'],button27['text'],
                   button30['text'],button31['text'],button32['text'],button33['text'],button34['text'],button35['text'],button36['text'],button37['text'], 
                   button40['text'],button41['text'],button42['text'],button43['text'],button44['text'],button45['text'],button46['text'],button47['text'],
                   button50['text'],button51['text'],button52['text'],button53['text'],button54['text'],button55['text'],button56['text'],button57['text'],
                   button60['text'],button61['text'],button62['text'],button63['text'],button64['text'],button65['text'],button66['text'],button67['text'],
                   button70['text'],button71['text'],button72['text'],button73['text'],button74['text'],button75['text'],button76['text'],button77['text']]

# 押されたボタンの識別番号を出力(0-78:高本作)
def buttonNumber(b):
        w = str(b)
        button_num = w.split("n")
        TippingOver(button_num[1])

# 押されたボタンから周囲をチェック(高本作)
def TippingOver(t_num):
    w_num = int(t_num)
    x_num = int(t_num) + 1
    count = 0
    # 右を見る
    while(w_num % 10 != 7):
        w_num = w_num + 1
        print(w_num)
        p = f'button{w_num}'
        print(eval(p)['text'])
        if eval(p)['text'] == '' or eval(p)['text'] == 'x':
            break
        if eval(p)['text'] == next_str:
            if(count > 0):
                for su in range(count):
                    q = f'button{x_num}'
                    eval(q)['text'] = next_str
                    x_num = x_num + 1
                break
        count = count + 1
    
    w_num = int(t_num)
    x_num = int(t_num) - 1
    count = 0
    # 左を見る
    while(w_num % 10 != 0):
        w_num = w_num - 1
        print(w_num)
        p = f'button{w_num}'
        print(eval(p)['text'])
        if eval(p)['text'] == '' or eval(p)['text'] == 'x':
            break
        if eval(p)['text'] == next_str:
            if(count > 0):
                for su in range(count):
                    q = f'button{x_num}'
                    eval(q)['text'] = next_str
                    x_num = x_num - 1
                break
        count = count + 1
    
    # 上を見る
    w_num = int(t_num)
    x_num = int(t_num) - 10
    count = 0
    while(w_num > 7):
        w_num = w_num - 10
        print(w_num)
        p = f'button{w_num}'
        print(eval(p)['text'])
        if eval(p)['text'] == '' or eval(p)['text'] == 'x':
            break
        if eval(p)['text'] == next_str:
            if(count > 0):
                for su in range(count):
                    q = f'button{x_num}'
                    eval(q)['text'] = next_str
                    x_num = x_num - 10
                break
        count = count + 1

    # 下を見る
    w_num = int(t_num)
    x_num = int(t_num) + 10
    count = 0
    while(w_num < 70):
        w_num = w_num + 10
        print(w_num)
        p = f'button{w_num}'
        print(eval(p)['text'])
        if eval(p)['text'] == '' or eval(p)['text'] == 'x':
            break
        if eval(p)['text'] == next_str:
            if(count > 0):
                for su in range(count):
                    q = f'button{x_num}'
                    eval(q)['text'] = next_str
                    x_num = x_num + 10
                break
        count = count + 1

    # 右下を見る
    w_num = int(t_num)
    x_num = int(t_num) + 11
    count = 0
    while(w_num < 70 and w_num % 10 != 7):
        w_num = w_num + 11
        print(w_num)
        p = f'button{w_num}'
        print(eval(p)['text'])
        if eval(p)['text'] == '' or eval(p)['text'] == 'x':
            break
        if eval(p)['text'] == next_str:
            if(count > 0):
                for su in range(count):
                    q = f'button{x_num}'
                    eval(q)['text'] = next_str
                    x_num = x_num + 11
                break
        count = count + 1

    # 左上を見る
    w_num = int(t_num)
    x_num = int(t_num) - 11
    count = 0
    while(w_num > 7 and w_num % 10 != 0):
        w_num = w_num - 11
        print(w_num)
        p = f'button{w_num}'
        print(eval(p)['text'])
        if eval(p)['text'] == '' or eval(p)['text'] == 'x':
            break
        if eval(p)['text'] == next_str:
            if(count > 0):
                for su in range(count):
                    q = f'button{x_num}'
                    eval(q)['text'] = next_str
                    x_num = x_num - 11
                break
        count = count + 1

    # 右上を見る
    w_num = int(t_num)
    x_num = int(t_num) - 9
    count = 0
    while(w_num > 7 and w_num % 10 != 7):
        w_num = w_num - 9
        print(w_num)
        p = f'button{w_num}'
        print(eval(p)['text'])
        if eval(p)['text'] == '' or eval(p)['text'] == 'x':
            break
        if eval(p)['text'] == next_str:
            if(count > 0):
                for su in range(count):
                    q = f'button{x_num}'
                    eval(q)['text'] = next_str
                    x_num = x_num - 9
                break
        count = count + 1

    # 左下を見る
    w_num = int(t_num)
    x_num = int(t_num) + 9
    count = 0
    while(w_num < 70 and w_num % 10 != 0):
        w_num = w_num + 9
        print(w_num)
        p = f'button{w_num}'
        print(eval(p)['text'])
        if eval(p)['text'] == '' or eval(p)['text'] == 'x':
            break
        if eval(p)['text'] == next_str:
            if(count > 0):
                for su in range(count):
                    q = f'button{x_num}'
                    eval(q)['text'] = next_str
                    x_num = x_num + 9
                break
        count = count + 1

                       
if __name__ == '__main__':
    
    root = Tk()
    root.title('オセロ')
    root.resizable(width=False, height=False)
    frame = ttk.Frame(root, padding=10)
    frame.grid(sticky=(E, W, S, N))
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    label1 = ttk.Label(frame, text="●のターンです")
    label1.grid(row=0, column=0, columnspan=10, stick=(N, S))
    
    s = ttk.Style()
    s.theme_use('classic')
    s.configure('MyWidget.TButton', background='#4db56a',padding=[0,18],width=6)
    s.map("MyWidget.TButton", background=[("disabled", "#4db56a")])
    
    button0 = ttk.Button(frame,style='MyWidget.TButton')
    button0["command"]=lambda: set_text2b('button0')
    button0.grid(row=1, column=0, stick=(E, W, S, N))
    button1 = ttk.Button(frame,style='MyWidget.TButton')
    button1["command"]=lambda: set_text2b('button1')
    button1.grid(row=1, column=1, stick=(E, W, S, N))
    button2 = ttk.Button(frame,style='MyWidget.TButton')
    button2["command"]=lambda: set_text2b('button2')
    button2.grid(row=1, column=2, stick=(E, W, S, N))
    button3 = ttk.Button(frame,style='MyWidget.TButton')
    button3["command"]=lambda: set_text2b('button3')
    button3.grid(row=1, column=3, stick=(E, W, S, N))
    button4 = ttk.Button(frame,style='MyWidget.TButton')
    button4["command"]=lambda: set_text2b('button4')
    button4.grid(row=1, column=4, stick=(E, W, S, N))
    button5 = ttk.Button(frame,style='MyWidget.TButton')
    button5["command"]=lambda: set_text2b('button5')
    button5.grid(row=1, column=5, stick=(E, W, S, N))
    button6 = ttk.Button(frame,style='MyWidget.TButton')
    button6["command"]=lambda: set_text2b('button6')
    button6.grid(row=1, column=6, stick=(E, W, S, N))
    button7 = ttk.Button(frame,style='MyWidget.TButton')
    button7["command"]=lambda: set_text2b('button7')
    button7.grid(row=1, column=7, stick=(E, W, S, N))

    button10 = ttk.Button(frame,style='MyWidget.TButton')
    button10["command"]=lambda: set_text2b('button10')
    button10.grid(row=2, column=0, stick=(E, W, S, N))
    button11 = ttk.Button(frame,style='MyWidget.TButton')
    button11["command"]=lambda: set_text2b('button11')
    button11.grid(row=2, column=1, stick=(E, W, S, N))
    button12 = ttk.Button(frame,style='MyWidget.TButton')
    button12["command"]=lambda: set_text2b('button12')
    button12.grid(row=2, column=2, stick=(E, W, S, N))
    button13 = ttk.Button(frame,style='MyWidget.TButton')
    button13["command"]=lambda: set_text2b('button13')
    button13.grid(row=2, column=3, stick=(E, W, S, N))
    button14 = ttk.Button(frame,style='MyWidget.TButton')
    button14["command"]=lambda: set_text2b('button14')
    button14.grid(row=2, column=4, stick=(E, W, S, N))
    button15 = ttk.Button(frame,style='MyWidget.TButton')
    button15["command"]=lambda: set_text2b('button15')
    button15.grid(row=2, column=5, stick=(E, W, S, N))
    button16 = ttk.Button(frame,style='MyWidget.TButton')
    button16["command"]=lambda: set_text2b('button16')
    button16.grid(row=2, column=6, stick=(E, W, S, N))
    button17 = ttk.Button(frame,style='MyWidget.TButton')
    button17["command"]=lambda: set_text2b('button17')
    button17.grid(row=2, column=7, stick=(E, W, S, N))

    button20 = ttk.Button(frame,style='MyWidget.TButton')
    button20["command"]=lambda: set_text2b('button20')
    button20.grid(row=3, column=0, stick=(E, W, S, N))
    button21 = ttk.Button(frame,style='MyWidget.TButton')
    button21["command"]=lambda: set_text2b('button21')
    button21.grid(row=3, column=1, stick=(E, W, S, N))
    button22 = ttk.Button(frame,style='MyWidget.TButton')
    button22["command"]=lambda: set_text2b('button22')
    button22.grid(row=3, column=2, stick=(E, W, S, N))
    button23 = ttk.Button(frame,style='MyWidget.TButton')
    button23["command"]=lambda: set_text2b('button23')
    button23.grid(row=3, column=3, stick=(E, W, S, N))
    button24 = ttk.Button(frame,style='MyWidget.TButton')
    button24["command"]=lambda: set_text2b('button24')
    button24.grid(row=3, column=4, stick=(E, W, S, N))
    button25 = ttk.Button(frame,style='MyWidget.TButton')
    button25["command"]=lambda: set_text2b('button25')
    button25.grid(row=3, column=5, stick=(E, W, S, N))
    button26 = ttk.Button(frame,style='MyWidget.TButton')
    button26["command"]=lambda: set_text2b('button26')
    button26.grid(row=3, column=6, stick=(E, W, S, N))
    button27 = ttk.Button(frame,style='MyWidget.TButton')
    button27["command"]=lambda: set_text2b('button27')
    button27.grid(row=3, column=7, stick=(E, W, S, N))

    button30 = ttk.Button(frame,style='MyWidget.TButton')
    button30["command"]=lambda: set_text2b('button30')
    button30.grid(row=4, column=0, stick=(E, W, S, N))
    button31 = ttk.Button(frame,style='MyWidget.TButton')
    button31["command"]=lambda: set_text2b('button31')
    button31.grid(row=4, column=1, stick=(E, W, S, N))
    button32 = ttk.Button(frame,style='MyWidget.TButton')
    button32["command"]=lambda: set_text2b('button32')
    button32.grid(row=4, column=2, stick=(E, W, S, N))
    button33 = ttk.Button(frame,style='MyWidget.TButton')
    button33["command"]=lambda: set_text2b('button33')
    button33.grid(row=4, column=3, stick=(E, W, S, N))
    button33["text"]="○"
    button33["state"] = "disable"
    button34 = ttk.Button(frame,style='MyWidget.TButton')
    button34["command"]=lambda: set_text2b('button34')
    button34.grid(row=4, column=4, stick=(E, W, S, N))
    button34["text"]="●"
    button34["state"] = "disable"
    button35 = ttk.Button(frame,style='MyWidget.TButton')
    button35["command"]=lambda: set_text2b('button35')
    button35.grid(row=4, column=5, stick=(E, W, S, N))
    button36 = ttk.Button(frame,style='MyWidget.TButton')
    button36["command"]=lambda: set_text2b('button36')
    button36.grid(row=4, column=6, stick=(E, W, S, N))
    button37 = ttk.Button(frame,style='MyWidget.TButton')
    button37["command"]=lambda: set_text2b('button37')
    button37.grid(row=4, column=7, stick=(E, W, S, N))

    button40 = ttk.Button(frame,style='MyWidget.TButton')
    button40["command"]=lambda: set_text2b('button40')
    button40.grid(row=5, column=0, stick=(E, W, S, N))
    button41 = ttk.Button(frame,style='MyWidget.TButton')
    button41["command"]=lambda: set_text2b('button41')
    button41.grid(row=5, column=1, stick=(E, W, S, N))
    button42 = ttk.Button(frame,style='MyWidget.TButton')
    button42["command"]=lambda: set_text2b('button42')
    button42.grid(row=5, column=2, stick=(E, W, S, N))
    button43 = ttk.Button(frame,style='MyWidget.TButton')
    button43["command"]=lambda: set_text2b('button43')
    button43.grid(row=5, column=3, stick=(E, W, S, N))
    button43["text"]="●"
    button43["state"] = "disable"
    button44 = ttk.Button(frame,style='MyWidget.TButton')
    button44["command"]=lambda: set_text2b('button44')
    button44.grid(row=5, column=4, stick=(E, W, S, N))
    button44["text"]="○"
    button44["state"] = "disable"
    button45 = ttk.Button(frame,style='MyWidget.TButton')
    button45["command"]=lambda: set_text2b('button45')
    button45.grid(row=5, column=5, stick=(E, W, S, N))
    button46 = ttk.Button(frame,style='MyWidget.TButton')
    button46["command"]=lambda: set_text2b('button46')
    button46.grid(row=5, column=6, stick=(E, W, S, N))
    button47 = ttk.Button(frame,style='MyWidget.TButton')
    button47["command"]=lambda: set_text2b('button47')
    button47.grid(row=5, column=7, stick=(E, W, S, N))

    button50 = ttk.Button(frame,style='MyWidget.TButton')
    button50["command"]=lambda: set_text2b('button50')
    button50.grid(row=6, column=0, stick=(E, W, S, N))
    button51 = ttk.Button(frame,style='MyWidget.TButton')
    button51["command"]=lambda: set_text2b('button51')
    button51.grid(row=6, column=1, stick=(E, W, S, N))
    button52 = ttk.Button(frame,style='MyWidget.TButton')
    button52["command"]=lambda: set_text2b('button52')
    button52.grid(row=6, column=2, stick=(E, W, S, N))
    button53 = ttk.Button(frame,style='MyWidget.TButton')
    button53["command"]=lambda: set_text2b('button53')
    button53.grid(row=6, column=3, stick=(E, W, S, N))
    button54 = ttk.Button(frame,style='MyWidget.TButton')
    button54["command"]=lambda: set_text2b('button54')
    button54.grid(row=6, column=4, stick=(E, W, S, N))
    button55 = ttk.Button(frame,style='MyWidget.TButton')
    button55["command"]=lambda: set_text2b('button55')
    button55.grid(row=6, column=5, stick=(E, W, S, N))
    button56 = ttk.Button(frame,style='MyWidget.TButton')
    button56["command"]=lambda: set_text2b('button56')
    button56.grid(row=6, column=6, stick=(E, W, S, N))
    button57 = ttk.Button(frame,style='MyWidget.TButton')
    button57["command"]=lambda: set_text2b('button57')
    button57.grid(row=6, column=7, stick=(E, W, S, N))

    button60 = ttk.Button(frame,style='MyWidget.TButton')
    button60["command"]=lambda: set_text2b('button60')
    button60.grid(row=7, column=0, stick=(E, W, S, N))
    button61 = ttk.Button(frame,style='MyWidget.TButton')
    button61["command"]=lambda: set_text2b('button61')
    button61.grid(row=7, column=1, stick=(E, W, S, N))
    button62 = ttk.Button(frame,style='MyWidget.TButton')
    button62["command"]=lambda: set_text2b('button62')
    button62.grid(row=7, column=2, stick=(E, W, S, N))
    button63 = ttk.Button(frame,style='MyWidget.TButton')
    button63["command"]=lambda: set_text2b('button63')
    button63.grid(row=7, column=3, stick=(E, W, S, N))
    button64 = ttk.Button(frame,style='MyWidget.TButton')
    button64["command"]=lambda: set_text2b('button64')
    button64.grid(row=7, column=4, stick=(E, W, S, N))
    button65 = ttk.Button(frame,style='MyWidget.TButton')
    button65["command"]=lambda: set_text2b('button65')
    button65.grid(row=7, column=5, stick=(E, W, S, N))
    button66 = ttk.Button(frame,style='MyWidget.TButton')
    button66["command"]=lambda: set_text2b('button66')
    button66.grid(row=7, column=6, stick=(E, W, S, N))
    button67 = ttk.Button(frame,style='MyWidget.TButton')
    button67["command"]=lambda: set_text2b('button67')
    button67.grid(row=7, column=7, stick=(E, W, S, N))

    button70 = ttk.Button(frame,style='MyWidget.TButton')
    button70["command"]=lambda: set_text2b('button70')
    button70.grid(row=8, column=0, stick=(E, W, S, N))
    button71 = ttk.Button(frame,style='MyWidget.TButton')
    button71["command"]=lambda: set_text2b('button71')
    button71.grid(row=8, column=1, stick=(E, W, S, N))
    button72 = ttk.Button(frame,style='MyWidget.TButton')
    button72["command"]=lambda: set_text2b('button72')
    button72.grid(row=8, column=2, stick=(E, W, S, N))
    button73 = ttk.Button(frame,style='MyWidget.TButton')
    button73["command"]=lambda: set_text2b('button73')
    button73.grid(row=8, column=3, stick=(E, W, S, N))
    button74 = ttk.Button(frame,style='MyWidget.TButton')
    button74["command"]=lambda: set_text2b('button74')
    button74.grid(row=8, column=4, stick=(E, W, S, N))
    button75 = ttk.Button(frame,style='MyWidget.TButton')
    button75["command"]=lambda: set_text2b('button75')
    button75.grid(row=8, column=5, stick=(E, W, S, N))
    button76 = ttk.Button(frame,style='MyWidget.TButton')
    button76["command"]=lambda: set_text2b('button76')
    button76.grid(row=8, column=6, stick=(E, W, S, N))
    button77 = ttk.Button(frame,style='MyWidget.TButton')
    button77["command"]=lambda: set_text2b('button77')
    button77.grid(row=8, column=7, stick=(E, W, S, N))
    
    run_once()
    root.mainloop()
