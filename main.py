def main():
    pass


def gen(num : str) -> str:
    for i in num:
        yield i


def tolist(num : str) -> list:
    return list(map(int, [i for i in num]))


def tohemmig(num : str) -> str:
    innum = input('Число: ')
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
        for i in range(2**n, ln + n, 2**(n+1)):
            for j in num[i - 1 : i + 2**n - 1]:
                flag = flag ^ j

        num[(2**n) - 1] = int(flag)

    return ''.join(map(str, num))


if __name__ == "__main__":
    main()