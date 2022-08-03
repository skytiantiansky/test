def hasSum(array,tarfet):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            r=array[i]+array[j]
            if r==tarfet:
                return 1,array[i],array[j]
    return 0,None,None


def hasSum1(array,target):
    array=sorted(array)
    i,j=0,len(array)-1
    while i<j:
        if array[i]+array[j]>target:
            j-=1
        elif array[i]+array[j]<target:
            i+=1
        else:
            break
    if i<j:
        return 1,array[i],array[j]
    else:
        return 0,None,None
def hasSum2(array,target):
    dict={}
    for i in range(len(array)):
        dict[array[i]]=i
    for j in range(len(array)):
        temp=target-array[j]
        if dict.get(temp)==None or dict.get(temp)==j:
            continue
        else:
            return 1,array[j],array[dict.get(temp)]
    return 0,None,None
def main():

    array = [1, 5, 7, 3]
    target_number = 10
    result, a, b = hasSum2(array, target_number)
    if result == 1:
        print('YES, %d + %d = %d' % (a, b, target_number))
    else:
        print('NO')



if __name__ == '__main__':
    main()