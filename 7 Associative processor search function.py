import re
import random
# ассоциативная память совершает поиск слова, если найдено, то возвращает список адресов хранения

def key_word(word = "", mas = {}, values = [], razryad = 0, stroka = ""):
    if word == "":  return [mas,values]
    stroka += str(random.randint(0,1))
    razryad += 1
    if razryad == 8:
        mas.setdefault(stroka, word)
        values.append(stroka)
        return [mas, values]
    else:   return key_word(word, mas, values, razryad, stroka)


def search_for_ecvivalense(pattern = "--------", search_arg = [], razryad = 0):
    if len(pattern) != 8:   raise("length of the pattern should be 8 symbols")
    i = 0
    while i != len(search_arg):
        if pattern[razryad] != '-':
            if search_arg[i][razryad] != pattern[razryad]:
                search_arg.pop(i)
            else:
                i += 1
        else:
            i +=1
    razryad += 1
    if razryad == 8 or len(search_arg) == 0: return search_arg
    else: return search_for_ecvivalense(pattern, search_arg, razryad)
            

def search_closer_value(pattern = "--------", search_arg = [], above = False, razryad = 0):
    if len(pattern) != 8:   raise("length of the pattern should be 8 symbols")
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
    elif razryad == 8:
        if not above:
            return max([int(i) for i in search_arg])
        else:
            return min([int(i) for i in search_arg])
    else:   return search_closer_value(pattern, search_arg, above, razryad)


key_word("bus")
key_word("boy")
key_word("class")
key_word("desk")
conteiner = key_word("house")[0]
print(conteiner)
print("Поисе по соответствию для шаблона '-1----1-' ", search_for_ecvivalense("-1----1-", key_word()[1], 0))
print("Поиск ближайшего снизу значения для шаблона '01------' ", search_closer_value("01------", key_word()[1], False, 0))
print("Поиск ближайшего сверху значения для шаблона '-0--1---' ", search_closer_value("-0--1---", key_word()[1], True, 0))
