def get_max_ascent_sequence(list):

    if list[0]==0:
        return [],0
    else:
        l=1
        alist=[list[0]]
        lmax=0
        mlist=[]
        for i in range(len(list)-1):
            if list[i]<list[i+1]:
                l+=1
                alist.append(list[i+1])
            else:
                if lmax<l:
                    lmax=l
                    mlist=alist
                l=1
                alist=[list[i+1]]
        return lmax,mlist

def main():
    a = [4, 2, 3, 7, 5, 1, 8, 11, 7, 3, 9, 10, 12]
    res, max_num = get_max_ascent_sequence(a)
    # res: 最长递增子序列, max_num: 该序列的长度
    print(res)
    print(max_num)


if __name__ == '__main__':
    main()