def get_ip(s):
    length=len(s)
    temp=0
    res_list=[]
    for i in range(length-1):
        if int(s[i])>0:
            temp=s[i]+s[i+1]
            temp_list=list(s[:i])+[temp]+list(s[i+2:])
            temp=".".join(temp_list)
            res_list.append(temp)
    return res_list

def main():
    s = '10112'
    res = get_ip(s)
    for i in res:
        # 每个i代表一个合法的ip字符串
        print(i)


if __name__ == '__main__':
    main()