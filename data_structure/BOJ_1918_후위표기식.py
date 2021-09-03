# 1918 후위표기식 스택
import sys
input = sys.stdin.readline

state = str(input())

stack = list()
result = list()
for x in state:
    if x == "(":
        stack.append(x)
    elif x==")":
        while stack and stack[-1]!= "(":
            result.append(stack.pop())
        stack.pop()
    elif x== "+" or x == "-":
        while stack and stack[-1]!="(":
            result.append(stack.pop())
        stack.append(x)
    elif x == "*" or x=="/":
        while stack and (stack[-1]=="*" or stack[-1] =="/"):
            result.append(stack.pop())
        stack.append(x)
    elif x.isalpha():
        #알파벳이라면
        result.append(x)
if stack:
    while stack:
        result.append(stack.pop())
for x in result:
    print(x, end="")
