#!/usr/bin/env python
# coding: utf-8

# In[12]:


class Sort:
    def min(self, x):
        min_idx = 0
        min = x[0]
        for i in range(1, len(x)):
            if min > x[i]:
                min = x[i]
                min_idx = i
        return min_idx

    def sort(self, x, letter):
        if letter == "a":
            for i in range(len(x)):
                _tmp = x[i:]
                minindx_in_tmp = self.min(_tmp)
                x[i], x[minindx_in_tmp + i] = x[minindx_in_tmp + i], x[i]
            return x
        
        elif letter == "d":
            for i in range(len(x)):
                _tmp = x[i:]
                minindx_in_tmp = self.min(_tmp)
                x[i], x[minindx_in_tmp + i] = x[minindx_in_tmp + i], x[i]
            return list(reversed(x))
                
        else :
            print("fail")
    





