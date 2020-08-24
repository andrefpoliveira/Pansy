from lib import pansy

while True:
    text = input('Pancy > ')
    result, error = pansy.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)