# coding:utf-8

#random 方面的东西
"""
python核心编程6-14习题的解题思路
设计一个"石头,剪子,布"游戏,有时又叫"Rochambeau",你小时候可能玩过,下面是规则.
你和你的对手,在同一时间做出特定的手势,必须是下面一种手势:石头,剪子,布.胜利者从
下面的规则中产生,这个规则本身是个悖论.
(a) 布包石头.
(b)石头砸剪子,
(c)剪子剪破布.在你的计算机版本中,用户输入她/他的选项,计算机找一个随机选项,然后由你
的程序来决定一个胜利者或者平手.注意:最好的算法是尽量少的使用 if 语句.

https://github.com/pythonpeixun/article/blob/master/jdstb.md
"""

import random
guess_list = ["石头", "剪刀", "布"]
win_combination = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]
while True:
    computer = random.choice(guess_list)
    people = input('请输入：石头,剪刀,布\n').strip()
    if people not in guess_list:
        people = input('重新请输入：石头,剪刀,布\n').strip()
        continue
    if computer == people:
        print ("平手，再玩一次！")
    elif [computer, people] in win_combination:
        print ("电脑获胜！")
    else:
        print ("人获胜！")
        break