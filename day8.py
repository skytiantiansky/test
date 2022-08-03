def maxDistance(array):
    dp=[]
    length=len(array)
    min_num=array[0]
    for i in range(length):
        if i==0:
            dp.append("O")
        else:
            if array[i]<min_num:
                dp.append("O")
                min_num=array[i]
            else:
                dp.append("X")
    index1=index2=length-1
    max_index1=max_index2=-1
    max_length=0
    while index1>=0:
        if dp[index1]=="X":
            index1-=1
            continue
        while array[index2]<=array[index1] and index2>index1:
            index2-=1
        if array[index2]>array[index1] and index2-index1>max_length:
            max_length=index2-index1
            max_index1=index1
            max_index2=index2
            index2=length-1
        index1-=1

    return max_length

def main():
    array = [5, 3, 4, 0 ,1, 4, 1]
    dis = maxDistance(array)
    print("dis=%d," % dis)


if __name__ == '__main__':
    main()