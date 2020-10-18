# Written by KirinFuji
#
# Transposition Cipher
# HELLO WORLD
# 
# [H][E][L][L]
# [O][ ][W][O]
# [R][L][D][ ]
#
# HORE LLWDLO |
#
# [0, 0] 1 1
# [0, 1] 2   2
# [0, 2] 3     3
# [0, 3] 4       4
#
# [1, 0] 5 5
# [1, 1] 6   6
# [1, 2] 7     7
# [1, 3] 8       8
#
# [2, 0] 9 9
# [2, 1] 10  10
# [2, 2] 11    11
# [2, 3] 12      12

# 1,5,9, 2,6,10, 3,7,11

import math

def text_info(text,key):
    length = len(text)
    rows = math.ceil(length / key)
    padding = key - (length % key)
    return [length, rows, padding]

def generate_table(rows, columns):
    return [["" for x in range(columns)] for y in range(rows)]

def display_table(table):
    for i in table:
        print(i)

def populate_table(string, key):
    length, rows, padding = text_info(string,key)
    table = generate_table(rows, key)
    pass_ = 0 
    for r in range(rows):
        for c in range(key):
            if pass_ <= length - 1:
                table[r][c] = string[pass_]
            pass_ += 1
    display_table(table)
    return [table, length, rows, padding, key, string]

    # 0,4,8, 1,5,9, 2,6,10
def get_cipher(table, rows, key, string):
    ciphertext = ""
    for c in range(key):
        for r in range(rows):
            ciphertext = ciphertext + table[r][c]
    return ciphertext

def encrypt(string, key):
    master = populate_table(string, key)
    ciphertext = get_cipher(master[0], master[2], master[4], master[5])
    print(ciphertext + "|" + str(master[3]))

def rev_cipher(table, rows, key, ciphertext, length):
    pass_ = 0
    for c in range(key):
        for r in range(rows):
            if pass_ <= length - 1:
                table[r][c] = ciphertext[pass_]
            pass_ += 1
    return table

def get_text(table, rows, key):
    text = ""
    for r in range(rows):
        for c in range(key):
            #print(f"[{r}][{c}]")
            text = text + table[r][c]
    return text

def decrypt(ciphertext, key):    
    length, rows, padding = text_info(ciphertext,key)
    table = generate_table(rows, key)
    table = rev_cipher(table, rows, key, ciphertext, length)
    display_table(table)
    print(get_text(table, rows, key) + "|" + str(padding))


encrypt("Hello World", 4)
decrypt("Hore llWdlo", 4)

