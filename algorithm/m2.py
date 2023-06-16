#Encryption
'''
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let  be the length of this text.
Then, characters are written into a grid:

Example
haveaniceday
>hae and via ecy
grid:
have
anic
eday
'''
def encryption(s):
    n = len(s) ** (0.5)
    c_len = math.ceil(n)
    str_list = [""] * c_len
    for i in range(len(s)):
        index = i % c_len
        str_list[index] += s[i]
    return " ".join(str_list)