import re

pattern = re.compile(r'=\w\w+f' )

f = open('data.txt')

# result = re.findall(pattern, f)

for line in f:
    result = re.findall(pattern, line)
    result = (bytes(result).decode('cp1251'))

    print(result)

f.close
