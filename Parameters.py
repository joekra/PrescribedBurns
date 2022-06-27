'''This function takes is fdfm, pig, and wind speed and returns
a value 0-3. "0" means that the hour that the inputs come from
is a possible burning hour. A "1" means that it is too dry. A "2"
means that it is too wet. A "3" means that it's too windy.
'''
def param(fdfm, prob, wind):

    if 4 <= fdfm <= 6 and 30 <= prob <= 70 and wind <= 23:
        return 0
    elif fdfm > 6:
        return 1
    elif fdfm < 4:
        return 2
    elif wind > 23:
        return 3
