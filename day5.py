def maxDistance(array):
    length=len(array)
    max=0
    temp=0
    for i in range(1,length):
        l1=array[i]
        for j in range(0,i):
            if array[i]>array[j]:
                temp=i-j
                if temp>max:
                    max=temp
    return max

def maxDistance1(array):
    length=len(array)
    dp=[]
    min_n=array[0]
    for i in range(length):
        if i==0:
            dp.append("O")
        else:
            if array[i]<min_n:
                dp.append("O")
                min_n=array[i]
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
        if index2>index1 and index2-index1>max_length:
            max_length=index2-index1
            max_index2=index2
            max_index1=index1
            index2=length-1
        index1-=1
    return max_length


def main():
    array = [5, 3, 4, 0 ,1, 4, 1]
    dis = maxDistance1(array)
    print("dis=%d," % dis)


if __name__ == '__main__':
    main()