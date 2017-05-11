# -*- coding:utf-8 -*-

f=open(r'D:\gitwork\hubpywork\report.txt')
reportlines=f.readlines()
#print reportlines
f.close()

reportline=[]
sum_avg=[]  #每个学生的总分和平均分
sumzong=[]  #每一科的平均分

sumzong.append('平均')
for k in range(1,10):
    sumzong.append(0)
    
for report in reportlines[:2]:
    reportline=report.split()
#    stu=reportline[0]
    
    for n in range(1,10):
        reportline[n]=int(reportline[n]) #每个学生的成绩转换为数字
        sumzong[n]+=reportline[n]

    sum1=sum(reportline[1:])#计算每个学生的总分
    avg=float(sum1/9)#计算每个学生的平均分
    sum_avg.append('%d %.1f'%(sum1,avg))

zong=0
for i in range(1,10):
    sumzong[i]=sumzong[i]/2
    zong+=sumzong[i]

sumzong.append(zong)
sumzong.append(float(zong/9))

print sumzong
print sum_avg

        

    

