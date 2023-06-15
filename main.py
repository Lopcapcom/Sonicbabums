str = 'Там холм лохмат'
str = str.casefold()
rev = reversed(str)
if list(str) == list(rev):
    print('TRUE')
else:
    print('FALSE')
