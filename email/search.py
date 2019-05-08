import re

file = '09_05_2019_06_07_27116066400616889666.html'

pattern_start_1 = re.compile('<td>1</td>')
pattern_start_2 = re.compile('<td>2</td>')
# pattern_eat = re.compile('молоко? хлеб? мороженое батон?')
pattern_eat = re.compile('[а-я]+')
pattern_count = re.compile(r'\d{,4}\.\d{,4}')
pattern_finish = re.compile('<!--  total -->')

# f = open('data.html', 'r', 'utf-8')
f = open(file, 'r')

num_line = 0

for line in f:

    num_line += 1
    overlap_one = re.findall(pattern_start_1, line)

    if overlap_one :
        # print(str(overlap_one))
        # print(num_line)
        # print(f.tell)

        i = num_line-1
        line_eat_int = i+1
        line_eat = [line_eat_int]
        line_count_int = i+3
        line_count = [line_count_int]

        # lines2print = [line_eat_int, line_count_int]
        # with open(file) as fp:
        #     for ei,x in enumerate(fp):
        #         if ei in lines2print:
        #             print(x.strip())
        #             # print(re.match(pattern_finish, ))
        #             print(ei)
        #             print('')

        if overlap_one:
            with open(file) as f:
                for line, line_content in enumerate(f):

                    if line in line_eat:
                        print(line_content)
                        eat = re.findall(pattern_eat, line_content)
                        print(str(eat))
                        print('')

                    if line in line_count:
                        print(line_content)
                        count = re.findall(pattern_count, line_content)
                        print(count)
                        print('')

                    if 

        if
