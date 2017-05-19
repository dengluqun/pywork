# -*- coding:gbk -*-
import datetime
import os

def writefile(fileroad,content):#写入文件
    f=open('%s'%fileroad,'a')
    f.writelines(content)
    f.close()

def init(filename,data):#文件初始化
    if not(os.path.exists(filename)):
        writefile(filename,data)

def readfile(fileroad):#读取文件
    try:
        f=open('%s'%fileroad)
    except:
        print '文件不存在，程序结束'
    filelists=f.readlines()
    f.close()
    return filelists


def gettime():#获取当前时间
    t=datetime.datetime.now()
    y=t.year
    m=t.month
    d=t.day
    return '%d-%d-%d'%(y,m,d)


def diary_input():#流水账单输入
    global diary
    diary.append(raw_input('\n记账模式\n交易对象：'))
    diary.append(input('收入/万：'))
    diary.append(input('支出/万：'))
    diary.append(input('应收账款/万：'))
    diary.append(input('应出账款/万：'))
    diary.append(gettime())

def balance_input(balance1,diary1):#资产情况输入
    zichan=int(balance[1])+diary[1]-diary[2]
    fuzhai=int(balance[2])+diary[4]-diary[3]
    jingzichan=zichan-fuzhai
    print '\n交易已记录'
    print'当前资产状况：\n最新资产：%d万\n最新负债：%d万\n最新净资产：%d万'%(zichan,fuzhai,jingzichan)
    return '\n%s %d %d %d'%(gettime(),zichan,fuzhai,jingzichan)

def mode_error(user_input,modeset):#模式错误处理
    sign=True
    while sign:
        try:
            mode_user=input(user_input)
        except:
            print '输入错误，请输入数字'
            continue

        if mode_user not in modeset: 
            print '输入错误，请输入正确的数字'
            continue
        else:
            sign=False
            return mode_user

def fun_init():#程序初始化
    global balance_origin
    global diary_origin
    global tishi1
    global tishi2
    global set
    
    balance_origin='结算日期 资产/w 负债/w 净资产/w\n2016-12-4 200000 10000 190000'
    diary_origin='交易对象 收入/w 支出/w 应收账款/w 应出账款/w 交易日期'
    init('balance.txt',balance_origin)
    init('diary.txt',diary_origin)
    
    tishi1='1.查账；2.记账；3.退出程序\n请选择服务：'
    tishi2='查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债状况\n请选择服务：'
    set=[1,2,3]
        

#主程序

fun_init()
while True:
    mode=mode_error(tishi1,set)

    diary=[]
    balance=[]
    balance_new=''
    
    if mode==2:   #记账
        diary_input()
    
        balance_origin=readfile('balance.txt')
        balance=balance_origin[-1].split(' ')#取原始资产数据
    
        balance_new=balance_input(balance,diary)#计算最新资产数据
        writefile('balance.txt',balance_new)

        for k in range(len(diary)):
            diary[k]=str(diary[k])
        
        diary_c='\n'+'\t'.join(diary)
        writefile('diary.txt',diary_c)
    
    if mode==1:   #查询
        mode_1=mode_error(tishi2,set)

        jiaoyifile=readfile('diary.txt')

        if mode_1==1:        
            print '最近十笔交易'   
            if len(jiaoyifile)<=11:
                for line in jiaoyifile:
                    print line 
            else:
                for line in jiaoyifile[:11]:
                    print line
                
        if mode_1==2:
            result=[]
            comname=raw_input('请输入公司名：')
            for k in jiaoyifile:
                k1=k.split()
                if k1[0]==comname:
                    result.append(k1[1:])
                
            print '与%s共有%d笔交易'%(comname,len(result))
            for j in range(len(result)):
                print('交易时间：%s\n收入：%d万\n支出：%d万\n应收账款：%d万\n应出账款：%d万\n'%
                  (result[j][4],int(result[j][0]),int(result[j][1]),int(result[j][2]),int(result[j][3])))

        if mode_1==3:
            zuixin=readfile('balance.txt')
            zuixin1=zuixin[-1].split()
            print('最新资产：%d万\n最新负债：%d万\n最新净资产：%d万\n最后更新时间：%s'%
              (int(zuixin1[1]),int(zuixin1[2]),int(zuixin1[3]),zuixin1[0]))
    if mode==3:
        break
        
    
