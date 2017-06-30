#!/usr/bin/pyhton3
#-*- coding:UTF-8 -*-

import _sqlite3
from wxpy import *

#init
bot = Bot()

#通过数据库验证输入的电话号码是否正确
def check_cell_db(cell):
    cx = _sqlite3.connect("tickets.db")
    flag = False
    cell_number=str(cell)
    sql = "select TCELL from TB_TICKETINFO where TCELL != ''"
    cursor = cx.execute(sql)

    for row in cursor:
        if cell_number == str(row[0]) or cell_number == '15927436659' or cell_number == '15951753907' or cell_number == '18051990912':
            print (cell_number)
            flag = True
            break

    cx.close()
    print (flag)
    return flag

#加群以后修改数据库状态
def set_db_status(cell):
    cx = _sqlite3.connect("tickets.db")
    flag = False
    cell_number = str(cell)
    sql = "update TB_TICKETINFO set TSTATUS = 1 where TCELL = '%s'" % cell_number
    print(sql)
    cx.execute(sql)
    cx.commit()
    cx.close()

def invite(user):
	group = bot.groups().search('Nanjing Conference')
	group[0].add_members(user, use_invitation=True)

#自动拉好友进微信群
@bot.register(chats=Friend)
def auto_invite_group(msg):
    print ("start invitation")
    print (msg.text)

    strText = str(msg.text)
    if strText.isdigit() == False:
        msg.chat.send('Hello{}, please only give me the cell number to buy Nanjing Conference ticket'.format(msg.chat.name))
        msg.chat.send('您好{}, 请只给我您购票用的手机号码'.format(msg.chat.name))
        return

    if check_cell_db(msg.text):
        set_db_status(msg.text)
        invite(msg.chat)
    else:
        msg.chat.send('Hello{}, please give me the correct cell number you used to buy Nanjing Conference tickets'.format(msg.chat.name))
        msg.chat.send('您好{}, 请给我正确的您购买南京峰会门票时注册的手机号码'.format(msg.chat.name))

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    print ('start add friends')
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    if check_cell_db(msg.text):
        set_db_status(msg.text)
        print (msg.text)
        new_friend.send( 'Hello {}, welcome to Nanjing Conference tickets'.format(new_friend.name))
        new_friend.send('您好 {}，欢迎参加南京峰会'.format(new_friend.name))
        invite(new_friend)
    else:
        new_friend.send('Hello {}, please send me the cell you used to buy Nanjing Conference tickets'.format(new_friend.name))
        new_friend.send('您好 {}，请给我您购买南京峰会门票时注册的手机号码'.format(new_friend.name))

embed()