for line in open("d"):
    for c in line:
        if 0 <= ord(c) <= 256:
            print(c,end='')
