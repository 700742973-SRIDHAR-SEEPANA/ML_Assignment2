def count(li):
    up=0
    lo=0
    for x in li:
        if x.isupper(): up+=1
        if x.islower(): lo+=1
    print("No.of Upper-case characters:", up)
    print("No.of Lower-case characters:", lo)
inp='The quick Brow Fox'
count(inp)