def search(text):
    return text.lower()


def decorate(text):
    return text.upper()


def beautify(func):
    beaut_text = func('Hi, Avinash here')
    print(beaut_text)


beautify(search)
beautify(decorate)
