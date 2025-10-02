opac = 1

def minus():
    global opac
    opac -= 0.1
    print(opac)

def plus():
    global opac
    opac += 0.1
    print(opac)

print(opac)
minus()
minus()
