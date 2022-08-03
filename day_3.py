class ListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next_node = None


def Singlelist(node):
    list = []
    l = 0
    cur =node
    list.append(node.value)
    if cur == None:
        return l
    else:

        while cur.next_node != None:
            cur = cur.next_node

            if cur.value in list:
                l1 = len(list) - list.index(cur.value)
                if l1>l:
                    l=l1
                list = []
            list.append(cur.value)
        return l




def main():
    # 下面完成构造链表的代码
    #TODO code!!!
    # 调用你编写的代码函数, 唯一的参数是头指针head
    a1 = ListNode(3)
    a2 = ListNode(8)
    a3 = ListNode(7)
    a4 = ListNode(1)
    a5 = ListNode(2)
    a6 = ListNode(3)
    a7 = ListNode(4)
    a8 = ListNode(5)
    a1.next_node=a2
    a2.next_node=a3
    a3.next_node=a4
    a4.next_node=a5
    a5.next_node=a6
    a6.next_node=a7
    a7.next_node=a8
    l1=Singlelist(a1)

    print('result length:', l1)

if __name__ == '__main__':
    main()
