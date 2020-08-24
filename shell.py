from lib import pansy

while True:
    text = input('Pancy > ')

    if text == "q": break
    
    result, error = pansy.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)