def onlyOneTimeNumber(array):
    a=list(set(array))
    for i in array:
        if array.count(i)==1:
            b=a.pop(a.index(i))

    return b

def main():
    array = [2, 35, 8, 16, 8, 2, 7, 35]
    num = onlyOneTimeNumber(array)
    print("num=%d," % num)


if __name__ == '__main__':
    main()