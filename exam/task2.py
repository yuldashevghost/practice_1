from threading import Thread


def printer(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return inner


@printer
def reversed_nums(x: int):
    y = str(x)
    print(y[::-1])


if __name__ == '__main__':
    x = list(map(int, input().split()))
    thread = []
    for i in x:
        t = Thread(target=reversed_nums, args=(i,))
        t.start()
        thread.append(t)
    for th in thread:
        th.join()
