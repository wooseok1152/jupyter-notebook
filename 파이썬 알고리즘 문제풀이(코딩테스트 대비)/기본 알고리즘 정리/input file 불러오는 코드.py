'''sys.stdin을 불러오는 것이 빠르다'''
'''쥬피터노트북에선 해당 코드 실행 안됨'''
import sys

sys.stdin = open("./stdin_test.txt", "r")
first_line = input().rstrip("\n").split()
second_line = input().rstrip("\n").split()

print(first_line, "\n")
print(second_line, "\n")
