import re

pattern = re.compile(r'хлеб морковка мороженное')

# f = open('data.html', 'r', 'utf-8')
f = open('data.html', 'r')

for line in f:
    d = re.findall(pattern, line, flags = re.IGNORECASE)
    print(str(d))
