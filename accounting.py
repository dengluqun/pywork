# -*- coding:gbk -*-
import datetime

def readfile(fileroad):#��ȡ�ļ�
    f=open('%s'%fileroad)
    filelists=f.readlines()
    f.close()
    return filelists

def writefile(fileroad,content):#д���ļ�
    f=open('%s'%fileroad,'a')
    f.writelines(content)
    f.close()

def gettime():#��ȡ��ǰʱ��
    t=datetime.datetime.now()
    y=t.year
    m=t.month
    d=t.day
    return '%d-%d-%d'%(y,m,d)


def diary_input():#��ˮ�˵�����
    global diary
    diary.append(raw_input('\n����ģʽ\n���׶���'))
    diary.append(input('����/��'))
    diary.append(input('֧��/��'))
    diary.append(input('Ӧ���˿�/��'))
    diary.append(input('Ӧ���˿�/��'))
    diary.append(gettime())

def balance_input(balance1,diary1):#�ʲ��������
    zichan=int(balance[1])+diary[1]-diary[2]
    fuzhai=int(balance[2])+diary[4]-diary[3]
    jingzichan=zichan-fuzhai
    print '\n�����Ѽ�¼'
    print'��ǰ�ʲ�״����\n�����ʲ���%d��\n���¸�ծ��%d��\n���¾��ʲ���%d��'%(zichan,fuzhai,jingzichan)
    return '\n%s %d %d %d'%(gettime(),zichan,fuzhai,jingzichan)



#������
mode=input('1.���ˣ�2.����\n��ѡ�����')

diary=[]
balance=[]
balance_new=''
    
if mode==2:   #����
    diary_input()
    
    balance_origin=readfile(r'D:\gitwork\hubpywork\balance.txt')
    balance=balance_origin[-1].split(' ')#ȡԭʼ�ʲ�����
    
    balance_new=balance_input(balance,diary)#���������ʲ�����
    writefile(r'D:\gitwork\hubpywork\balance.txt',balance_new)

    for k in range(len(diary)):
        diary[k]=str(diary[k])
        
    diary_c='\n'+'\t'.join(diary)
    writefile(r'D:\gitwork\hubpywork\diary.txt',diary_c)
    
if mode==1:   #��ѯ
    mode_1=input('����ģʽ\n1.��ѯ���ʮ�ʽ��׼�¼\n2.��ѯ��ĳ��˾��������\n3.��ѯ����ʲ���ծ״��\n��ѡ�����')
    jiaoyifile=readfile(r'D:\gitwork\hubpywork\diary.txt')
    
    if mode_1==1:        
        print '���ʮ�ʽ���'   
        if len(jiaoyifile)<=11:
            for line in jiaoyifile:
                print line 
        else:
            for line in jiaoyifile[:11]:
                print line
                
    if mode_1==2:
        result=[]
        comname=raw_input('�����빫˾����')
        for k in jiaoyifile:
            k1=k.split()
            if k1[0]==comname:
                result.append(k1[1:])
                
        print '��%s����%d�ʽ���'%(comname,len(result))
        for j in range(len(result)):
            print('����ʱ�䣺%s\n���룺%d��\n֧����%d��\nӦ���˿%d��\nӦ���˿%d��\n'%
                  (result[j][4],int(result[j][0]),int(result[j][1]),int(result[j][2]),int(result[j][3])))

    if mode_1==3:
        zuixin=readfile(r'D:\gitwork\hubpywork\balance.txt')
        zuixin1=zuixin[-1].split()
        print('�����ʲ���%d��\n���¸�ծ��%d��\n���¾��ʲ���%d��\n������ʱ�䣺%s'%
              (int(zuixin1[1]),int(zuixin1[2]),int(zuixin1[3]),zuixin1[0]))
        
        
    
