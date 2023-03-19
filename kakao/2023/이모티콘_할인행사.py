from itertools import product

# def solution(users, emoticons):
#     discounts = [10, 20, 30, 40]
#     results = []
#
#     for discount in product(discounts, repeat=len(emoticons)):
#         sum_user = 0
#         sum_pay = 0
#         for rate, limit in users:
#             pay = 0
#             for index, emoticon in enumerate(emoticons):
#                 if discount[index] >= rate:
#                     pay += (1-0.01*discount[index]) * emoticon
#             if pay >= limit:
#                 sum_user +=1
#             else:
#                 sum_pay += pay
#         results.append([sum_user, sum_pay])
#     results.sort(key=lambda x: [-x[0], -x[1]])
#     return results[0]


# def solution(users, emoticons):
#     discounts = [10, 20, 30, 40]
#     results = []
#
#     def dfs():




# users = [[40, 10000], [25, 10000]]
# emoticons = [7000, 9000]
# solution(users, emoticons)

def permute(elements):

    results = []

    visited = [False] * 3


    def dfs(node):
        visited.append(node)
        if len(visited) ==3:
            print(visited)
        for index, node in enumerate(elements):
            if not visited[index]:
                visited[index] = True
                dfs
                visited[index] = False

    dfs(1)
permute([1,2,3])























