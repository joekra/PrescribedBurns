''' This function takes in the time of day, rh, and dry bulb
temperature. It returns a reference fuel moisture value based on rh
and temperature.
'''


def rfm(time, rh, temp):
    # reference fuel moisture can only be calculated between 0800-1959
    # return 0 is added at the end of if statements in the case of an error
    if 800 <= time <= 1959:
        if 0 <= rh <= 4:
            return 1
        elif 5 <= rh <= 9:
            if 10 <= temp <= 69:
                return 2
            elif 70 <= temp:
                return 1
            else:
                return 0
        elif 10 <= rh <= 14:
            return 2
        elif 15 <= rh <= 19:
            if 10 <= temp <= 69:
                return 3
            elif 70 <= temp:
                return 2
            else:
                return 0
        elif 20 <= rh <= 24:
            if 10 <= temp <= 69:
                return 4
            elif 70 <= temp:
                return 3
            else:
                return 0
        elif 25 <= rh <= 29:
            if 10 <= temp <= 69:
                return 5
            elif 70 <= temp:
                return 4
            else:
                return 0
        elif 30 <= rh <= 34:
            if 10 <= temp <= 89:
                return 5
            elif 90 <= temp:
                return 4
            else:
                return 0
        elif 35 <= rh <= 39:
            if 10 <= temp <= 69:
                return 6
            elif 70 <= temp:
                return 5
            else:
                return 0
        elif 40 <= rh <= 44:
            if 10 <= temp <= 49:
                return 7
            elif 50 <= temp:
                return 6
            else:
                return 0
        elif 45 <= rh <= 54:
            if 10 <= temp <= 29:
                return 8
            elif 30 <= temp:
                return 7
            else:
                return 0
        elif 55 <= rh <= 59:
            return 8
        elif 60 <= rh <= 64:
            if 10 <= temp <= 49:
                return 9
            elif 50 <= temp:
                return 8
            else:
                return 0
        elif 65 <= rh <= 69:
            if 10 <= temp <= 69:
                return 9
            elif 70 <= temp:
                return 8
            else:
                return 0
        elif 70 <= rh <= 74:
            if 10 <= temp <= 49:
                return 10
            elif 50 <= temp:
                return 9
            else:
                return 0
        elif 75 <= rh <= 79:
            if 10 <= temp <= 29:
                return 11
            elif 30 <= temp:
                return 10
            else:
                return 0
        elif 80 <= rh <= 84:
            if 10 <= temp <= 29:
                return 12
            elif 30 <= temp <= 69:
                return 11
            elif 70 <= temp:
                return 10
            else:
                return 0
        elif 85 <= rh <= 89:
            if 10 <= temp <= 69:
                return 12
            elif 70 <= temp:
                return 11
            else:
                return 0
        elif 90 <= rh <= 99:
            if 10 <= temp <= 49:
                return 13
            elif 50 <= temp:
                return 12
            else:
                return 0
        elif rh == 100:
            if 10 <= temp <= 29:
                return 14
            elif 30 <= temp <= 109:
                return 13
            elif 110 <= temp:
                return 12
            else:
                return 0
        else:
            return 0
    else:
        return 0
