''' This function takes in fdfm and dry bulb temperature.
It then goes to the matching fdfm and based on the temperature
it returns pig.
'''


def pig(fdfm, temp):
    if fdfm == 2:
        if temp >= 70:
            return 100
        elif 40 <= temp < 70:
            return 90
        elif 30 <= temp < 40:
            return 80
        else:
            return 0
    elif fdfm == 3:
        if temp >= 110:
            return 100
        elif 80 <= temp < 110:
            return 90
        elif 40 <= temp < 80:
            return 80
        elif 30 <= temp < 40:
            return 70
        else:
            return 0
    elif fdfm == 4:
        if temp >= 80:
            return 80
        elif 40 <= temp < 80:
            return 70
        elif 30 <= temp < 40:
            return 60
        else:
            return 0
    elif fdfm == 5:
        if temp >= 80:
            return 70
        elif 40 <= temp < 80:
            return 60
        elif 30 <= temp < 40:
            return 50
        else:
            return 0
    elif fdfm == 6:
        if temp >= 70:
            return 60
        elif 30 <= temp < 70:
            return 50
        else:
            return 0
    elif fdfm == 7:
        if temp >= 100:
            return 60
        elif 60 <= temp < 100:
            return 50
        elif 30 <= temp < 60:
            return 40
        else:
            return 0
    elif fdfm == 8:
        if temp >= 100:
            return 50
        elif 40 <= temp < 100:
            return 40
        elif 30 <= temp < 40:
            return 30
        else:
            return 0
    elif fdfm == 9:
        if temp >= 70:
            return 40
        elif 30 <= temp < 70:
            return 30
        else:
            return 0
    elif fdfm == 10:
        if temp >= 100:
            return 40
        elif 50 <= temp < 100:
            return 30
        elif 30 <= temp < 50:
            return 20
        else:
            return 0
    elif fdfm == 11:
        if temp >= 70:
            return 30
        elif 30 <= temp < 70:
            return 20
        else:
            return 0
    elif fdfm == 12:
        if temp >= 90:
            return 30
        elif 30 <= temp < 90:
            return 20
        else:
            return 0
    elif fdfm == 13:
        if temp >= 40:
            return 20
        elif 30 <= temp < 40:
            return 10
        else:
            return 0
    elif fdfm == 14:
        if temp >= 60:
            return 20
        elif 30 <= temp < 60:
            return 10
        else:
            return 0
    elif fdfm == 15:
        if temp >= 90:
            return 20
        elif 30 <= temp < 90:
            return 10
        else:
            return 0
    elif fdfm == 16:
        if temp >= 110:
            return 20
        elif 30 <= temp < 110:
            return 10
        else:
            return 0
    elif fdfm == 17:
        if temp >= 30:
            return 100
        else:
            return 0
    else:
        return 0
