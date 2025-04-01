def media_lista(lista):
    soma = 0
    for i in lista:
      soma += i
    return soma/len(lista)

print(media_lista({1, 2, 8, 9}))
