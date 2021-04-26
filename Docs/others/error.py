"""
błędy w pythonie, jak sobie z nimi radzić
>>> https://docs.python.org/3/tutorial/errors.html

"""

while True:
    try:
        x = int(input('podaj int\n'))
        print('twój int:', x)
        break
    except ValueError:
        print('to nie int')

        