
import re

def raschetni(stroka):
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
    print(last)
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
    return final[:-1]

def tablichni(stroka):
    tabl=[]
    final=""
    for i in range(2):
        tabl.append([])
        for j in range(4):
            tabl[i].append('0')
    stroka = re.split(r'\+',stroka)
    for i in stroka:
        if re.findall(r'^\!',i)!=[]:
            m=1
        else:
            m=0
        if re.findall(r'\*\!\w+\*',i)!=[]:
            if re.findall(r'\*\!\w+$',i)!=[]:
                n=0
            else:
                n=1
        else:
            if re.findall(r'\*\!\w+$',i)!=[]:
                n=3
            else:
                n=2
        tabl[m][n]='1'
    for i in range (4):
        if tabl[0][i] == '1' and tabl[1][i] == '1':
            if i == 0:
                final+="!x2*!x3"
            elif i == 1:
                final+="!x2*x3"
            elif i == 2:
                final+="x2*x3"
            else:
                final+="x2*!x3"
            tabl[0][i] = '0'
            tabl[1][i] = '0'
            final+='+'
    for j in range (2):
        if tabl[j][0] == '1' and tabl[j][1] == '1':
            if j == 0:
                final+='x1'
            else:
                final+='!x1'
            final+="*!x2+"
            tabl[j][0] = '0'
            tabl[j][1] = '0'
        if tabl[j][0] == '1' and tabl[j][3] == '1':
            if j == 0:
                final+='x1'
            else:
                final+='!x1'
            final+="*!x3+"
            tabl[j][0] = '0'
            tabl[j][3] = '0'
        if tabl[j][1] == '1' and tabl[j][2] == '1':
            if j == 0:
                final+='x1'
            else:
                final+='!x1'
            final+="*x3+"
            tabl[j][1] = '0'
            tabl[j][2] = '0'
        if tabl[j][2] == '1' and tabl[j][3] == '1':
            if j == 0:
                final+='x1'
            else:
                final+='!x1'
            final+="*x2+"
            tabl[j][2] = '0'
            tabl[j][3] = '0'
    return final[:-1]

def sDNF(stroka):
    podstr=re.split(r'\+',stroka)
    for i in range (0,len(podstr)):
        podstr[i]=re.split(r'\*',podstr[i])
    final=[]
    for i in range(0,len(podstr)):
        for j in range (0,len(podstr)):
            if (i!=j)&(i<j):
                counter=0
                temp=[]
                for x in range(0,len(podstr[i])):
                    if podstr[i][x] == podstr[j][x]:
                        counter+=1
                        temp.append(podstr[i][x])
                if counter == len(podstr[i])-1:
                    final.append(temp)
    for i in range(0,len(final)):
        final[i]='*'.join(final[i])
    final='+'.join(final)
    return final

def raschetno_tabl(stroka):
    podstr=sDNF(stroka)
    podstr=re.split(r'\+',podstr)
    stroka=re.split(r'\+',stroka)
    for i in range (0,len(podstr)):
        podstr[i]=re.split(r'\*',podstr[i])
    tabl=[]
    for m in range (0,len(podstr)):
        tabl.append([])
        for n in range (0,len(stroka)):
            proverk=True
            for i in podstr[m]:
                if (re.findall(r'^'+i,stroka[n])==[])&(re.findall(r'\*'+i,stroka[n])==[]):
                    proverk=False
            if proverk==True:
                tabl[m].append('1')
            else:
                tabl[m].append('0')
    tabl.append([])
    for x in range(0,len(tabl[0])):
        tabl[len(tabl)-1].append('0')
    for i in range (0, len(podstr)):
        podstr[i]='*'.join(podstr[i])
    final=""
    for j in range (0,len(tabl[i])):
        temp_sum=0
        for i in range (0,len(tabl)):
            temp_sum+=int(tabl[i][j]) 
        if temp_sum == 1:
            for i in range (0,len(tabl)):
                if tabl[i][j]=='1':
                    final+=podstr[i]+'+'
                    for k in tabl[i]:
                        tabl[len(tabl)-1][j]=int(tabl[len(tabl)-1][j])+int(k)
                    break
    return final[:-1]

