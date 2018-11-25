
import re

def otric(stok):
    counter=0
    final=""
    i=0
    kolvo_oper=0
    for k in stok:
        if (k=='('):
            counter+=1
        if (k==')'):
            counter-=1
        if ((k=='+')|(k=='*'))&(counter==0):
            kolvo_oper+=1
    while True:
        if (stok[i]=='('):
            counter+=1
        if (stok[i]==')'):
            counter-=1
        if (counter==0)&((stok[i]=='+')|(stok[i]=='*')):
            kolvo_oper-=1
            final+="!"
            for j in range(0,i):
                final+=stok[j]
            if (stok[i]=='+'):
                final+='*'
            else:
                final+='+'
            finish=""
            for j in range(i+1,len(stok)):
                finish+=stok[j]
            if (kolvo_oper>0):
                final+=otric(finish)
            else:
                final+="!"+finish
            break
        i+=1
        if (i==len(stok)):
            break
    finish=final
    for s in range(0,len(final)-1):
        if (final[s]=='!')&(final[s+1]=='!'):
            finish=final[0:s]+final[s+2:]
    if (finish[0]=='('):
        counter-=1
        finish=finish[1:]
    for m in range (1,len(finish)-1):
        if (finish[m]=='('):
            counter+=1
        if (finish[m]==')'):
            counter-=1        
        if (finish[m]=='(')&(finish[m-1]!='!')&(counter==1):
            counter-=2
            finish=finish[0:m]+finish[m+1:]
            m-=1
        if (finish[m]==')')&(counter==-2):
            counter+=2
            finish=finish[0:m]+finish[m+1:]
            m-=1
    return finish

def dnf(stroka):
    counter=0
    max_count=0
    kolvo_oper=0
    for k in stroka:
        if (k=='('):
            counter+=1
            if counter>max_count:
                max_count=counter
        if (k==')'):
            counter-=1
        if ((k=='+')|(k=='*'))&(counter==0):
            kolvo_oper+=1
    if max_count==0:
        return stroka
    if (kolvo_oper==0)&(stroka[0]=='!'):
        stroka=stroka[2:-1]
        final=otric(stroka)
    if kolvo_oper>0:
        final=""
        i=0
        while i<len(stroka)-1:
            if stroka[i]=='(':
                counter+=1
            if stroka[i]==')':
                counter-=1
            if (counter==0)&(stroka[i]=='!')&(stroka[i+1]=='('):
                part=""
                i=i+2
                counter+=1
                while (counter!=0):
                    if (stroka[i]=='('):
                        counter+=1
                    if (stroka[i]==')'):
                        counter-=1
                    part+=stroka[i]
                    i+=1
                i-=1
                part=part[0:-1]
                final+=otric(part)
            else:
                final+=stroka[i]
            i+=1
        final+=stroka[i]
    return dnf(final)
    
def sdnf(stroka):
    stroka=dnf(stroka)
    vse=[]
    for i in re.findall(r'\w\d+',stroka):
        if i not in vse:
            vse.append(i)
    podstr=re.split('\+',stroka)
    for i in range(0,len(podstr)):
        for j in vse:
            if j not in podstr[i]:
                podstr.append(podstr[i]+'*!'+j)
                podstr[i]+="*"+j
    return'+'.join(podstr)

def knf(stroka):
    stroka=dnf(stroka)
    mnog=[[]]
    podstr=re.split(r'\+',stroka)
    for t in range (0,len(podstr)):
        mnog.append([])
        for i in re.findall(r'\!?\w\d+',podstr[t]):
                mnog[t].append(i)
    del mnog[len(mnog)-1]
    podstr[:]=[]
    proverka=True
    for t in range (0,len(mnog)-1,2):
        for i in mnog[t]:
            for j in mnog[t+1]:
                i=i[::-1]
                i+='!'
                i=i[::-1]
                if i==j:
                    proverka=False
                i=i[1:]
                j=j[::-1]
                j+='!'
                j=j[::-1]
                if j==i:
                    proverka=False
                j=j[1:]
                if proverka==True:
                    temp='('+i+'+'+j+')'
                    podstr.append(temp)
    return '*'.join(podstr)
                
