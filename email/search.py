import re

file = '09_05_2019_06_07_27116066400616889666.html'

pattern_start_1 = re.compile('<td>1</td>')
pattern_start_2 = re.compile('<td>2</td>')
pattern_start_3 = re.compile('<td>3</td>')
pattern_start_4 = re.compile('<td>4</td>')
pattern_start_5 = re.compile('<td>5</td>')
pattern_start_6 = re.compile('<td>6</td>')
pattern_start_7 = re.compile('<td>7</td>')

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


        # lines2print = [line_eat_int, line_count_int]
        # with open(file) as fp:
        #     for ei,x in enumerate(fp):
        #         if ei in lines2print:
        #             print(x.strip())
        #             # print(re.match(pattern_finish, ))
        #             print(ei)
        #             print('')

        if overlap_one:
            with open(file) as f_1:
                for line, line_content in enumerate(f_1):

                    i = num_line-1
                    line_eat_int = i+1
                    line_eat = [line_eat_int]
                    line_count_int = i+3
                    line_count = [line_count_int]
                    line_two_int = i+18
                    line_two = [line_two_int]

                    if line in line_eat:
                        # print(line)
                        # print(line_content)
                        eat = re.findall(pattern_eat, line_content)
                        print(str(eat))
                        print('')

                    if line in line_count:
                        # print(line)
                        # print(line_content)
                        count = re.findall(pattern_count, line_content)
                        print(count)
                        print('')

                    if line in line_two:
                        a = re.findall(pattern_start_2, line_content)
                        if a:
                            i_2 = line_two_int
                            line_eat_int_2 = i_2+1
                            line_eat_2 = [line_eat_int_2]
                            line_count_int_2 = i_2+3
                            line_count_2 = [line_count_int_2]
                            line_three_int = i_2+18
                            line_three = [line_three_int]

                            with open(file) as f_2:
                                for line, line_content in enumerate(f_2):

                                    if line in line_eat_2:
                                        # print(line)
                                        # print(line_content)
                                        eat_2 = re.findall(pattern_eat, line_content)
                                        print(eat_2)
                                        print('')

                                    if line in line_count_2:
                                        # print(line)
                                        # print(line_content)
                                        count_2 = re.findall(pattern_count, line_content)
                                        print(count_2)
                                        print('')

                                    if line in line_three:
                                        a = re.findall(pattern_start_3, line_content)
                                        if a:
                                            i_3 = line_three_int
                                            line_eat_int_3 = i_3+1
                                            line_eat_3 = [line_eat_int_3]
                                            line_count_int_3 = i_3+3
                                            line_count_3 = [line_count_int_3]
                                            line_four_int = i_3+18
                                            line_four = [line_four_int]

                                            with open(file) as f_3:
                                                for line, line_content in enumerate(f_3):

                                                    if line in line_eat_3:
                                                        # print(line)
                                                        # print(line_content)
                                                        eat_3 = re.findall(pattern_eat, line_content)
                                                        print(eat_3)
                                                        print('')

                                                    if line in line_count_3:
                                                        # print(line)
                                                        # print(line_content)
                                                        count_3 = re.findall(pattern_count, line_content)
                                                        print(count_3)
                                                        print('')

                                                    if line in line_four:
                                                        a = re.findall(pattern_start_4, line_content)
                                                        if a:
                                                            i_4 = line_four_int
                                                            line_eat_int_4 = i_4+1
                                                            line_eat_4 = [line_eat_int_4]
                                                            line_count_int_4 = i_4+3
                                                            line_count_4 = [line_count_int_4]
                                                            line_five_int = i_4+18
                                                            line_five = [line_five_int]

                                                            with open(file) as fp:
                                                                for line, line_content in enumerate(fp):

                                                                    if line in line_eat_4:
                                                                        # print(line)
                                                                        # print(line_content)
                                                                        eat_4 = re.findall(pattern_eat, line_content)
                                                                        print(eat_4)
                                                                        print('')

                                                                    if line in line_count_4:
                                                                        # print(line)
                                                                        # print(line_content)
                                                                        count_4 = re.findall(pattern_count, line_content)
                                                                        print(count_4)
                                                                        print('')

                                                                    if line in line_five:
                                                                        a = re.findall(pattern_start_5, line_content)
                                                                        if a:
                                                                            i_5 = line_five_int
                                                                            line_eat_int_5 = i_5+1
                                                                            line_eat_5 = [line_eat_int_5]
                                                                            line_count_int_5 = i_5+3
                                                                            line_count_5 = [line_count_int_5]
                                                                            line_six_int = i_5+18
                                                                            line_six = [line_six_int]

                                                                            with open(file) as fp:
                                                                                for line, line_content in enumerate(fp):

                                                                                    if line in line_eat_5:
                                                                                        print(line)
                                                                                        print(line_content)
                                                                                        eat_5 = re.findall(pattern_eat, line_content)
                                                                                        print(eat_5)
                                                                                        print('')

                                                                                    if line in line_count_5:
                                                                                        print(line)
                                                                                        print(line_content)
                                                                                        count_5 = re.findall(pattern_count, line_content)
                                                                                        print(count_5)
                                                                                        print('')

                                                                                    if line in line_six:
                                                                                        a = re.findall(pattern_start_6, line_content)
                                                                                        if a:
                                                                                            i_6 = line_six_int
                                                                                            line_eat_int_6 = i_6+1
                                                                                            line_eat_6 = [line_eat_int_6]
                                                                                            line_count_int_6 = i_6+3
                                                                                            line_count_6 = [line_count_int_6]
                                                                                            line_seven_int = i_6+18
                                                                                            line_seven = [line_seven_int]

                                                                                            with open(file) as fp:
                                                                                                for line, line_content in enumerate(fp):

                                                                                                    if line in line_eat_6:
                                                                                                        print(line)
                                                                                                        print(line_content)
                                                                                                        eat_6 = re.findall(pattern_eat, line_content)
                                                                                                        print(eat_6)
                                                                                                        print('')

                                                                                                    if line in line_count_6:
                                                                                                        print(line)
                                                                                                        print(line_content)
                                                                                                        count_6 = re.findall(pattern_count, line_content)
                                                                                                        print(count_6)
                                                                                                        print('')

                                                                                                    if line in line_seven:
                                                                                                        a = re.findall(pattern_start_7, line_content)
                                                                                                        if a:
                                                                                                            i_7 = line_seven_int
                                                                                                            line_eat_int_7 = i_7+1
                                                                                                            line_eat_7 = [line_eat_int_7]
                                                                                                            line_count_int_7 = i_7+3
                                                                                                            line_count_7 = [line_count_int_7]
                                                                                                            line_eight_int = i_7+18
                                                                                                            line_eight = [line_eight_int]

                                                                                                            with open(file) as fp:
                                                                                                                for line, line_content in enumerate(fp):

                                                                                                                    if line in line_eat_7:
                                                                                                                        print(line)
                                                                                                                        print(line_content)
                                                                                                                        eat_7 = re.findall(pattern_eat, line_content)
                                                                                                                        print(eat_7)
                                                                                                                        print('')

                                                                                                                    if line in line_count_7:
                                                                                                                        print(line)
                                                                                                                        print(line_content)
                                                                                                                        count_7 = re.findall(pattern_count, line_content)
                                                                                                                        print(count_7)
                                                                                                                        print('')
