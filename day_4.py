def get_max_ascent_sequence(list):
    hash_index={}
    length=len(list)
    max_count=0
    dp=[0]*length
    end=0
    for i in range(length):
        dp[i]=1
        for j in range(0,i):
            if list[i]>list[j]:
                if dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    hash_index[i]=j
                if dp[i]>max_count:
                    max_count=dp[i]
                    end=i
    result=[]
    while end>=0:
        result.append(list[end])
        if end in hash_index.keys():
            end=hash_index[end]
        else:
            end=-1
    result.reverse()
    return result,max_count



def main():
    a = [4, 2, 3, 7, 5, 1, 8, 11, 7, 3, 9, 10, 12]
    res, max_num = get_max_ascent_sequence(a)
    print(res)
    print(max_num)


if __name__ == '__main__':
    main()