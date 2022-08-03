def get_point_number(a):
    length=len(a)
    index=0
    left=0
    right=length-1
    mid=1
    while mid<length-1:
        if max(a[:mid+1])==a[mid] and min(a[mid:])==a[mid]:
            return mid
        elif max(a[:mid+1])!=a[mid] or min(a[mid:])!=a[mid]:
            mid+=1
    return None


def main():
    a = [1, 0, 1, 0, 1, 2, 3]
    res = get_point_number(a)
    print(res)

if __name__ == '__main__':
    main()