''' This Function takes on the month and time of day.
It returns a corrections value for fuel moisture.
'''


def dfm(month, time, aspect, slope, shade):
    # Default corrections are for S aspect, 0% slope, level, and unshaded
    # These tables are the possible corrections values
    # Table b is for May - July
    table_b_n = [
        [3, 4, 5],
        [1, 2, 4],
        [0, 1, 3],
        [0, 1, 3],
        [1, 2, 4],
        [3, 4, 5]
    ]
    table_b_e = [
        [2, 4],
        [1, 0, 4],
        [0, 3],
        [0, 1, 4],
        [1, 3, 4],
        [4, 5]
    ]
    table_b_s = [
        [3, 4],
        [1, 4],
        [0, 1, 3],
        [0, 1, 3],
        [1, 4],
        [3, 5]
    ]
    table_b_w = [
        [3, 5],
        [1, 3, 4],
        [0, 1, 3],
        [0, 3],
        [1, 0, 4],
        [3, 2, 4]
    ]
    # Table c is for February - April and August - October
    table_c_n = [
        [4, 5],
        [2, 3, 5],
        [1, 3, 4],
        [1, 3, 4],
        [2, 3, 5],
        [4, 5]
    ]
    table_c_e = [
        [4, 3, 5],
        [2, 1, 4],
        [1, 4],
        [1, 2, 4],
        [2, 4, 5],
        [4, 5]
    ]
    table_c_s = [
        [4, 5],
        [2, 4],
        [1, 4],
        [1, 4],
        [2, 4],
        [4, 5]
    ]
    table_c_w = [
        [4, 5],
        [2, 4, 5],
        [1, 2, 4],
        [1, 4],
        [2, 1, 4],
        [4, 3, 5]
    ]
    # Table D is for November - January
    table_d_n = [
        [5],
        [4, 5],
        [3, 5],
        [3, 5],
        [4, 5],
        [5]
    ]
    table_d_e = [
        [5],
        [4, 3, 5],
        [3, 2, 5],
        [3, 4, 5],
        [4, 5],
        [5]
    ]
    table_d_s = [
        [5],
        [4, 3, 5],
        [3, 1, 5],
        [2, 1, 5],
        [4, 3, 5],
        [5]
    ]
    table_d_w = [
        [5],
        [4, 5],
        [3, 4, 5],
        [3, 2, 5],
        [4, 3, 5],
        [5]
    ]
    # Months are assigned numerical values
    if shade == False:
        if 0 <= slope <= 30:
            if 5 <= month <= 7:
                if aspect == "N":
                    if 800 <= time <= 959:
                        return table_b_n[0][0]
                    elif 1000 <= time <= 1159:
                        return table_b_n[1][0]
                    elif 1200 <= time <= 1359:
                        return table_b_n[2][0]
                    elif 1400 <= time <= 1559:
                        return table_b_n[3][0]
                    elif 1600 <= time <= 1759:
                        return table_b_n[4][0]
                    elif 1800 <= time <= 1959:
                        return table_b_n[5][0]
                    else:
                        return 0
                elif aspect == "E":
                    if 800 <= time <= 959:
                        return table_b_e[0][0]
                    elif 1000 <= time <= 1159:
                        return table_b_e[1][0]
                    elif 1200 <= time <= 1359:
                        return table_b_e[2][0]
                    elif 1400 <= time <= 1559:
                        return table_b_e[3][0]
                    elif 1600 <= time <= 1759:
                        return table_b_e[4][0]
                    elif 1800 <= time <= 1959:
                        return table_b_e[5][0]
                    else:
                        return 0
                elif aspect == "S":
                    if 800 <= time <= 959:
                        return table_b_s[0][0]
                    elif 1000 <= time <= 1159:
                        return table_b_s[1][0]
                    elif 1200 <= time <= 1359:
                        return table_b_s[2][0]
                    elif 1400 <= time <= 1559:
                        return table_b_s[3][0]
                    elif 1600 <= time <= 1759:
                        return table_b_s[4][0]
                    elif 1800 <= time <= 1959:
                        return table_b_s[5][0]
                    else:
                        return 0
                elif aspect == "W":
                    if 800 <= time <= 959:
                        return table_b_w[0][0]
                    elif 1000 <= time <= 1159:
                        return table_b_w[1][0]
                    elif 1200 <= time <= 1359:
                        return table_b_w[2][0]
                    elif 1400 <= time <= 1559:
                        return table_b_w[3][0]
                    elif 1600 <= time <= 1759:
                        return table_b_w[4][0]
                    elif 1800 <= time <= 1959:
                        return table_b_w[5][0]
                    else:
                        return 0
            elif 2 <= month <= 4 or 8 <= month <= 10:
                if aspect == "N":
                    if 800 <= time <= 959:
                        return table_c_n[0][0]
                    elif 1000 <= time <= 1159:
                        return table_c_n[1][0]
                    elif 1200 <= time <= 1359:
                        return table_c_n[2][0]
                    elif 1400 <= time <= 1559:
                        return table_c_n[3][0]
                    elif 1600 <= time <= 1759:
                        return table_c_n[4][0]
                    elif 1800 <= time <= 1959:
                        return table_c_n[5][0]
                    else:
                        return 0
                elif aspect == "E":
                    if 800 <= time <= 959:
                        return table_c_e[0][0]
                    elif 1000 <= time <= 1159:
                        return table_c_e[1][0]
                    elif 1200 <= time <= 1359:
                        return table_c_e[2][0]
                    elif 1400 <= time <= 1559:
                        return table_c_e[3][0]
                    elif 1600 <= time <= 1759:
                        return table_c_e[4][0]
                    elif 1800 <= time <= 1959:
                        return table_c_e[5][0]
                    else:
                        return 0
                elif aspect == "S":
                    if 800 <= time <= 959:
                        return table_c_s[0][0]
                    elif 1000 <= time <= 1159:
                        return table_c_s[1][0]
                    elif 1200 <= time <= 1359:
                        return table_c_s[2][0]
                    elif 1400 <= time <= 1559:
                        return table_c_s[3][0]
                    elif 1600 <= time <= 1759:
                        return table_c_s[4][0]
                    elif 1800 <= time <= 1959:
                        return table_c_s[5][0]
                    else:
                        return 0
                elif aspect == "W":
                    if 800 <= time <= 959:
                        return table_c_w[0][0]
                    elif 1000 <= time <= 1159:
                        return table_c_w[1][0]
                    elif 1200 <= time <= 1359:
                        return table_c_w[2][0]
                    elif 1400 <= time <= 1559:
                        return table_c_w[3][0]
                    elif 1600 <= time <= 1759:
                        return table_c_w[4][0]
                    elif 1800 <= time <= 1959:
                        return table_c_w[5][0]
                    else:
                        return 0
            elif month == 1 or month == 11 or month == 12:
                if aspect == "N":
                    if 800 <= time <= 959:
                        return table_d_n[0][0]
                    elif 1000 <= time <= 1159:
                        return table_d_n[1][0]
                    elif 1200 <= time <= 1359:
                        return table_d_n[2][0]
                    elif 1400 <= time <= 1559:
                        return table_d_n[3][0]
                    elif 1600 <= time <= 1759:
                        return table_d_n[4][0]
                    elif 1800 <= time <= 1959:
                        return table_d_n[5][0]
                    else:
                        return 0
                elif aspect == "E":
                    if 800 <= time <= 959:
                        return table_d_e[0][0]
                    elif 1000 <= time <= 1159:
                        return table_d_e[1][0]
                    elif 1200 <= time <= 1359:
                        return table_d_e[2][0]
                    elif 1400 <= time <= 1559:
                        return table_d_e[3][0]
                    elif 1600 <= time <= 1759:
                        return table_d_e[4][0]
                    elif 1800 <= time <= 1959:
                        return table_d_e[5][0]
                    else:
                        return 0
                elif aspect == "S":
                    if 800 <= time <= 959:
                        return table_d_s[0][0]
                    elif 1000 <= time <= 1159:
                        return table_d_s[1][0]
                    elif 1200 <= time <= 1359:
                        return table_d_s[2][0]
                    elif 1400 <= time <= 1559:
                        return table_d_s[3][0]
                    elif 1600 <= time <= 1759:
                        return table_d_s[4][0]
                    elif 1800 <= time <= 1959:
                        return table_d_s[5][0]
                    else:
                        return 0
                elif aspect == "W":
                    if 800 <= time <= 959:
                        return table_d_w[0][0]
                    elif 1000 <= time <= 1159:
                        return table_d_w[1][0]
                    elif 1200 <= time <= 1359:
                        return table_d_w[2][0]
                    elif 1400 <= time <= 1559:
                        return table_d_w[3][0]
                    elif 1600 <= time <= 1759:
                        return table_d_w[4][0]
                    elif 1800 <= time <= 1959:
                        return table_d_w[5][0]
                    else:
                        return 0
            else:
                return 0
        elif slope > 30:
            if 5 <= month <= 7:
                if aspect == "N":
                    if 800 <= time <= 959:
                        return table_b_n[0][1]
                    elif 1000 <= time <= 1159:
                        return table_b_n[1][1]
                    elif 1200 <= time <= 1359:
                        return table_b_n[2][1]
                    elif 1400 <= time <= 1559:
                        return table_b_n[3][1]
                    elif 1600 <= time <= 1759:
                        return table_b_n[4][1]
                    elif 1800 <= time <= 1959:
                        return table_b_n[5][1]
                    else:
                        return 0
                elif aspect == "E":
                    if 800 <= time <= 959:
                        return table_b_e[0][0]
                    elif 1000 <= time <= 1159:
                        return table_b_e[1][1]
                    elif 1200 <= time <= 1359:
                        return table_b_e[2][0]
                    elif 1400 <= time <= 1559:
                        return table_b_e[3][1]
                    elif 1600 <= time <= 1759:
                        return table_b_e[4][1]
                    elif 1800 <= time <= 1959:
                        return table_b_e[5][1]
                    else:
                        return 0
                elif aspect == "S":
                    if 800 <= time <= 959:
                        return table_b_s[0][0]
                    elif 1000 <= time <= 1159:
                        return table_b_s[1][0]
                    elif 1200 <= time <= 1359:
                        return table_b_s[2][1]
                    elif 1400 <= time <= 1559:
                        return table_b_s[3][1]
                    elif 1600 <= time <= 1759:
                        return table_b_s[4][0]
                    elif 1800 <= time <= 1959:
                        return table_b_s[5][0]
                    else:
                        return 0
                elif aspect == "W":
                    if 800 <= time <= 959:
                        return table_b_w[0][1]
                    elif 1000 <= time <= 1159:
                        return table_b_w[1][1]
                    elif 1200 <= time <= 1359:
                        return table_b_w[2][1]
                    elif 1400 <= time <= 1559:
                        return table_b_w[3][0]
                    elif 1600 <= time <= 1759:
                        return table_b_w[4][1]
                    elif 1800 <= time <= 1959:
                        return table_b_w[5][1]
                    else:
                        return 0
            elif 2 <= month <= 4 or 8 <= month <= 10:
                if aspect == "N":
                    if 800 <= time <= 959:
                        return table_c_n[0][0]
                    elif 1000 <= time <= 1159:
                        return table_c_n[1][1]
                    elif 1200 <= time <= 1359:
                        return table_c_n[2][1]
                    elif 1400 <= time <= 1559:
                        return table_c_n[3][1]
                    elif 1600 <= time <= 1759:
                        return table_c_n[4][1]
                    elif 1800 <= time <= 1959:
                        return table_c_n[5][0]
                    else:
                        return 0
                elif aspect == "E":
                    if 800 <= time <= 959:
                        return table_c_e[0][1]
                    elif 1000 <= time <= 1159:
                        return table_c_e[1][1]
                    elif 1200 <= time <= 1359:
                        return table_c_e[2][0]
                    elif 1400 <= time <= 1559:
                        return table_c_e[3][1]
                    elif 1600 <= time <= 1759:
                        return table_c_e[4][1]
                    elif 1800 <= time <= 1959:
                        return table_c_e[5][1]
                    else:
                        return 0
                elif aspect == "S":
                    if 800 <= time <= 959:
                        return table_c_s[0][0]
                    elif 1000 <= time <= 1159:
                        return table_c_s[1][0]
                    elif 1200 <= time <= 1359:
                        return table_c_s[2][0]
                    elif 1400 <= time <= 1559:
                        return table_c_s[3][0]
                    elif 1600 <= time <= 1759:
                        return table_c_s[4][0]
                    elif 1800 <= time <= 1959:
                        return table_c_s[5][0]
                    else:
                        return 0
                elif aspect == "W":
                    if 800 <= time <= 959:
                        return table_c_w[0][1]
                    elif 1000 <= time <= 1159:
                        return table_c_w[1][1]
                    elif 1200 <= time <= 1359:
                        return table_c_w[2][1]
                    elif 1400 <= time <= 1559:
                        return table_c_w[3][0]
                    elif 1600 <= time <= 1759:
                        return table_c_w[4][1]
                    elif 1800 <= time <= 1959:
                        return table_c_w[5][1]
                    else:
                        return 0
            elif month == 1 or month == 11 or month == 12:
                if aspect == "N":
                    if 800 <= time <= 959:
                        return table_d_n[0][0]
                    elif 1000 <= time <= 1159:
                        return table_d_n[1][1]
                    elif 1200 <= time <= 1359:
                        return table_d_n[2][1]
                    elif 1400 <= time <= 1559:
                        return table_d_n[3][1]
                    elif 1600 <= time <= 1759:
                        return table_d_n[4][1]
                    elif 1800 <= time <= 1959:
                        return table_d_n[5][0]
                    else:
                        return 0
                elif aspect == "E":
                    if 800 <= time <= 959:
                        return table_d_e[0][0]
                    elif 1000 <= time <= 1159:
                        return table_d_e[1][1]
                    elif 1200 <= time <= 1359:
                        return table_d_e[2][1]
                    elif 1400 <= time <= 1559:
                        return table_d_e[3][1]
                    elif 1600 <= time <= 1759:
                        return table_d_e[4][1]
                    elif 1800 <= time <= 1959:
                        return table_d_e[5][0]
                    else:
                        return 0
                elif aspect == "S":
                    if 800 <= time <= 959:
                        return table_d_s[0][0]
                    elif 1000 <= time <= 1159:
                        return table_d_s[1][1]
                    elif 1200 <= time <= 1359:
                        return table_d_s[2][1]
                    elif 1400 <= time <= 1559:
                        return table_d_s[3][1]
                    elif 1600 <= time <= 1759:
                        return table_d_s[4][1]
                    elif 1800 <= time <= 1959:
                        return table_d_s[5][0]
                    else:
                        return 0
                elif aspect == "W":
                    if 800 <= time <= 959:
                        return table_d_w[0][0]
                    elif 1000 <= time <= 1159:
                        return table_d_w[1][1]
                    elif 1200 <= time <= 1359:
                        return table_d_w[2][1]
                    elif 1400 <= time <= 1559:
                        return table_d_w[3][1]
                    elif 1600 <= time <= 1759:
                        return table_d_w[4][1]
                    elif 1800 <= time <= 1959:
                        return table_d_w[5][0]
                    else:
                        return 0
            else:
                return 0
        else:
            return 0
    elif shade == True:
        if 5 <= month <= 7:
            if aspect == "N":
                if 800 <= time <= 959:
                    return table_b_n[0][2]
                elif 1000 <= time <= 1159:
                    return table_b_n[1][2]
                elif 1200 <= time <= 1359:
                    return table_b_n[2][2]
                elif 1400 <= time <= 1559:
                    return table_b_n[3][2]
                elif 1600 <= time <= 1759:
                    return table_b_n[4][2]
                elif 1800 <= time <= 1959:
                    return table_b_n[5][2]
                else:
                    return 0
            elif aspect == "E":
                if 800 <= time <= 959:
                    return table_b_e[0][1]
                elif 1000 <= time <= 1159:
                    return table_b_e[1][2]
                elif 1200 <= time <= 1359:
                    return table_b_e[2][1]
                elif 1400 <= time <= 1559:
                    return table_b_e[3][2]
                elif 1600 <= time <= 1759:
                    return table_b_e[4][2]
                elif 1800 <= time <= 1959:
                    return table_b_e[5][1]
                else:
                    return 0
            elif aspect == "S":
                if 800 <= time <= 959:
                    return table_b_s[0][1]
                elif 1000 <= time <= 1159:
                    return table_b_s[1][1]
                elif 1200 <= time <= 1359:
                    return table_b_s[2][2]
                elif 1400 <= time <= 1559:
                    return table_b_s[3][2]
                elif 1600 <= time <= 1759:
                    return table_b_s[4][1]
                elif 1800 <= time <= 1959:
                    return table_b_s[5][1]
                else:
                    return 0
            elif aspect == "W":
                if 800 <= time <= 959:
                    return table_b_w[0][1]
                elif 1000 <= time <= 1159:
                    return table_b_w[1][2]
                elif 1200 <= time <= 1359:
                    return table_b_w[2][2]
                elif 1400 <= time <= 1559:
                    return table_b_w[3][1]
                elif 1600 <= time <= 1759:
                    return table_b_w[4][2]
                elif 1800 <= time <= 1959:
                    return table_b_w[5][2]
                else:
                    return 0
        elif 2 <= month <= 4 or 8 <= month <= 10:
            if aspect == "N":
                if 800 <= time <= 959:
                    return table_c_n[0][1]
                elif 1000 <= time <= 1159:
                    return table_c_n[1][2]
                elif 1200 <= time <= 1359:
                    return table_c_n[2][2]
                elif 1400 <= time <= 1559:
                    return table_c_n[3][2]
                elif 1600 <= time <= 1759:
                    return table_c_n[4][2]
                elif 1800 <= time <= 1959:
                    return table_c_n[5][1]
                else:
                    return 0
            elif aspect == "E":
                if 800 <= time <= 959:
                    return table_c_e[0][2]
                elif 1000 <= time <= 1159:
                    return table_c_e[1][2]
                elif 1200 <= time <= 1359:
                    return table_c_e[2][1]
                elif 1400 <= time <= 1559:
                    return table_c_e[3][2]
                elif 1600 <= time <= 1759:
                    return table_c_e[4][2]
                elif 1800 <= time <= 1959:
                    return table_c_e[5][1]
                else:
                    return 0
            elif aspect == "S":
                if 800 <= time <= 959:
                    return table_c_s[0][1]
                elif 1000 <= time <= 1159:
                    return table_c_s[1][1]
                elif 1200 <= time <= 1359:
                    return table_c_s[2][1]
                elif 1400 <= time <= 1559:
                    return table_c_s[3][1]
                elif 1600 <= time <= 1759:
                    return table_c_s[4][1]
                elif 1800 <= time <= 1959:
                    return table_c_s[5][1]
                else:
                    return 0
            elif aspect == "W":
                if 800 <= time <= 959:
                    return table_c_w[0][1]
                elif 1000 <= time <= 1159:
                    return table_c_w[1][2]
                elif 1200 <= time <= 1359:
                    return table_c_w[2][2]
                elif 1400 <= time <= 1559:
                    return table_c_w[3][1]
                elif 1600 <= time <= 1759:
                    return table_c_w[4][2]
                elif 1800 <= time <= 1959:
                    return table_c_w[5][2]
                else:
                    return 0
        elif month == 1 or month == 11 or month == 12:
            if aspect == "N":
                if 800 <= time <= 959:
                    return table_d_n[0][0]
                elif 1000 <= time <= 1159:
                    return table_d_n[1][1]
                elif 1200 <= time <= 1359:
                    return table_d_n[2][1]
                elif 1400 <= time <= 1559:
                    return table_d_n[3][1]
                elif 1600 <= time <= 1759:
                    return table_d_n[4][1]
                elif 1800 <= time <= 1959:
                    return table_d_n[5][0]
                else:
                    return 0
            elif aspect == "E":
                if 800 <= time <= 959:
                    return table_d_e[0][0]
                elif 1000 <= time <= 1159:
                    return table_d_e[1][2]
                elif 1200 <= time <= 1359:
                    return table_d_e[2][2]
                elif 1400 <= time <= 1559:
                    return table_d_e[3][2]
                elif 1600 <= time <= 1759:
                    return table_d_e[4][1]
                elif 1800 <= time <= 1959:
                    return table_d_e[5][0]
                else:
                    return 0
            elif aspect == "S":
                if 800 <= time <= 959:
                    return table_d_s[0][0]
                elif 1000 <= time <= 1159:
                    return table_d_s[1][2]
                elif 1200 <= time <= 1359:
                    return table_d_s[2][2]
                elif 1400 <= time <= 1559:
                    return table_d_s[3][2]
                elif 1600 <= time <= 1759:
                    return table_d_s[4][2]
                elif 1800 <= time <= 1959:
                    return table_d_s[5][0]
                else:
                    return 0
            elif aspect == "W":
                if 800 <= time <= 959:
                    return table_d_w[0][0]
                elif 1000 <= time <= 1159:
                    return table_d_w[1][1]
                elif 1200 <= time <= 1359:
                    return table_d_w[2][2]
                elif 1400 <= time <= 1559:
                    return table_d_w[3][2]
                elif 1600 <= time <= 1759:
                    return table_d_w[4][2]
                elif 1800 <= time <= 1959:
                    return table_d_w[5][0]
                else:
                    return 0
        else:
            return 0
    else:
        return 0