def sKNF(stroka):
    podstr=re.split(r'\)\*\(',stroka[1:-1])
    for i in range (0,len(podstr)):
        podstr[i]=re.split(r'\+',podstr[i])
    final=[]
    for i in range(0,len(podstr)):
        for j in range (0,len(podstr)):
            if (i!=j)&(i<j):
                counter=0
                temp=[]
                for x in range(0,len(podstr[i])):
                    if podstr[i][x] == podstr[j][x]:
                        counter+=1
                        temp.append(podstr[i][x])
                if counter == len(podstr[i])-1:
                    final.append(temp)
    for i in range(0,len(final)):
        final[i]='+'.join(final[i])
    final=')*('.join(final)
    final='('+final+')'
    return final

def raschetni(stroka):
    stroka=sKNF(stroka)
    stroka=re.split(r'\)\*\(',stroka[1:-1])
    for i in range (0,len(stroka)):
        stroka[i]=re.split(r'\+',stroka[i])
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
                temp.setdefault(stroka[i][j],'0')
                temp.setdefault('!'+stroka[i][j],'1')
            else:
                temp.setdefault(stroka[i][j][1:],'1')
                temp.setdefault(stroka[i][j],'0')
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
            final[s]='+'.join(final[s])
        for j in range(0,len(final)):
            if re.findall(r'^0\+0$',final[j])!=[]:
                a=re.findall(r'^0\+0$',final[j])
                b='0'
                final[j]=final[j].replace(a[0],b)
            if re.findall(r'^1\+0$',final[j])!=[]:
                a=re.findall(r'^1\+0$',final[j])
                b=''
                final[j]=final[j].replace(a[0],b)
            if re.findall(r'^0\+1$',final[j])!=[]:
                a=re.findall(r'^0\+1$',final[j])
                b=''
                final[j]=final[j].replace(a[0],b)#
            if re.findall(r'^\!?[a-z]\d*\+0$',final[j])!=[]:
                a=re.findall(r'^\!?[a-z]\d*\+0$',final[j])
                b=re.findall(r'^\!?[a-z]\d*',final[j])
                final[j]=final[j].replace(a[0],b[0])
            if re.findall(r'^0\+\!?[a-z]\d*$',final[j])!=[]:
                a=re.findall(r'^0\+\!?[a-z]\d*$',final[j])
                b=re.findall(r'\!?[a-z]\d*$',final[j])
                final[j]=final[j].replace(a[0],b[0])
            if re.findall(r'^\!?[a-z]\d*\+1$',final[j])!=[]:
                a=re.findall(r'^\!?[a-z]\d*\+1$',final[j])
                b=""
                final[j]=final[j].replace(a[0],b)
            if re.findall(r'^1\+\!?[a-z]\d*$',final[j])!=[]:
                a=re.findall(r'^1\+\!?[a-z]\d*$',final[j])
                b=""
                final[j]=final[j].replace(a[0],b)
        temp_list.append(final)
    last=[]
    for i in range(0,len(temp_list)):
        temp=""
        for j in range (0, len(temp_list[i])):
            if temp_list[i][j]!='':
               temp+=temp_list[i][j]+'*'
        temp=temp[:-1]
        last.append(temp)
    print(last)
    for i in range (0,len(last)):
        a = re.findall(r'\!?[a-z]\d*',last[i])
        if len(a) > 1:
            last[i] = last[i].replace(a[1],'1')
            last[i] = last[i].replace(a[0],'1')
            if re.findall(r'^\*',last[i]) != []:
                last[i]=last[i][1:]
            if re.findall(r'\*$',last[i]) != []:
                last[i]=last[i][:-1]
    final=""
    for i in range (0,len(last)):
        if re.findall(r'\!?[a-z]\d*',last[i]) != []:
            final+='(' +'+'.join(stroka[i])+')*'
    return final[:-1]

