from .models import Product

f = open('../email/search')
line = f.readlines()
str = line[0:len(line)]
str = [line.rstrip('\n') for line in str]

Product.objects.create(name=str[1], count=str[2], date=str[0])
# Сделать цикл для name and count и как-то обработать дату из DD.MM.YYYY HH:MM в YYYY.MM.DD HH:MM:SS
