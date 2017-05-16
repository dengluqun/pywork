# -*- coding:gbk -*-

f=open(r'D:\gitwork\hubpywork\report.txt')
reportlines=f.readlines()

f.close()

reportline=[]
sumstu=[]  #每个学生的总分和平均分
avgstu=[]  #每个学生的平均分
sumzong=[]  #每一科的平均分
result=[]

sumzong.append('平均')
for k in range(1,10):
    sumzong.append(0)
    
for report in reportlines:
    reportline=report.split()
    #print reportline
    
    for n in range(1,10):
        reportline[n]=int(reportline[n]) #每个学生的成绩转换为数字
        sumzong[n]+=reportline[n] #每一科的总分

    sum1=sum(reportline[1:])#计算每个学生的总分
    avg=float(sum1/9)#计算每个学生的平均分
    '''sumstu.append(sum1)
    avgstu.append(avg)'''
    reportline.append(sum1)
    reportline.append(avg)
    result.append(reportline)
    
    
zong=0
for i in range(1,10):  #计算总的总分及总平均分
    sumzong[i]=sumzong[i]/len(reportlines) #计算每一科的平均分
    zong+=sumzong[i]

sumzong.append(zong)
sumzong.append(float(zong/9))

result1=sorted(result[1:],key=lambda x:x[10],reverse=True)#排序

result2=[]
result2.append(sumzong)
for n in result1:
    result2.append(n)


for n in range(len(result2)):
    for i in range(1,10):
        if result2[n][i]<60:
            result2[n][i]='不及格'
    for i in range(12):
        result2[n][i]=str(result2[n][i])
        
jieguo=[]
jieguo.append('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%('名称','姓名','语文','数学','英语','物理',
                                                                '化学','生物','政治','历史','地理','总分','平均分'))
for k in range(len(result2)):
   jieguo.append('%d\t'%k+'\t'.join(result2[k])+'\n')


file1=open(r'D:\gitwork\hubpywork\result.txt','w')
file1.writelines(jieguo)
file1.close()


