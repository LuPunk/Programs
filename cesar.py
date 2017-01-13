def cezar(n):
    big_chr = range(65, 91)
    small_chr = range(97, 123)

    if len(n) == 0:
        return (n)

    else:
        if ord(n) in big_chr:
            if (ord(n)+3) in big_chr:
                return (chr(ord(n)+3))
            else:
                return (chr((ord(n)+3)-26))

        elif ord(n) in small_chr:
            if (ord(n)+3) in small_chr:
                return (chr(ord(n)+3))
            else:
                return (chr((ord(n)+3)-26))

        else:
            return (n)

def uncezar(n):
    big_chr = range(65, 91)
    small_chr = range(97, 123)

    if len(n) == 0:
        return (n)

    else:
        if ord(n) in big_chr:
            if (ord(n) - 3) in big_chr:
                return (chr(ord(n) - 3))
            else:
                return (chr((ord(n) - 3) + 26))

        elif ord(n) in small_chr:
            if (ord(n) - 3) in small_chr:
                return (chr(ord(n) - 3))
            else:
                return (chr((ord(n) - 3) + 26))

        else:
            return (n)

def st_cezar(word):
    cezar_word = ""

    for i in word:
        cezar_word += cezar(i)

    return cezar_word

def un_st_cezar(word):
    uncezar_word = ""

    for i in word:
        uncezar_word += uncezar(i)

    return uncezar_word

def file():
    try:
        with open('source.txt', 'r') as data:
            for i in data:
                return (st_cezar(i))
    except:
        print("Nincs fájl.")

    return None

print(file())