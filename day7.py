def get_min_value(a):
    left=0
    right=len(a)-1
    min_value=a[left]
    while left<=right:
        mid=int(left+(right-left)/2)
        min_value=min(a[left],min_value)

        if a[left]==a[mid] and a[right]==a[mid]:
            left+=1
        elif a[left]>=a[mid]:
            right=mid-1
            min_value=min(a[mid],min_value)
        else:
            left=mid+1
            min_value=min(a[left],min_value)
    return min_value


def main():
    a = [3, 4, 5, 6, 1, 2]
    res = get_min_value(a)
    print('res=%d' % res)


if __name__ == '__main__':
    main()