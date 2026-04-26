'''
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.

'''

a = 5000
b = 9490

inicio = a if a % 2 == 1 else a + 1
fim = b if b % 2 == 1 else b - 1

# total = sum(range(inicio, fim + 1, 2)) # outra forma de somar

total = 0
for i in range(inicio, fim + 1, 2):
    total += i



print(f"após a soma dos números ímpares: {total}") # 16265025