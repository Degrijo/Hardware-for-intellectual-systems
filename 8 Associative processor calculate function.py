
import random

def create_massive(m):
    mas = [[0 for j in range (m)]for i in range (m)]
    return mas

def key_word(word = "", mas = {}, values = [], razryad = 0, stroka = ""):
    if word == "":  return [mas,values]
    stroka += str(random.randint(0,1))
    razryad += 1
    if razryad == 16:
        mas.setdefault(stroka, word)
        values.append(stroka)
        return [mas, values]
    else:   return key_word(word, mas, values, razryad, stroka)

def fill_massive(massive, keys):
    if len(keys) > len(massive): raise("Too many keys for memory massive")
    for i in range(len(keys)):
        if len(keys[i]) != len(massive): raise("Keys should have fixed length")
        for j in range (len(keys[i])):
            if j < len(massive) - i:
                massive[i + j][j] = int(keys[i][j])
            else:
                massive[j-len(massive)+i][j] = int(keys[i][j])
    return massive

def search_closer_value(pattern = "----------------", search_arg = [], above = False, razryad = 0):
    if len(pattern) != 16:   raise("length of the pattern should be 16 symbols")
    i = 0
    while i != len(search_arg):
        if pattern[razryad] != '-':
            if not above and int(search_arg[i][razryad]) > int(pattern[razryad]) or above and int(search_arg[i][razryad]) < int(pattern[razryad]):
                search_arg.pop(i)
            else:
                i += 1
        else:
            i +=1
    razryad +=1
    if len(search_arg) == 0:
        return search_arg
    elif razryad == 16:
        if not above:
            return max([int(i) for i in search_arg])
        else:
            return min([int(i) for i in search_arg])
    else:   return search_closer_value(pattern, search_arg, above, razryad)

def read(mas, num):
    temp = []
    for j in range(len(mas)):
        if j < len(mas) - num:
            temp += [mas[num + j][j]]
        else:
            temp += [mas[j-len(mas) + num][j]]
    return temp

def write(mas, num, key):
    for j in range (len(key)):
        if j < len(mas) - num:
            mas[num + j][j] = int(key[j])
        else:
            mas[j-len(mas)+num][j] = int(key[j])

def conjunction(mas, m, n):
    temp = read(mas, m)
    for j in range(len(mas)):
        if j < len(mas) - n:
            temp[j] &= mas[n + j][j]
        else:
            temp[j] &= mas[j-len(mas) + n][j]
    temp = [str(i) for i in temp]
    return ''.join(temp)

def Shevver(mas, m, n):
    temp = conjunction(mas, m, n)
    for i in range(len(temp)):
        if temp[i] == '0':    temp = temp[0:i] + '1' + temp[i+1:]
        else:   temp = temp[0:i] + '0' + temp[i+1:]
    return temp
    
def repeating(mas, m):
    temp = read(mas, m)
    temp = [str(i) for i in temp]
    temp = ''.join(temp)
    return temp

def inversion(mas, m):
    temp = read(mas, m)
    temp = [str(i) for i in temp]
    temp = ''.join(temp)
    for i in range(len(temp)):
        if temp[i] == '0':    temp = temp[0:i] + '1' + temp[i+1:]
        else:   temp = temp[0:i] + '0' + temp[i+1:]
    return temp

def summa(mas, m, n):
    temp = read(mas, m)
    per = 0
    final = ""
    for i in range (len(temp)):
        val = temp[i] + read(mas, n)[i] + per
        if val == 0:
            per = 0
            final += '0'
        elif val == 1:
            per = 0
            final += '1'
        elif val == 2:
            per = 1
            final += '0'
        elif val == 3:
            per = 1
            final += '1'
    final = [str(i) for i in final]
    final = ''.join(final)
    return final
    

memory_massive = create_massive(16)
key_word("bus")
key_word("boy")
key_word("class")
key_word("desk")
conteiner = key_word("house")[0]
print(conteiner)
memory_massive = fill_massive(memory_massive, key_word()[1])
for raw in memory_massive:
    print(raw)
print("Поиск ближайшего снизу значения для шаблона '01--------------' ", search_closer_value("01--------------", key_word()[1], False, 0))
print("Конъюнкция 0 и 1 слов, которая записывается в 5 ячейку ", conjunction(memory_massive, 0, 1))
write(memory_massive, 5, conjunction(memory_massive, 0, 1))
for raw in memory_massive:
    print(raw)
print("операция Шиффера над 3 и 4 словами, которая записывается в 6 ячейку ", Shevver(memory_massive, 3, 4))
write(memory_massive, 6, Shevver(memory_massive, 3, 4))
for raw in memory_massive:
    print(raw)
print("Повторение первого элемента 2 слова, которое записывается в 7 ячейку ", repeating(memory_massive, 2))
write(memory_massive, 7, repeating(memory_massive, 2))
for raw in memory_massive:
    print(raw)
print("Отрицание первого элемента 5 слова, которое записывается в 8 ячейку ", inversion(memory_massive, 5))
write(memory_massive, 8, inversion(memory_massive, 5))
for raw in memory_massive:
    print(raw)
print("Сумма 3 и 6 элементов, которая записывается в 9 ячейку", summa(memory_massive, 3, 6))
write(memory_massive, 9, summa(memory_massive, 3, 6))
for raw in memory_massive:
    print(raw)
