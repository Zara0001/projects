import re

pattern = re.compile(r'\w+')

# with open('data.html', 'r') as f:

f = open('data.html', 'rt', encoding='UTF-8')
g = open('data_pars.html', 'w')

for line in f:
    peremennaua = re.findall(pattern, line)
    print(f.read())
    g.write(str(peremennaua))

f.close
g.close
