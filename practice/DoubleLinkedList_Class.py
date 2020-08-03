#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Node Class: item으로 value를 가지고 right, left를 가진다. link가 없을 경우, None을 입력한다.
class DNode:
    def __init__(self, item = None):
        self.item = item
        self.right = None
        self.left = None

class DoubleLinkedList:
    def __init__(self):
        self.root = DNode()
        
    def append(self, item):
        curNode = self.root
        newNode = DNode(item)
        while curNode != None:
            if curNode.item == None:
                self.root = newNode
                break
            elif curNode.right == None:
                curNode.right = newNode
                newNode.left = curNode
                break
            else:
                curNode = curNode.right
                
    def insert(self, index, item):
        newNode = DNode(item)
        curNode = self.root
        if index == 0:
            if self.root.item == None:
                self.root = newNode
            else:
                self.root = newNode
                newNode.right = curNode
        elif index < 0 or index >= self.listSize():
            print('error')
        else:
            for i in range(index-1):
                curNode = curNode.right
            _tmp = curNode.right
            curNode.right = newNode
            newNode.left = curNode
            newNode.right = _tmp
            newNode.right.left = newNode
            
    def find(self, item):
        curNode = self.root
        index = 0
        while curNode != None:
            if curNode.item == item:
                return index
            else:
                curNode = curNode.right
                index += 1
        if curNode == None:
            index = -1
            return index
        
    def delete(self, item):
        curNode = self.root
        index = self.find(item)
        if index == -1:
            print("삭제할 아이템이 없습니다.")
        elif index == 0:
            self.root = curNode.right
        elif index+1 == self.listSize():
            while curNode.right != None:
                curNode = curNode.right
            curNode.left.right = None
        else:
            for i in range(index):
                curNode = curNode.right
            curNode.left.right = curNode.right
            curNode.right.left = curNode.left
                
    def listSize(self):
        curNode = self.root
        size = 0
        while curNode != None:
            if curNode.item == None:
                return size
            else:
                curNode = curNode.right
                size += 1
        return size

    def print(self):
        curNode = self.root
        while curNode != None:
            print(curNode.item)
            curNode = curNode.right

