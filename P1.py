"""
CCC 2025 Senior Problem 1
2025/02/19
"""

  


input = input().split()
b1 = int(input[0])
b2 = int(input[2])
# width of the first and second painting

h1 = int(input[1])
h2 = int(input[3]) 

widest = max(b1, b2)
highest = max(h1, h2)

p1 = 2 * (h1 + h2 + widest)
p2 = 2 * (b1 + b2 + highest)

print(min(p1, p2))