#1339 G4 greedy
import sys
input = sys.stdin.readline

n= int(input())
arr = list()
for i in range(n):
    arr.append(input().strip())

alphabet=dict()
for word in arr:
    for alpha in range(len(word)):
        if word[alpha] in alphabet:
            alphabet[word[alpha]]+= 10**(len(word)-alpha-1)
        else:
            alphabet[word[alpha]]= 10**(len(word)-alpha-1)

sorted_alphabet = sorted(alphabet.items(), key=lambda x:x[1], reverse=True)

answer=0
for x in range(len(sorted_alphabet)):
    answer += sorted_alphabet[x][1]*(9-x)

print(answer)