def tablichni(stroka):
    tabl=[]
    final=""
    for i in range(2):
        tabl.append([])
        for j in range(4):
            tabl[i].append('0')
    stroka = re.split(r'\)\*\(',stroka[1:-1])
    for i in stroka:
        if re.findall(r'^\!',i)!=[]:
            m=1
        else:
            m=0
        if re.findall(r'\+\!\w+\+',i)!=[]:
            if re.findall(r'\+\!\w+$',i)!=[]:
                n=0
            else:
                n=1
        else:
            if re.findall(r'\+\!\w+$',i)!=[]:
                n=3
            else:
                n=2
        tabl[m][n]='1'
    for i in range (4):
        if tabl[0][i] == '1' and tabl[1][i] == '1':
            if i == 0:
                final+="(!x2+!x3)"
            elif i == 1:
                final+="(!x2+x3)"
            elif i == 2:
                final+="(x2+x3)"
            else:
                final+="(x2+!x3)"
            tabl[0][i] = '0'
            tabl[1][i] = '0'
            final+='*'
    for j in range (2):
        if tabl[j][0] == '1' and tabl[j][1] == '1':
            if j == 0:
                final+='(x1'
            else:
                final+='(!x1'
            final+="+!x2)*"
            tabl[j][0] = '0'
            tabl[j][1] = '0'
        if tabl[j][0] == '1' and tabl[j][3] == '1':
            if j == 0:
                final+='(x1'
            else:
                final+='(!x1'
            final+="+!x3)*"
            tabl[j][0] = '0'
            tabl[j][3] = '0'
        if tabl[j][1] == '1' and tabl[j][2] == '1':
            if j == 0:
                final+='(x1'
            else:
                final+='(!x1'
            final+="+x3)*"
            tabl[j][1] = '0'
            tabl[j][2] = '0'
        if tabl[j][2] == '1' and tabl[j][3] == '1':
            if j == 0:
                final+='(x1'
            else:
                final+='(!x1'
            final+="+x2)*"
            tabl[j][2] = '0'
            tabl[j][3] = '0'
    return final[:-1]

def raschetno_tabl(stroka):
    podstr=sKNF(stroka)
    podstr=re.split(r'\)\*\(',podstr[1:-1])
    stroka=re.split(r'\)\*\(',stroka[1:-1])
    for i in range (0,len(podstr)):
        podstr[i]=re.split(r'\+',podstr[i])
    tabl=[]
    for m in range (0,len(podstr)):
        tabl.append([])
        for n in range (0,len(stroka)):
            proverk=True
            for i in podstr[m]:
                if (re.findall(r'^'+i,stroka[n])==[])&(re.findall(r'\+'+i,stroka[n])==[]):
                    proverk=False
            if proverk==True:
                tabl[m].append('1')
            else:
                tabl[m].append('0')
    tabl.append([])
    for x in range(0,len(tabl[0])):
        tabl[len(tabl)-1].append('0')
    for i in range (0, len(podstr)):
        podstr[i]='+'.join(podstr[i])
    final=""
    for j in range (0,len(tabl[i])):
        temp_sum=0
        for i in range (0,len(tabl)):
            temp_sum+=int(tabl[i][j]) 
        if temp_sum == 1:
            for i in range (0,len(tabl)):
                if tabl[i][j]=='1':
                    final+='('+podstr[i]+')*'
                    for k in tabl[i]:
                        tabl[len(tabl)-1][j]=int(tabl[len(tabl)-1][j])+int(k)
                    break
    return final[:-1]

print("СКНФ ","(!x1+!x2+x3)*(!x1+x2+x3)*(x1+!x2+!x3)*(!x1+!x2+!x3)")
print("сокращенная Конъюнктивная Нормальная Форма ",sKNF("(!x1+!x2+x3)*(!x1+x2+x3)*(x1+!x2+!x3)*(!x1+!x2+!x3)"))# мое
print("Тупиковая форма СДНФ расчетный метод ", raschetni("(!x1+!x2+x3)*(!x1+x2+x3)*(x1+!x2+!x3)*(!x1+!x2+!x3)"))
print("Тупиковая форма СДНФ расчетно-табличный метод ", raschetno_tabl("(!x1+!x2+x3)*(!x1+x2+x3)*(x1+!x2+!x3)*(!x1+!x2+!x3)"))
print("Тупиковая форма СДНФ табличный метод ", tablichni("(!x1+!x2+x3)*(!x1+x2+x3)*(x1+!x2+!x3)*(!x1+!x2+!x3)"))

print("СДНФ ","!x1*!x3*x2+!x2*x3*x1+!x1*!x3*!x2+!x2*x3*!x1")
print("сокращенная Дизъюнктивная Нормальная Форма ",sDNF("!x1*x2*!x3+x1*!x2*x3+!x1*!x2*!x3+!x1*!x2*x3"))# мое
print("Тупиковая форма СДНФ расчетный метод ", raschetni("!x1*x2*!x3+x1*!x2*x3+!x1*!x2*!x3+!x1*!x2*x3"))
print("Тупиковая форма СДНФ расчетно-табличный метод ", raschetno_tabl("!x1*x2*!x3+x1*!x2*x3+!x1*!x2*!x3+!x1*!x2*x3"))
print("Тупиковая форма СДНФ табличный метод ", tablichni("!x1*x2*!x3+x1*!x2*x3+!x1*!x2*!x3 +!x1*!x2*x3"))
