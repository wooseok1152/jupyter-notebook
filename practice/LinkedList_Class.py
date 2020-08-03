
#!/usr/bin/env python
# coding: utf-8

# In[5]:


# delete 메소드 구현
# find method를 이용해 delete 할 item의 인덱스를 구한다.
# del item이 첫번째 노드면 self.root에 del item의 링크를 넣는다.
# del item이 중간노드면 index-1 번째 링크에 del item 링크를 넣는다.
# 마지막 노드라면 index-1 번째 링크에 None를 넣는다.

class Node:
    def __init__(self, item=None):
        self.item = item
        self.link = None
        
class LinkedList:
    def __init__(self):
        self.root = Node()

    def append(self, item):
        newNode = Node(item)
        curNode = self.root
        if curNode.item == None:
            self.root = newNode
        else:
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode
    
    def print(self):
        curNode = self.root
        print(curNode.item)
        while curNode.link != None:
            curNode = curNode.link
            print(curNode.item)
    
    def listSize(self):
        curNode = self.root
        cnt = 1
        while curNode.link != None:
            curNode = curNode.link
            cnt += 1
        return cnt
            
    def insert(self, idx, item):
        n = self.listSize()
        if idx < 0 or idx >= n:
            print("index range error")
        else:
            newNode = Node(item)
            curNode = self.root
            if idx == 0:
                _tmp = self.root
                self.root = newNode
                newNode.link = _tmp
            else:
                for curIdx in range(idx-1):
                    curNode = curNode.link
                _tmp = curNode.link
                curNode.link = newNode
                newNode.link = _tmp
    
    def find(self, item):
        find = -1
        idx = 0
        if self.root.item == item:
            find += 1
        else:
            curNode = self.root
            while curNode.link != None:
                curNode = curNode.link
                idx += 1
                if curNode.item == item:
                    find = idx
                    break
        return find
    
    def delete(self,item):
        delYN = False
        curNode = self.root
        preNode = curNode
        if curNode.item == item:
            self.root = self.root.link
            delYN = True
        else:
            while curNode.link != None:
                preNode = curNode
                curNode = curNode.link
                if curNode.item == item:
                    preNode.link = curNode.link
                    delYN = True
        if curNode.item == item:
            preNode.link = None
            delYN = True
        if delYN == False:
            print("delete failed")


        

