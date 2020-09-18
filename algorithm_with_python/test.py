import sys
import time

start = time.time()
sys.stdin = open(r"C:\Users\my\Desktop\Documents\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 3\5. 수들의 합\in4.txt")
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

# print(n)
# print(m)
# print(a)

def numbers_sum_ocassion(m,number_list):
    
    start = time.time()
    count = 0
    for i in range(len(number_list)):
        
        for j in range(i, len(number_list)):
            
            if i == j:
                
                if number_list[i] == m:
                    
                    count = count + 1
                    break
                
                continue
            
#             print(sum(number_list[i:j+1]))
            if sum(number_list[i:j+1]) == m:
                
                count = count + 1
#                 print("count :", count)
                break
            
            if sum(number_list[i:j+1]) > m:

                break
                
    return count

print(numbers_sum_ocassion(m, a))
print(time.time() - start)