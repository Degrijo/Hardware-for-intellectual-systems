
import re
import math

def digit_automate():
    tabl = []
    tabl = [[1 for i in range(32)] for j in range(13)]
    for i in range(32):
        if i>15:
            tabl[0][i] = 0
        if 16>i>7 or 32>i>23:
            tabl[1][i] = 0
        if 8>i>3 or 16>i>11 or 24>i>19 or 32>i>27:
            tabl[2][i] = 0
        if 4>i>1 or 8>i>5 or 12>i>9 or 16>i>13 or 20>i>17 or 24>i>21 or 28>i>25 or 32>i>29:
            tabl[3][i] = 0
        if i%2 == 1:
            tabl[4][i] = 0
        if 31>i>14:
            tabl[5][i] = 0
        if 15>i>6 or 31>i>22:
            tabl[6][i] = 0
        if 9>i>2 or 15>i>10 or 23>i>18 or 31>i>26:
            tabl[7][i] = 0
        if 3>i>0 or 7>i>4 or 11>i>8 or 15>i>12 or 19>i>16 or 23>i>20 or 27>i>24 or 31>i>28:
            tabl[8][i] = 0
        if i%16 == 15:
            tabl[9][i] = 0
        if i%8 == 7:
            tabl[10][i] = 0
        if i%4 == 3:
            tabl[11][i] = 0
        if i%2 == 1:
            tabl[12][i] = 0
    return tabl

h4=""
h3=""
h2=""
h1=""

for i in range(0,len(digit_automate()[9])):
    if digit_automate()[9][i] == 0:
        if digit_automate()[0][i] == 0:
            h4+='!q4*'
        else:
            h4+='q4*'
        if digit_automate()[1][i] == 0:
            h4+='!q3*'
        else:
            h4+='q3*'
        if digit_automate()[2][i] == 0:
            h4+='!q2*'
        else:
            h4+='q2*'
        if digit_automate()[3][i] == 0:
            h4+='!q1*'
        else:
            h4+='q1*'
        if digit_automate()[4][i] == 0:
            h4+='!v+'
        else:
            h4+='v+'
    if digit_automate()[10][i] == 0:
        if digit_automate()[0][i] == 0:
            h3+='!q4*'
        else:
            h3+='q4*'
        if digit_automate()[1][i] == 0:
            h3+='!q3*'
        else:
            h3+='q3*'
        if digit_automate()[2][i] == 0:
            h3+='!q2*'
        else:
            h3+='q2*'
        if digit_automate()[3][i] == 0:
            h3+='!q1*'
        else:
            h3+='q1*'
        if digit_automate()[4][i] == 0:
            h3+='!v+'
        else:
            h3+='v+'
    if digit_automate()[11][i] == 0:
        if digit_automate()[0][i] == 0:
            h2+='!q4*'
        else:
            h2+='q4*'
        if digit_automate()[1][i] == 0:
            h2+='!q3*'
        else:
            h2+='q3*'
        if digit_automate()[2][i] == 0:
            h2+='!q2*'
        else:
            h2+='q2*'
        if digit_automate()[3][i] == 0:
            h2+='!q1*'
        else:
            h2+='q1*'
        if digit_automate()[4][i] == 0:
            h2+='!v+'
        else:
            h2+='v+'
    if digit_automate()[12][i] == 0:
        if digit_automate()[0][i] == 0:
            h1+='!q4*'
        else:
            h1+='q4*'
        if digit_automate()[1][i] == 0:
            h1+='!q3*'
        else:
            h1+='q3*'
        if digit_automate()[2][i] == 0:
            h1+='!q2*'
        else:
            h1+='q2*'
        if digit_automate()[3][i] == 0:
            h1+='!q1*'
        else:
            h1+='q1*'
        if digit_automate()[4][i] == 0:
            h1+='!v+'
        else:
            h1+='v+'
h4=h4[:-1]
h3=h3[:-1]
h2=h2[:-1]
h1=h1[:-1]

