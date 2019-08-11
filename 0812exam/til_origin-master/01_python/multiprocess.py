from multiprocessing import Process, Queue
import time


def work(id, start, end, result):
    for i in range(start, end):  # 2 ~ 10
        for j in range(2, int(end ** 0.5)+1):
            if i % j == 0:
                break
        else:
            pass


if __name__ == '__main__':
    start_time = time.time()

    start = 2
    end = int(1e6)

    q = Queue()

    p1 = Process(target=work, args=(1, start, end//2, q))
    p2 = Process(target=work, args=(2, end//2, end, q))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    q.put('STOP')

    total = 0
    while True:
        result = q.get()
        if result == 'STOP':
            break
            
    end_time = time.time()
    print(end_time - start_time)
