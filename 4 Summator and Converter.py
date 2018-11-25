
import re

#одноразрядный двоичный сумматор на 3 входа (ОДС-3) с представлением выходных функций в СКНФ

def summator():
    tabl = [[0,0,0],[0,0,1],[0,1,0],[1,0,0],[0,1,1],[1,0,1],[1,1,0],[1,1,1]]
    for i in range (0,8):
        rez = tabl[i][0] + tabl[i][1] + tabl[i][2]
        if rez == 3:
            perenos = 1
            rez -= 2
        elif rez == 2:
            perenos = 1
            rez -= 2
        elif rez == 1:
            perenos = 0
        elif rez == 0:
            perenos = 0
        tabl[i].append(rez)
        tabl[i].append(perenos)
    return tabl

def tablichni_3(stroka):
    tabl=[]
    string = stroka
    final=""
    for i in range(2):
        tabl.append([])
        for j in range(4):
            tabl[i].append('0')
    string = re.split(r'\)\*\(',string[1:-1])
    for i in string:
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
    final = final[:-1]
    if tabl[0].count('1') == 0 and tabl[1].count('1') == 0:
        return final
    for i in range(0,2):
        for j in range (0,4):
            if tabl[i][j] == '1':
                final +='*('
                counter = 0
                if i == 0:
                    final += 'x1+'
                    counter += 1
                if j == 1:
                    final += 'x3+'
                    counter += 1
                if j == 3:
                    final += 'x2+'
                    counter += 1
                final = final[:-1]
                final += ')'
                if counter <=1:
                    final = stroka
                tabl[i][j] = '0'
    return final

print("[x1,x2,x3,rez,perenos]")
for i in range(0,8):
        print([str(i+1)+')'] + summator()[i])

SKNF_rez = ""
SKNF_perenos = ""
for i in range(0,8):
    if summator()[i][3] == 1:
        SKNF_rez += '('
        if summator()[i][0] == 1:
            SKNF_rez += 'x1+'
        else:
            SKNF_rez += '!x1+'
        if summator()[i][1] == 1:
            SKNF_rez += 'x2+'
        else:
            SKNF_rez += '!x2+'
        if summator()[i][2] == 1:
            SKNF_rez += 'x3'
        else:
            SKNF_rez += '!x3'
        SKNF_rez += ')*'
        
    if summator()[i][4] == 1:
        SKNF_perenos += '('
        if summator()[i][0] == 1:
            SKNF_perenos += 'x1+'
        else:
            SKNF_perenos += '!x1+'
        if summator()[i][1] == 1:
            SKNF_perenos += 'x2+'
        else:
            SKNF_perenos += '!x2+'
        if summator()[i][2] == 1:
            SKNF_perenos += 'x3'
        else:
            SKNF_perenos += '!x3'
        SKNF_perenos += ')*'
SKNF_rez = SKNF_rez[:-1]
SKNF_perenos = SKNF_perenos[:-1]
print("СКНФ для выходных функций сумматора:")
print(SKNF_rez)
print(SKNF_perenos)
print("Минимализированные СКНФ для выходных функций:")
print(tablichni_3(SKNF_rez))
print(tablichni_3(SKNF_perenos))
print('---------------------------')

def preobrazovatel():
    tabl = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
    for i in range(0,16):
        if len(suma([0,1,0,1],tabl[i])) == 4:
            tabl[i] += suma([0,1,0,1],tabl[i])
        else:
            tabl[i] += ['-','-','-','-']
    return tabl

def suma(spis1,spis2):
    if len(spis1) == len(spis2):
        dop = 0
        final = []
        for i in range(len(spis1)-1,-1,-1):
            temp = spis1[i] + spis2[i] + dop
            if temp == 3:
                dop = 1
                final.append(1)
            elif temp == 2:
                dop = 1
                final.append(0)
            elif temp == 1:
                dop = 0
                final.append(1)
            elif temp == 0:
                dop = 0
                final.append(0)
        if dop != 0:
            final.append(dop)
        final.reverse()
        return final

