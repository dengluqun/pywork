# -*- coding:gbk -*-

f=open(r'D:\gitwork\hubpywork\report.txt')
reportlines=f.readlines()
#print reportlines
f.close()

reportline=[]
sumstu=[]  #ÿ��ѧ�����ֺܷ�ƽ����
avgstu=[]  #ÿ��ѧ����ƽ����
sumzong=[]  #ÿһ�Ƶ�ƽ����
result=[]

sumzong.append('ƽ��')
for k in range(1,10):
    sumzong.append(0)
    
for report in reportlines:
    reportline=report.split()
    #print reportline
    
    for n in range(1,10):
        reportline[n]=int(reportline[n]) #ÿ��ѧ���ĳɼ�ת��Ϊ����
        sumzong[n]+=reportline[n] #ÿһ�Ƶ��ܷ�

    sum1=sum(reportline[1:])#����ÿ��ѧ�����ܷ�
    avg=float(sum1/9)#����ÿ��ѧ����ƽ����
    '''sumstu.append(sum1)
    avgstu.append(avg)'''
    reportline.append(sum1)
    reportline.append(avg)
    result.append(reportline)
    
    
#print result
zong=0
for i in range(1,10):  #�����ܵ��ּܷ���ƽ����
    sumzong[i]=sumzong[i]/len(reportlines) #����ÿһ�Ƶ�ƽ����
    zong+=sumzong[i]

sumzong.append(zong)
sumzong.append(float(zong/9))

#for n in range(len(reportlines)):
result2=[]
result2.append(sumzong)
result1=sorted(result[1:],key=lambda x:x[10],reverse=True)

for n in result1:
    result2.append(n)

for n in range(1,len(result2)):
    for i in range(1,10):
        if result2[n][i]<60:
            result2[n][i]='������'
#print result2

for n in range(len(result2)):
    for i in range(1,12):
        result2[n][i]=str(result2[n][i])
            
jieguo=[]
for k in range(len(result2)):
   jieguo.append(' '.join(result2[k])+'\n')

#print jieguo

file1=open(r'D:\gitwork\hubpywork\result.txt','w')
file1.writelines(jieguo)
file1.close()


