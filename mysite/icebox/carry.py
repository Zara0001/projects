import time
from icebox.models import Product
def carry(file):
    f = open(file)
    line = f.readlines()
    f.close
    str = line[0:len(line)]
    str = [line.rstrip('\n') for line in str]
    lens = int((len(line))/2)
    lens_i = lens*2
    print(lens)
    str_name = 1
    str_count = 2
    str_date = 0
    i=0
    for i in range(lens):
        Product.objects.create(name=str[str_name], count=str[str_count], date=str[str_date])
        if str_count<lens_i:
            str_name += 2
            str_count += 2
            time.sleep(1)
