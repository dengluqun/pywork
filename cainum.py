# -*- coding:gbk -*-
import random

f=open(r"D:\gitwork\hubpywork\user.txt")
userlists=f.readlines()
f.close()

def yuanshishuju(lists):  #����ԭʼ����
    scores1={}
    for user in userlists:
        user1=user.split()
        scores1[user1[0]]=user1[1:]
    return scores1

def compare(computer,user,time1):   #������
    if computer> user:
        print("%d ̫С��"% user)
        time1+=1
        jieguo=0
    if computer < user:
        print("%d ̫����"% user)
        time1+=1
        jieguo=0
    if computer==user:
        jieguo=1
    return (time1,jieguo)

def yichang():   #�쳣����
    global user_num
    yichang_sign=0
    try:
        user_num=input("������100���ڵ�����\n")
    except:
        yichang_sign=1
        
    if yichang_sign==0:    
        if user_num<0 or user_num>100:
            yichang_sign=1
    return yichang_sign

def writefile(scores1):#�������д���ļ�
    result=''
    for s in scores1:
        result+=s+'\t'+'\t'.join(scores1[s])+'\n'
            
    f=open(r"D:\gitwork\hubpywork\user.txt",'w')
    f.write(result)
    f.close()
    
    
#������
 
username=raw_input("�������û�����")
print('��ӭ���� %s��ף����Ϸ��죡'% username)

scores=yuanshishuju(userlists)
score=scores.get(username)

if score is None:  #���û��Ĵ���     
    score=[0,0,0]

cishu=int(score[0])
zonglunshu=int(score[1])
min_time=int(score[2])
    
contin='go'
while contin=='go':#����Ϸѭ��
    
    cishu+=1
    com_num=random.randint(0,100)
    print("�²������Ǽ���")
    sign=False
    time=1
    
    while(sign==False):#�µĴ���ѭ��
        print("��%d��"% time)

        while(1): # �쳣����
            yichang1=yichang()
            if yichang1==1:
                continue
            else:
                break

        com_res=compare(com_num,user_num,time) #������
        time=com_res[0]
        jieguo1=com_res[1]

        if jieguo1==1: #���к�Ĵ���
            zonglunshu+=time
            if min_time==0 or min_time>time:
                min_time=time
            
            print("�����ˣ��𰸾��� %d\n����д�һ������ %d �λ���\n��һ������ %d ����Ϸ\n��ƽ�� %.2f �β��д�\n����óɼ��� %d ��"%
                  (user_num,time,cishu,float(zonglunshu)/cishu,min_time))
            scores[username]=[str(cishu),str(zonglunshu),str(min_time)]
            
            writefile(scores)#���д���ļ�
            sign = True

    user_contin=raw_input('����"go"����һ�Σ������˳���Ϸ')#�Ƿ�ʼ����Ϸ
    if user_contin == contin:
        print "����Ϸ"
        continue
    else:
        break
            

