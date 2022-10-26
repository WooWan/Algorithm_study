import sys, math
sys.setrecursionlimit(10**8)

def solution(n, k):
    answer = 0
    # INF = 100000
    # primeArray =[False]*2 + [True]*INF
    def convertKNumber(number):
        if k > number:
            return str(number)
        return convertKNumber(number // k) + str(number % k)

    # 만약 실제 코딩테스트하라면 isPrime을 구현한 뒤, 시간 초과를 만났을 것 => 빠르게 에라토스테네스 검색 후 적용
    def isPrime(num):
        if num <= 1: return False
        print(num)
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    # def filterPrimeNum():
    #     m = int(INF ** 0.5)
    #     for i in range(2, m + 1):
    #         if primeArray[i] == True:  # i가 소수인 경우
    #             for j in range(i + i, INF, i):  # i이후 i의 배수들을 False 판정
    #                 primeArray[j] = False
    #
    # def isPrime(num):
    #     return primeArray[num] == True

    convertedNum = convertKNumber(n)
    # filterPrimeNum()
    temp = ""
    for num in convertedNum:
        if num == "0" and temp != "":
            if isPrime(int(float(temp))) and temp != "1":
                answer += 1
            temp = ""
        else:
            temp += str(num)

    if temp != "" and isPrime(int(float(temp))):
        answer += 1
    return answer


print(solution(437674, 3))
print(solution(110011, 10))
