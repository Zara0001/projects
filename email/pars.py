import re

pattern = re.compile(r'<!-- Items -->')

# with open('data.html', 'r') as f:

f = open('data.html')
g = open('data_pars.html', 'w')

for line in f:
    peremennaua = re.findall(pattern, line)
    if peremennaua:
        print(peremennaua)
        print(line)
    # print(peremennaua)
    g.write(str(peremennaua))

f.close
g.close
