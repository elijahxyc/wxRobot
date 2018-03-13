from wxpy import *
import time

bot = Bot()

bot.self.send('Hello World!')
friends = bot.friends()

#tmc
def getName(name):
    re_name = ''
    if name.find('.') != -1:
        pos = name.rfind('.')
        re_name = name[pos+1:len(name)]
        if re_name.find('zz') != -1:
            pos = re_name.rfind('zz')
            re_name = re_name[pos+1:len(re_name)]  
    elif name.find('zz') != -1:
        pos = name.rfind('zz')
        re_name = name[pos+2:len(name)]
    return re_name

count = 1
count_send = 0

for friend in friends:
    name = str(friend)
    name = name.lstrip('<Friend: ')
    name = name.rstrip('>')

    if name.find('tmc') != -1:
        if count <= 148:
            count = count + 1
            continue
        
        name = getName(name)
        msg = '' + name
        #friend.send(msg)
        count = count + 1
        #count_send = count_send + 1
        #print(msg)
        #print(name)
    elif name.find('zz') != -1 and name.find('yb') == -1 and name.find('zxq') == -1 and name.find('yx') == -1 and name.find('gp') == -1:
        name = getName(name)
        count_send = count_send + 1
        msg = '' + name 
        #friend.send(msg)
        #print(msg)
    
    #if count_send > 0:
        #time.sleep(5)
    
print(count_send)
            