print("[x4,x3,x2,x1,y4,y3,y2,y1]")
for i in range(0,16):
        print([str(i+1)+')'] + preobrazovatel()[i])
        
SKNF_y4 = ""
SKNF_y3 = ""
SKNF_y2 = ""
SKNF_y1 = ""
for i in range(0,12):
    if preobrazovatel()[i][4] == 1:
        SKNF_y4 += '('
        if preobrazovatel()[i][0] == 1:
            SKNF_y4 += 'x4+'
        else:
            SKNF_y4 += '!x4+'
        if preobrazovatel()[i][1] == 1:
            SKNF_y4 += 'x3+'
        else:
            SKNF_y4 += '!x3+'
        if preobrazovatel()[i][2] == 1:
            SKNF_y4 += 'x2+'
        else:
            SKNF_y4 += '!x2+'
        if preobrazovatel()[i][3] == 1:
            SKNF_y4 += 'x1'
        else:
            SKNF_y4 += '!x1'
        SKNF_y4 += ')*'
        
    if preobrazovatel()[i][5] == 1:
        SKNF_y3 += '('
        if preobrazovatel()[i][0] == 1:
            SKNF_y3 += 'x4+'
        else:
            SKNF_y3 += '!x4+'
        if preobrazovatel()[i][1] == 1:
            SKNF_y3 += 'x3+'
        else:
            SKNF_y3 += '!x3+'
        if preobrazovatel()[i][2] == 1:
            SKNF_y3 += 'x2+'
        else:
            SKNF_y3 += '!x2+'
        if preobrazovatel()[i][3] == 1:
            SKNF_y3 += 'x1'
        else:
            SKNF_y3 += '!x1'
        SKNF_y3 += ')*'

    if preobrazovatel()[i][6] == 1:
        SKNF_y2 += '('
        if preobrazovatel()[i][0] == 1:
            SKNF_y2 += 'x4+'
        else:
            SKNF_y2 += '!x4+'
        if preobrazovatel()[i][1] == 1:
            SKNF_y2 += 'x3+'
        else:
            SKNF_y2 += '!x3+'
        if preobrazovatel()[i][2] == 1:
            SKNF_y2 += 'x2+'
        else:
            SKNF_y2 += '!x2+'
        if preobrazovatel()[i][3] == 1:
            SKNF_y2 += 'x1'
        else:
            SKNF_y2 += '!x1'
        SKNF_y2 += ')*'
        
    if preobrazovatel()[i][7] == 1:
        SKNF_y1 += '('
        if preobrazovatel()[i][0] == 1:
            SKNF_y1 += 'x4+'
        else:
            SKNF_y1 += '!x4+'
        if preobrazovatel()[i][1] == 1:
            SKNF_y1 += 'x3+'
        else:
            SKNF_y1 += '!x3+'
        if preobrazovatel()[i][2] == 1:
            SKNF_y1 += 'x2+'
        else:
            SKNF_y1 += '!x2+'
        if preobrazovatel()[i][3] == 1:
            SKNF_y1 += 'x1'
        else:
            SKNF_y1 += '!x1'
        SKNF_y1 += ')*'

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
    start_val = sKNF(stroka)
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
    if final != "":
        return final[:-1]
    else:
        return start_val
    
SKNF_y3 = SKNF_y3[:-1]
SKNF_y4 = SKNF_y4[:-1]
SKNF_y2 = SKNF_y2[:-1]
SKNF_y1 = SKNF_y1[:-1]
print("СКНФ для всех 4 функций:")
print(SKNF_y4)
print(SKNF_y3)
print(SKNF_y2)
print(SKNF_y1)
print("Минимализированные СКНФ для всех функций:")
print(raschetni(SKNF_y4))
print(raschetni(SKNF_y3))
print(raschetni(SKNF_y2))
print(raschetni(SKNF_y1))
