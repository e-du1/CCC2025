"""
CCC 2025 Senior Problem 1
2025/02/19
"""

  

def Solution(inputNum):
    input = inputNum.split()
    b1 = int(input[0])
    b2 = int(input[2])
    h1 = int(input[1])
    h2 = int(input[3]) 
    
    a = b1 + b2

    if input[3] > input[1]:
        b = int(input[3])
    else:
        b = int(input[1])
    return 2*a + 2*b
    
