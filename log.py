from datetime import date, timedelta, datetime
import os
import pandas as pd

rec1 = str('')
list1 = []
for day in range(0, -5, -1):
    d = date.today() + timedelta(days=day)
    d = 'log_' + str(d).replace('-', '_') + '.log'
    dir = os.path.join('E:\Programms\log', d)
    print(dir)

    if os.path.exists(dir):
        with open(dir) as file_log:
            for line in file_log:
                if len(line) > 1:
                    string = line.replace('\n', '').split(';')
                    if string and string[1] == 'ERROR':
                        rec1 = string
                        continue
                    if rec1 and rec1[1] == 'ERROR' and string[1] == '5':
                        # print(rec1)
                        # print(string)
                        list1.append(rec1)
                        list1.append(string)
                        rec1 = str('')
                        string = str('')

        diction = pd.DataFrame(list1)
        diction = diction.sort_values(0)
        print(diction)

# Запись в фаил
        d = 'err_' + d
        dir_wr = os.path.join('E:\Programms\log', d)
        file = open(dir_wr, 'w')
        for s in list1:
            file.write(s[0] +';' + s[1] + '\n')
        file.close()
