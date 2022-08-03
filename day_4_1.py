def  getclosenumber(x, y):
    l2=[]
    for j in range(len(x)):
        l1=[i for i in x if i>=y[j]]
        if min(l1)>y[j]:

            t=x.pop(x.index(min(l1)))
            l2.append(t)
            x.sort()
            break
        if min(l1)==y[j]:
            l2.append(x.pop(x.index(min(l1))))
    l2+=x
    return l2





def main():
    x = [4, 6, 2, 0, 3, 5]
    y = [5, 3, 2, 4, 1, 0]
    res = getclosenumber(x, y)
    print("res=%s" % res)

if __name__ == '__main__':
    main()

