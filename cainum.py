# -*- coding:gbk -*-
import random

f=open(r"D:\gitwork\hubpywork\user.txt")
userlists=f.readlines()
f.close()

def yuanshishuju(lists):  #处理原始数据
    scores1={}
    for user in userlists:
        user1=user.split()
        scores1[user1[0]]=user1[1:]
    return scores1

def compare(computer,user,time1):   #猜数字
    if computer> user:
        print("%d 太小了"% user)
        time1+=1
        jieguo=0
    if computer < user:
        print("%d 太大了"% user)
        time1+=1
        jieguo=0
    if computer==user:
        jieguo=1
    return (time1,jieguo)

def yichang():   #异常处理
    global user_num
    yichang_sign=0
    try:
        user_num=input("请输入100以内的数字\n")
    except:
        yichang_sign=1
        
    if yichang_sign==0:    
        if user_num<0 or user_num>100:
            yichang_sign=1
    return yichang_sign

def writefile(scores1):#结果处理及写入文件
    result=''
    for s in scores1:
        result+=s+'\t'+'\t'.join(scores1[s])+'\n'
            
    f=open(r"D:\gitwork\hubpywork\user.txt",'w')
    f.write(result)
    f.close()
    
    
#主程序
 
username=raw_input("请输入用户名：")
print('欢迎回来 %s，祝你游戏愉快！'% username)

scores=yuanshishuju(userlists)
score=scores.get(username)

if score is None:  #新用户的处理     
    score=[0,0,0]

cishu=int(score[0])
zonglunshu=int(score[1])
min_time=int(score[2])
    
contin='go'
while contin=='go':#新游戏循环
    
    cishu+=1
    com_num=random.randint(0,100)
    print("猜猜数字是几？")
    sign=False
    time=1
    
    while(sign==False):#猜的次数循环
        print("第%d次"% time)

        while(1): # 异常处理
            yichang1=yichang()
            if yichang1==1:
                continue
            else:
                break

        com_res=compare(com_num,user_num,time) #猜数字
        time=com_res[0]
        jieguo1=com_res[1]

        if jieguo1==1: #猜中后的处理
            zonglunshu+=time
            if min_time==0 or min_time>time:
                min_time=time
            
            print("猜中了！答案就是 %d\n你猜中答案一共用了 %d 次机会\n你一共玩了 %d 次游戏\n你平均 %.2f 次猜中答案\n你最好成绩是 %d 次"%
                  (user_num,time,cishu,float(zonglunshu)/cishu,min_time))
            scores[username]=[str(cishu),str(zonglunshu),str(min_time)]
            
            writefile(scores)#结果写入文件
            sign = True

    user_contin=raw_input('输入"go"再玩一次，否则退出游戏')#是否开始新游戏
    if user_contin == contin:
        print "新游戏"
        continue
    else:
        break
            

