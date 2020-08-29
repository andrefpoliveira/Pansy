from lib import pansy

while True:
    text = input('Pansy> ')

    if text == "exit": break

    result, error = pansy.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print(repr(result))
