"""
CCC 2025 Senior Problem 2
2025/02/19
"""


cipher = list(input())
c = int(input())

cipher_length = 0
cipher_list = []    # stores repeat counts
cipher_value = []   # stores characters
saved_value = ""

for i in range(len(cipher)):
    if cipher[i].isalpha():
        cipher_list.append(cipher[i])
        if cipher[i-1].isnumeric() and i != 0:
            cipher_value.append(int(saved_value))
            cipher_length += int(saved_value)
            saved_value = ""
    else:
        saved_value += cipher[i]

cipher_value.append(int(saved_value))
cipher_length += int(saved_value)
# print(cipher_value)

rle_list = []
index = c % cipher_length
# print(cipher_length)

counter = 0 
for i in cipher_value:
    for j in range(i):
        rle_list.append(cipher_list[counter])
    counter += 1



# rle_list is a numerical list of the cipher (non-repeated tho)
print(rle_list[index])