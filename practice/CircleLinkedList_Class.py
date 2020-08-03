#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, item=None):
        self.item = item
        self.link = None
        
class CircleLinkedList_Class:
    def __init__(self):
        self.root = Node()
        self.tail = self.root
        self.current = self.root
        
    def append(self, item):
        # 추가할 새노드를 만든다.
        newNode = Node(item)
        # 루트가 비어 있으면 루트와 테일을 새노드로 지정한다.
        if self.root.item == None:
            self.root = newNode
            self.tail = newNode
            newNode.link = self.root
        else:
        # 루트가 비어 있지 않으면 테일 뒤에 새노드를 추가하고 테일을 업데이트한다.
            _tmp = self.tail.link
            self.tail.link = newNode
            newNode.link = _tmp
            self.tail = newNode

    # 리스트 안에 모든 노드를 프린트 한다. 
    def print(self):
        curNode = self.root
        print(curNode.item)
        while curNode.link != self.root:
            curNode = curNode.link
            print(curNode.item)

    # 리스트에 존재하는 노드 수를 구한다.
    def listSize(self):
        curNode = self.root
        cnt = 1
        while curNode.link != self.root:
            curNode = curNode.link
            cnt += 1
        return cnt

    # 리스트에서 item을 가지는 노드를 current 노드로 지정한다.
    def setCurrent(self,item):
        curNode = self.root
        for i in range(self.listSize()):
            if curNode.item == item:
                self.current = curNode
            else:
                curNode = curNode.link

    # current 노드를 다음 노드로 바꾼다.
    def moveNext(self):
        self.current = self.current.link
        print("현재 위치는 ", self.current.item, "입니다.")

    # current 다음에 item을 삽입한다.
    def insert(self, item):
        # 삽입할 새 노드를 만든다.
        newNode = Node(item)
        # current 노드의 링크에 새 노드를 지정하고 새노드의 링크에 current 노드가 연결되어 있던 링크를 지정하여 연결한다.
        _tmp = self.current.link
        self.current.link = newNode
        newNode.link = _tmp
        # 만약, item1이 tail 노드 였다면 새노드를 tail 노드로 재지정한다.
        if self.current == self.tail:
            self.tail = newNode

    # item을 가지는 노드를 삭제한다.
    def delete(self, item):
        delYN = False
        # 루트가 삭제 대상 노드인지 확인한다. 루트를 삭제할 경우, 루트 다음 노드를 루트로 갱신하고 tail 노드의 링크를 갱신된 루트로 재지정한다.
        curNode = self.root
        if curNode.item == item:
            self.root = self.root.link
            self.tail.link = self.root
            delYN = True
        # 루트가 삭제 대상이 아닐 경우, 끝까지 탐색하면서 item이 존재하는 노드를 찾는다.
        # 찾았다면 preNode의 링크에 대상노드 링크를 넘겨준다. 만약, 대상 노드가 tail노드라면 tail 노드를 preNode로 변경한다.
        else:
            while curNode.link != self.root:
                preNode = curNode
                curNode = curNode.link
                if curNode.item == item:
                    preNode.link = curNode.link
                    if curNode == self.tail:
                        self.tail = preNode
                    delYN = True
        # 삭제를 하지 못했으면 error message를 출력한다.
        if delYN == False: print("delete failed")



