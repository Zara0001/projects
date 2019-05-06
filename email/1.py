import lxml as html
from lxml.html import parse
from pandas import DataFrame

with open("data.html", 'r') as f:
    page = f.read()

a = parse(page)
e = a.getroot().\
    find_class('x_w95 x_font12').\
    pop()