def sknf(stroka):
    stroka=knf(stroka)
    vse=[]
    for i in re.findall(r'\w\d+',stroka):
        if i not in vse:
            vse.append(i)
    podstr=re.split('\*',stroka)
    dlin=len(podstr)
    for i in range(0,dlin):
        for j in vse:
            if j not in podstr[i]:
                podstr[i]=podstr[i][0:-1]
                podstr.append(podstr[i]+'+!'+j+')')
                podstr[i]+='+'+j+')'
    vse[:]=[]
    tabl=[]
    for t in range (0,len(podstr)):
        vse.append(re.findall(r'\!?\w\d+',podstr[t]))
        vse[t].sort()
        tabl.append(True)
    
    for m in range (0,len(vse)):
        for n in range (0,len(vse)):
            if (vse[m]==vse[n])&(m!=n)&(tabl[m]!=False)&(tabl[n]!=False):
                tabl[n]=False
    i=0
    for f in range(0,len(tabl)):
        if tabl[f]==False:
            del podstr[f-i]
            i+=1
    return '*'.join(podstr)

def tabl_ist(stroka):
    tabl=[[]]
    vse=[]
    strin=""
    for i in re.findall(r'\w\d+',stroka):
        if i not in vse:
            vse.append(i)
            strin+='0'
    vse.sort()
    tabl[0]+=vse+['f1']+['f2']+['']
    tabl.append([])
    for j in strin:
        tabl[1].append(j)
    for i in range (2,pow(2,len(vse))+1):
        strin=plus1(strin)
        tabl.append([])
        for j in strin:
            tabl[i].append(j)
    for w in range(1,len(tabl)):
        podstr=re.split(r'\+',sdnf(stroka))
        for t in range (0,len(podstr)):
            for j in re.findall(r'\w\d+',podstr[t]):
                for i in range(0,len(tabl[0])):
                    if j==tabl[0][i]:
                        podstr[t]=podstr[t].replace(j,tabl[w][i])
            podstr[t]=podstr[t].replace('!0','1')
            podstr[t]=podstr[t].replace('!1','0')
            if podstr[t].count('0')!=0:
                podstr[t]='0'
            else:
                podstr[t]='1'
        podstr='+'.join(podstr)
        if podstr.count('1')!=0:
            podstr='1'
        else:
            podstr='0'
        tabl[w].append(podstr)
    for w in range(1,len(tabl)):
        podstr=re.split(r'\*',sknf(stroka))
        for t in range (0,len(podstr)):
            for j in re.findall(r'\w\d+',podstr[t]):
                for i in range(0,len(tabl[0])):
                    if j==tabl[0][i]:
                        podstr[t]=podstr[t].replace(j,tabl[w][i])
            podstr[t]=podstr[t].replace('!0','1')
            podstr[t]=podstr[t].replace('!1','0')
            if podstr[t].count('1')!=0:
                podstr[t]='1'
            else:
                podstr[t]='0'
        podstr='*'.join(podstr)
        if podstr.count('0')!=0:
            podstr='0'
        else:
            podstr='1'
        tabl[w].append(podstr)
    return tabl
    
def plus1(stroka):
    stroka=stroka[::-1]
    ost=1
    final=""
    for j in range (0,len(stroka)):
            temp=int(stroka[j])+ost
            if temp==0:
                final+='0'
                ost=0
            if temp==1:
                final+='1'
                ost=0
            if temp==2:
                final+='0'
                ost=1
    return final[::-1]

def ch_form(stroka):
    tabl=tabl_ist(stroka)
    fina1="V("
    fina2="^("
    for i in range (1,len(tabl)):
        if tabl[i][tabl[0].index('f1')]=='1':
            fina1+=str(i-1)
        else:
            fina2+=str(i-1)
    fina1+=')'
    fina2+=')'
    return fina1,fina2
                        
            
print("Начальный вид ","!((x1+x3)*!(!x2*x3))")
print("Дизъюнктивная нормальная форма ",dnf("!((x1+x3)*!(!x2*x3))"))
print("Совершенная дизъюнктивная нормальная форма ",sdnf("!((x1+x3)*!(!x2*x3))"))
print("Конъюнктивная нормальная форма ",knf("!((x1+x3)*!(!x2*x3))"))
print("Совершенная конъюнктивная нормальная форма ",sknf("!((x1+x3)*!(!x2*x3))"))
for i in range(0,len(tabl_ist("!((x1+x3)*!(!x2*x3))"))):
    print(tabl_ist("!((x1+x3)*!(!x2*x3))")[i])
print(ch_form("!((x1+x3)*!(!x2*x3))")[0]+"    "+ch_form("!((x1+x3)*!(!x2*x3))")[1])
