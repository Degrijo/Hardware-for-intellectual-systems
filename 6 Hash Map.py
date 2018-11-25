
import re

class Hash_table:
    _N = 16
    _tabl = [[] for _ in range(_N)]
    def __init__(self,key,value):
        if len(key) == len(value):
            for i in range(0,len(key)):
                self.adding_square(key[i],value[i])
        else:
            raise("Sets 'serials_of_weap' and 'countries' are not ecvivalent")
    def _hash_funct(self,key):
        number = 0
        poz={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,' ':0,'-':1}
        for i in key:
            if re.findall(r'\d',i)!=[]:
                number += int(re.findall(r'\d',i)[0])
            elif re.findall(r'[a-z]',i.lower())!=[]:
                number += poz[i.lower()]
        number=number%self._N
        return number
    def get_square(self,key):
        for i in self._tabl[self._hash_funct(key)]:
            if i.get_key() == key:
                return i.get_value()
    def adding_square(self,key,value = None): #добавляет элемент, если ключа не существует, в противном случае возвращает значение по существующему ключу
        class square:
            def __init__(self,key,value):
                self.key = key
                self.value = value
            def get_inf(self):
                return self.key + " : " + self.value
            def get_value(self):
                return value
            def get_key(self):
                return key
        test=True
        for i in self._tabl[self._hash_funct(key)]:
            if i.get_key() == key:
                test=False
        if test == True:
            self._tabl[self._hash_funct(key)].append(square(key,value))
        else:
            return self.get_square(key)
    def get_tabl(self):
        final="{ "
        for i in range(0,self._N):
            if self._tabl[i]!=[]:
                for j in self._tabl[i]:
                    final+=j.get_inf() + "; "
        final=final[:-2]+" }"
        return final
    def del_square(self,key):
        for i in range(0,len(self._tabl[self._hash_funct(key)])):
            if self._tabl[self._hash_funct(key)][i].get_key() == key:
                 self._tabl[self._hash_funct(key)].pop(i)

serials_of_weap=["AK-74M", "M16 A4", "HK G36", "Steyr AUG A3", "Beretta ARX-160"]
countries=["в Азербайджане, Белоруси, Болгарии, Грузии, Иордании, Казахстане, Молдавии, Туркменистане", "в Боливии, Великобритании, Индонезии, Латвии, Японии", "в Австралии, Бразилии, Великобритании, Индонезии, Исландии, Испании, Мексике, Португалии", "в Австрии, Новой Зеландии, Ирландии , Саудовской Аравии, Тунисе, Омане, Марокко, Боливии , Эквадоре", "в Албании, Египте, Италии , Казахстане, Мексике, Туркменистане"]
weapon = Hash_table(serials_of_weap,countries)
print("Вывод всей таблицы")
print(weapon.get_tabl())
print("Поиск по ключу")
print("M16 A4 ",weapon.get_square("M16 A4"))
print("Удаление элемента по ключу")
weapon.del_square("HK G36")
print(weapon.get_tabl())
