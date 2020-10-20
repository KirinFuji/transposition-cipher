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

def table_select(table,row,column):
    return table[row][column]

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
###############################################
def encrypt(text,key):

    def get_ciphertext(table):
        s = ""
        for tab in table:
            for letter in tab:
                if letter != None:
                    s = s + letter
        return "|" + s + "|"

    table = generate_table(key,text)
    t_insert(key,text,table)
    display_table(table)
    print(get_ciphertext(table))
###########################################
        
def decrypt(text,key):

    def get_decipher_locations_setup(table):
        for tabl in table:
            l=[i for i,v in enumerate(tabl) if v != None]
            yield(l)

    def get_decipher_locations(table):
        var = list(get_decipher_locations_setup(table))
        for t in list(range(len(var))):
            for i in list(range(len(var[t]))):
                #print(t,var[t][i])
                yield(t,var[t][i])

    def decipher_to_locations(table,text):
        iter_ = 0
        for i in list(get_decipher_locations(table)):
            #print(table[i[0]][i[1]])
            print(str(i[0]) + " " + str(i[1]))
            print(text[iter_])
            table[i[0]][i[1]] = text[iter_]
            iter_ += 1

    def get_cleartext(table):
        pattern = list(create_pattern(key))
        pattern = l2s(pattern)
        while len(pattern) < len(text):
            pattern = pattern[:-1] + pattern

        s = ""    
        for i in range(len(text)):
            col = i
            row = int(pattern[i])-1
            s = s + table_select(table,row,col)
        return s

    table = generate_table(key,text)
    t_insert(key,text,table)
    decipher_to_locations(table,text)
    display_table(table)
    return get_cleartext(table)

###################################################

# "This is a really long string meant to ensure that the cipher works on really long strings. This is a really long string meant to ensure that the cipher works on really long strings. This is a really long string meant to ensure that the cipher works on really long strings."
# From https://www.boxentriq.com/code-breaking/rail-fence-cipher
#Tarot arilmu sl.rs hersheltit a rwelti s o esreck  os  e ttttahr e tirlsn ehteorlsns ynganehiroyngTaagrno tp nagrs y gtnthhr y gialgnne tponlgnh lnia e iwolni a g ns epkn gsh l it t hw l iisloneertco loni lnmaue isoln.Trasr ohte rasrsiylgmnuh rsylg.soerc o ettaret   sek s
# From this python script
#Tarot arilmu sl.rs hersheltit a rwelti s o esreck  os  e ttttahr e tirlsn ehteorlsns ynganehiroyngTaagrno tp nagrs y gtnthhr y gialgnne tponlgnh lnia e iwolni a g ns epkn gsh l it t hw l iisloneertco loni lnmaue isoln.Trasr ohte rasrsiylgmnuh rsylg.soerc o ettaret   sek s

# ['H', None, None, None, None, None, None, None, 'r', None, None, None, None, None, None, None, 'w', None, None, None, None, None, None, None, 'o', None, None, None, None, None, None, None, 's', None, None, None, None, None, None, None, 'e', None, None, None, None, None, None, None, 'b', None, None, None, None, None, None, None, 'n', None, None]
# [None, 'e', None, None, None, None, None, 'o', None, 'd', None, None, None, None, None, 'o', None, ' ', None, None, None, None, None, 'y', None, 'u', None, None, None, None, None, 'd', None, 't', None, None, None, None, None, 'v', None, 'n', None, None, None, None, None, ' ', None, 'e', None, None, None, None, None, 'i', None, 'g', None]
# [None, None, 'l', None, None, None, 'G', None, None, None, 'o', None, None, None, 'h', None, None, None, 'h', None, None, None, ' ', None, None, None, 'r', None, None, None, 'a', None, None, None, 'e', None, None, None, 'd', None, None, None, 't', None, None, None, 's', None, None, None, 'e', None, None, None, 'o', None, None, None, '?']
# [None, None, None, 'l', None, ' ', None, None, None, None, None, 'n', None, ' ', None, None, None, None, None, 'a', None, 'e', None, None, None, None, None, ' ', None, 'o', None, None, None, None, None, 'r', None, 'a', None, None, None, None, None, 'u', None, 'e', None, None, None, None, None, 'n', None, 'g', None, None, None, None, None]
# [None, None, None, None, 'o', None, None, None, None, None, None, None, ',', None, None, None, None, None, None, None, 'v', None, None, None, None, None, None, None, 'r', None, None, None, None, None, None, None, ' ', None, None, None, None, None, None, None, 'r', None, None, None, None, None, None, None, ' ', None, None, None, None, None, None]
# |Hrwosebneodo yudtvn eiglGohh raedtseo?l n ae orauengo,vr r |
# 0,0|0,8|0,16|0,24|0,32|0,40|0,48|0,56|1,1|1,7|1,9|1,15|1,17|1,23|1,25|1,31|1,33|1,39|1,41|1,47|1,49|1,55|1,57|2,2|2,6|2,10|2,14|2,18|....

# n+8 n+8 n+8
# 0,0|0,8|0,16|0,24|0,32|0,40|0,48|0,56
# n+6 n+2 n+6 n+2
# 1,1|1,7|1,9|1,15|1,17|1,23|1,25|1,31|1,33|1,39|1,41|1,47|1,49|1,55|1,57
# n+4 n+4 n+4
# 2,2|2,6|2,10|2,14|2,18|2,# 15 -
# n+6 n+2 n+6 n+2
# 3,3
# #n+8 n+8 n+8
# 4,4|0,8|0,16|0,24|0,32|0,40|0,48|0,56

#text = "This is a really long string meant to ensure that the cipher works on really long strings. This is a really long string meant to ensure that the cipher works on really long strings. This is a really long string meant to ensure that the cipher works on really long strings."
#key = 7
#text = "Tarot arilmu sl.rs hersheltit a rwelti s o esreck  os  e ttttahr e tirlsn ehteorlsns ynganehiroyngTaagrno tp nagrs y gtnthhr y gialgnne tponlgnh lnia e iwolni a g ns epkn gsh l it t hw l iisloneertco loni lnmaue isoln.Trasr ohte rasrsiylgmnuh rsylg.soerc o ettaret   sek s"
#encrypt(text,key)
    
#cleartext = l2s(list(decrypt(text,key)))
#print(cleartext)

#encrypt("Hello World! Im Alive!",5)

#|HrAeol llWdmil !Iv!o e|

text = "HrAeol llWdmil !Iv!o e"
key = 5
cleartext = l2s(list(decrypt(text,key)))
print(cleartext)
# output: Hello World! Im Alive!
