"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""
count = 0
n = int(input('Сколько встретилось друзей: '))
graph = [[int(i > j) for i in range(n)] for j in range(n)]
print(*graph, sep='\n')
for i in graph:
    count += i.count(1)
print(count)