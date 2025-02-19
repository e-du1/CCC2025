"""
CCC 2025 Senior Problem 2
2025/02/19
"""


cipher = list(input())
c = int(input())

cipher_length = 0
cipher_list = []
cipher_value = []
saved_value = ""
for i in range(len(cipher)):
    if i == 0:
        cipher_value.append(cipher[i])
    elif cipher[i].isdigit() == False:
        # if it is not a number
        # check to see if the previous value was a number
        if cipher[i-1].isdigit() == True:
            # step 1: save the current character as a cipher value
            
            cipher_value.append(cipher[i])
            # step 2: save the previous number to the cipher length
            cipher_list.append(int(saved_value))
            cipher_length += int(saved_value)
        else:
            cipher_value.append(cipher[i])
            continue
    else:
        # if it is a number
        if cipher[i-1].isdigit() == True:
            saved_value += cipher[i]
        else:
            # if the previous value was NOT a number, but this one is
            # we add it to a string called saved_value
            saved_value = cipher[i]

# we need to add the last value to the cipher list
cipher_list.append(int(saved_value))
cipher_length += int(saved_value)

# we now have cipher length and whatever the cipher is

# c is 'cth' character if we repeat infinitely the cipher
# print(f"the different values are: {cipher_list}")
# print(f"The characters are {cipher_value}")
# print(cipher_length)
index = c % cipher_length
# we now have a value that we're looking for 
for j in range(len(cipher_list)):
    x = cipher_list[j]
    if x >= index:
        print(cipher_value[j])
        break
    else:
        index -= x
        continue