
# Written by KirinFuji as part of Learning basic ciphers

# WIP

# Rail Fence cipher

# columns = length of text
# rows = key or 'n of rails'
def generate_table(key,text):
    return [[None for x in range(len(text))] for y in range(key)]

def display_table(table):
    for i in table:
        print(i)

def table_input(table,row,column,input_):
    table[row][column] = input_

def create_pattern(key):
    key = key + 1
    pat_ = list(range(1,key))
    s = ""
    for x in pat_:
        s = s + str(x)    
    pat_.pop()
    pat_.reverse()
    for x in pat_:
        s = s + str(x)
    for x in s:
        yield x

def l2s(list_):
    s = ""
    for i in list_:
        s = s + str(i)
    return s

def t_insert(key,text,table):
    pattern = list(create_pattern(key))
    pattern = l2s(pattern)
    while len(pattern) < len(text):
        pattern = pattern[:-1] + pattern
    iter_ = 0
    
    for letter in text:
        col = iter_
        table_input(table,int(pattern[iter_])-1,col,letter)
        iter_ += 1

def get_ciphertext(table):
    s = ""
    for tab in table:
        for letter in tab:
            if letter != None:
                s = s + letter
    return "|" + s + "|"

# From https://www.boxentriq.com/code-breaking/rail-fence-cipher
#Tarot arilmu sl.rs hersheltit a rwelti s o esreck  os  e ttttahr e tirlsn ehteorlsns ynganehiroyngTaagrno tp nagrs y gtnthhr y gialgnne tponlgnh lnia e iwolni a g ns epkn gsh l it t hw l iisloneertco loni lnmaue isoln.Trasr ohte rasrsiylgmnuh rsylg.soerc o ettaret   sek s
# From this python script
#Tarot arilmu sl.rs hersheltit a rwelti s o esreck  os  e ttttahr e tirlsn ehteorlsns ynganehiroyngTaagrno tp nagrs y gtnthhr y gialgnne tponlgnh lnia e iwolni a g ns epkn gsh l it t hw l iisloneertco loni lnmaue isoln.Trasr ohte rasrsiylgmnuh rsylg.soerc o ettaret   sek s


text = "This is a really long string meant to ensure that the cipher works on really long strings. This is a really long string meant to ensure that the cipher works on really long strings. This is a really long string meant to ensure that the cipher works on really long strings."
key = 7
table = generate_table(key,text)
display_table(table)
t_insert(key,text,table)
display_table(table)
print(get_ciphertext(table))
