import sudan
import time

if __name__ == '__main__':

    print('Count without mapping')
    start = time.time()
    for i in range(22):
        print(f'n=1, x={i}, y={i}, result: {sudan.sudan_nomem(1,i,i)}')
    end = time.time()
    print(f"Took {end-start}")

    # y=3 is max recursion depth for n=2, x=1
    for i in range(3):
        print(f'n=2, x=1, y={i}, result: {sudan.sudan_nomem(2,1,i)}')

    print('\nCount with mapping')
    start = time.time()
    for i in range(900):
        print(f'n=1, x={i}, y={i}, result: {sudan.sudan_mem(1,i,i)}')
    end = time.time()
    print(f"Took {end-start}")

    for i in range(3):
        print(f'n=2, x=1, y={i}, result: {sudan.sudan_mem(2,1,i)}')