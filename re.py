import re

pattern = re.compile(r"((=\w\w)+[=])" )

f = open('data.txt')
g = open('re.txt', 'w')

# result = re.findall(pattern, f)

for line in f:
    result = re.findall(pattern, line)
    result = (bytes(result).decode('cp1251'))

    # print(result)
    g.write(result + '\n')

g.close
f.close
