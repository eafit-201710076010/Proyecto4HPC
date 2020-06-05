from random import choice

def string(length):
    DNA = ""
    for count in range(length):
        DNA+=choice("CGTA")
    return DNA

f = open("dataset.txt", "w")
lenght = 5
lines = 5

for i in range(lines):
    f.write(string(lenght)+'\n')
f.close()


