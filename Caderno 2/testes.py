def teste():
    num = 10

    a = 1/10 + 1/10 + 1/10
    b = (3/10)

    print(a == b)

def precisao():
    for x in [0.3, 0.33, 0.333, 0.3333, 0.33333, 0.333333, 0.3333333, 0.333333333]:
        print(f'3*{x}'.ljust(13,' '),'=', 3*x, sep=' ')
