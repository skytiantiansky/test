def frog_jump(a):
    index=0

    t=0
    while t<len(a):
        if a[t]>1:
            t=a[t]+t
        else:
            t+=1
        index+=1
    return index


def main():
    a = [2, 1, 3, 1, 1]
    res = frog_jump(a)
    print(res)

if __name__ == '__main__':
    main()