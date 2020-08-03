#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Queue:
    def __init__(self):
        self.q = []
        
    def enQueue(self, item):
        self.q.append(item)
        
    def deQueue(self):
        if self.isEmpty() == False: 
            return self.q.pop(0)
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        if len(self.q) > 0:
            return False
        else:
            return True
        
    def peek(self):
        if self.isEmpty() == False: 
            return self.q[0]
    
    def delete(self, item):
        if item in self.q: 
            self.q.remove(item)
        else:
            print("해당 아이템이 존재하지 않습니다.")


