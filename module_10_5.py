import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file1:
        while True:
            line = file1.readline().strip()
            all_data.append(line)
            if not line:
                break


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start1 = datetime.now()

for file in files:
    print(file)
    read_info(file)

end1 = datetime.now()
result_time = end1 - start1
print(f'Время выполнения линейного вызова: {result_time} ')

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start2 = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    end2 = datetime.now()
    multiprocessing_time = end2 - start2
    print(f'Время работы мультипроцесса: {multiprocessing_time}')
