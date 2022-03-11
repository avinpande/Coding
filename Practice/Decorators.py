def search(text):
    return text.lower()


def decorate(text):
    return text.upper()


def beautify(func):
    beaut_text = func('Hi, Avinash here')
    print(beaut_text)


def create_adder(x):
    print('In create adder')

    def adder(y):
        print('in adder')
        return x + y

    return adder


add_15 = create_adder(15)
print(add_15(10))
change = beautify
change(search)
change(decorate)