def raschetni(stroka):
    start_val = sDNF(stroka)
    stroka=sDNF(stroka)
    stroka=re.split(r'\+',stroka)
    for i in range (0,len(stroka)):
        stroka[i]=re.split(r'\*',stroka[i])
    temp_list=[]
    for i in range (0,len(stroka)):
        temp={}
        final=[]
        for s in range(0,len(stroka)):
            final.append([])
            for l in range(0,len(stroka[s])):
                final[s].append(stroka[s][l])
        for j in range (0,len(stroka[i])):
            if stroka[i][j].count('!')==0:
                temp.setdefault(stroka[i][j],'1')
                temp.setdefault('!'+stroka[i][j],'0')
            else:
                temp.setdefault(stroka[i][j][1:],'0')
                temp.setdefault(stroka[i][j],'1')
        for j in range (0,len(stroka)):
            if i==j:
                if i==len(stroka):
                    break
            for x in range (0,len(stroka[j])):
                for z in temp:
                    if z==stroka[j][x]:
                        final[j][x]=temp[z]
                        break
        for s in range(0,len(final)):
            final[s]='*'.join(final[s])
        for j in range(0,len(final)):
            if re.findall(r'^1\*1$',final[j])!=[]:
                a=re.findall(r'^1\*1$',final[j])
                b='1'
                final[j]=final[j].replace(a[0],b)
            if re.findall(r'^1\*0$',final[j])!=[]:
                a=re.findall(r'^1\*0$',final[j])
                b=''
                final[j]=final[j].replace(a[0],b)
            if re.findall(r'^0\*1$',final[j])!=[]:
                a=re.findall(r'^0\*1$',final[j])
                b=''
                final[j]=final[j].replace(a[0],b)
            if re.findall(r'^\!?[a-z]\d*\*1$',final[j])!=[]:
                a=re.findall(r'^\!?[a-z]\d*\*1$',final[j])
                b=re.findall(r'^\!?[a-z]\d*',final[j])
                final[j]=final[j].replace(a[0],b[0])
            if re.findall(r'^1\*\!?[a-z]\d*$',final[j])!=[]:
                a=re.findall(r'^1\*\!?[a-z]\d*$',final[j])
                b=re.findall(r'\!?[a-z]\d*$',final[j])
                final[j]=final[j].replace(a[0],b[0])
            if re.findall(r'^\!?[a-z]\d*\*0$',final[j])!=[]:
                a=re.findall(r'^\!?[a-z]\d*\*0$',final[j])
                b=""
                final[j]=final[j].replace(a[0],b)
            if re.findall(r'^0\*\!?[a-z]\d*$',final[j])!=[]:
                a=re.findall(r'^0\*\!?[a-z]\d*$',final[j])
                b=""
                final[j]=final[j].replace(a[0],b)
        temp_list.append(final)
    last=[]
    for i in range(0,len(temp_list)):
        temp=""
        for j in range (0, len(temp_list[i])):
            if temp_list[i][j]!='':
               temp+=temp_list[i][j]+'+'
        temp=temp[:-1]
        last.append(temp)
    for i in range (0,len(last)):
        a = re.findall(r'\!?[a-z]\d*',last[i])
        if len(a) > 1:
            last[i] = last[i].replace(a[1],'1')
            last[i] = last[i].replace(a[0],'')
            if re.findall(r'^\+',last[i]) != []:
                last[i]=last[i][1:]
            if re.findall(r'\+$',last[i]) != []:
                last[i]=last[i][:-1]
    final=""
    for i in range (0,len(last)):
        if re.findall(r'\!?[a-z]\d*',last[i]) != []:
            final+='*'.join(stroka[i])+'+'
    if final!="":
        return final[:-1]
    else:
        return start_val

def sDNF(stroka):
    podstr=re.split(r'\+',stroka)
    for i in range (0,len(podstr)):
        podstr[i]=re.split(r'\*',podstr[i])
    final=[]
    siz=len(podstr)
    for i in range(int(math.log(siz,2))):#переменная величина
        for i in range(0,len(podstr)):
            for j in range (0,len(podstr)):
                if i<j:
                    counter=0
                    temp=[]
                    for x in range(0,len(podstr[i])):
                        if podstr[i][x] == podstr[j][x]:
                            counter+=1
                            temp.append(podstr[i][x])
                    if counter == len(podstr[i])-1:
                        test=True
                        for y in final:
                            if temp==y:
                                test=False
                        if test ==True:
                            final.append(temp)
        podstr=final
        final=[]
    for i in range(0,len(podstr)):
        podstr[i]='*'.join(podstr[i])
    podstr='+'.join(podstr)
    return podstr

print("Вывод таблицы истинности и возбуждения")
for i in digit_automate():
    print(i)
print("Вывод сднф для всех 4 сигналов возбуждения")
print(h4)
print(h3)
print(h2)
print(h1)
print("Вывод минимизированных сднф для всех 4 сигналов возбуждения")
print(raschetni(h4))
print(raschetni(h3))
print(raschetni(h2))
print(raschetni(h1))
