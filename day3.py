class ListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next_node = None
class Singlelist:
    def __init__(self,node):
        self.head=node
    def add(self,item):
        node=ListNode(item)
        if self.head==None:
            self.head=node
        else:
            node.next_node=self.head
            self.head=node
    def append(self,item):
        node=ListNode(item)
        if self.head==None:
            self.head=node
        else:
            cur=self.head
            while cur.next_node!=None:
                cur=cur.next_node
            cur.next_node=node
    def lengthOfCircle(self):
        list=[]
        l=0
        cur=self.head
        list.append(cur.value)
        if cur==None:
            return l
        else:

            while cur.next_node!=None:
                cur=cur.next_node
                if cur.value  in list:
                    l=len(list)-list.index(cur.value)
                    list=[]
                    return l
            return l


def main():
    # 下面完成构造链表的代码
    #TODO code!!!
    # 调用你编写的代码函数, 唯一的参数是头指针head
    node=ListNode(5)
    link1=Singlelist(node)
    res = link1.lengthOfCircle()
    print('result length:', res)

if __name__ == '__main__':
    main()
