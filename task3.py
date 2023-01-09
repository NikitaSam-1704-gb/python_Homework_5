#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def RLE_algoritm(data):
    ecoding=''
    priv_char=''
    count=1
    if not data: return ''
    for char in data:
        if char != priv_char:
            if priv_char:
                ecoding+=str(count)+priv_char+' ' 
            count=1
            priv_char=char
        else:
            count+=1
    else:
        ecoding+=str(count)+priv_char+' ' 
        return ecoding

stroka=str(input('Введите набор букв-> '))
stroka_rle=RLE_algoritm(stroka)
print(stroka_rle)
  