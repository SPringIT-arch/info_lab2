def main():
    func = int(input("""Выберите функцию из предложенных
    1) Кодирование
    2) Декодирование

Номер функции: """))

    if func == 1:
        num = input("Введите код: ")
        print(tohammig(num))
    elif func == 2:
        num = input("Введите код: ")
        decode(num)
        


def gen(num : str) -> str:
    for i in num:
        yield i


def tolist(num : str) -> list:
    return list(map(int, [i for i in num]))


def tohammig(num : str) -> str:
    innum = num
    ln = len(innum)
    nxt = gen(innum)
    num = []
    n = 0

    while ln >= (2**n) - (n + 1):
        n += 1

    ln = ln + n

    r = [2**i for i in range(n)]

    for i in range(ln):
        if i + 1 in r:
            num.append(0)
        else:
            num.append(int(nxt.__next__()))

    for n in range(n):
        flag = 0
        for i in range(2**n, ln + 1, 2**(n+1)):
            for j in num[i - 1 : i + 2**n - 1]:
                flag = flag ^ j

        num[(2**n) - 1] = int(flag)

    return ''.join(map(str, num))[:ln - 1]


def decode(num : str) -> str:
    num = tolist(num)
    ln = len(num)
    
    n = 0

    while ln > (2**n):
        n += 1

    r = [num[2**i - 1] for i in range(n)]

    ii = [''] * len(r)

    for n in range(n):
        num[2**n - 1] = 0
        flag = 0
        for i in range(2**n, ln + 1, 2**(n+1)):
            for j in num[i - 1 : i + 2**n - 1]:
                flag = flag ^ j
        
        ii[n] = int(flag)

    err = 0
    for i in range(len(r)):
        if r[i] != ii[i]:
            err += 2**i            

    if err == 0:
        print('ошибок нет')
        print(''.join(map(str, num)))
    else:
        print(f'ошибка в бите {err}')
        num[err - 1] = int(not(num[err - 1]))
        print(''.join(map(str, num)))

    return ''.join(map(str, num))

if __name__ == "__main__":
    main()
