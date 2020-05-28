import csv
import numpy
import time

start_time = time.time()

f = open('./test.csv', 'r', encoding='utf-8')
read = csv.reader(f)
p_list = [[] for _ in range(10)]
cnt = 0

for line in read:
    for i in range(10):
        try:
            p_list[i].append(int(line[i]))
        except:
            p_list[i].append(0)
    cnt += 1
f.close()

for i, p in enumerate(p_list):
    # print(p)
    print(f'p{i}')
    print('min', min(p))
    print('max', max(p))
    print('avg', sum(p)/len(p))
    print('standard deviation', numpy.std(p))
    print('median', numpy.median(p))
    print()

print('total line', cnt)

end_time = time.time()
print('time', end_time-start_time)