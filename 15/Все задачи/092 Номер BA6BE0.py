
list_answer = [int(input()) for _ in range(int(input()))]
print(sum(x for x in list_answer if x % 6 == 0 and x % 10 == 2))



