# -*- coding:gbk -*-
import datetime

def readfile(fileroad):#读取文件
    f=open('%s'%fileroad)
    filelists=f.readlines()
    f.close()
    return filelists

def writefile(fileroad,content):#写入文件
    f=open('%s'%fileroad,'a')
    f.writelines(content)
    f.close()

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



#主程序
mode=input('1.查账；2.记账\n请选择服务：')

diary=[]
balance=[]
balance_new=''
    
if mode==2:   #记账
    diary_input()
    
    balance_origin=readfile(r'D:\gitwork\hubpywork\balance.txt')
    balance=balance_origin[-1].split(' ')#取原始资产数据
    
    balance_new=balance_input(balance,diary)#计算最新资产数据
    writefile(r'D:\gitwork\hubpywork\balance.txt',balance_new)

    for k in range(len(diary)):
        diary[k]=str(diary[k])
        
    diary_c='\n'+'\t'.join(diary)
    writefile(r'D:\gitwork\hubpywork\diary.txt',diary_c)
    
if mode==1:   #查询
    mode_1=input('查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债状况\n请选择服务：')
    jiaoyifile=readfile(r'D:\gitwork\hubpywork\diary.txt')
    
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
        zuixin=readfile(r'D:\gitwork\hubpywork\balance.txt')
        zuixin1=zuixin[-1].split()
        print('最新资产：%d万\n最新负债：%d万\n最新净资产：%d万\n最后更新时间：%s'%
              (int(zuixin1[1]),int(zuixin1[2]),int(zuixin1[3]),zuixin1[0]))
        
        
    
