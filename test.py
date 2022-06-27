from RFM import rfm
from DFM import dfm
from PIG import pig
from Parameters import param

burn_count = 0
burn_day = 0
too_wind = 0
too_dry = 0
too_wet = 0
burnt = False
next_day = 0
term_count = 0
wrong = False
repeat = True
enter = False
shade = False
# Loop repeats until user no longer wants to process a file

while repeat == True:
    # Opens file with name that was entered by the user
    raws = open(input(str("Enter name of the input file: ")) + ".csv", "r")
    burn = open(input(str("Enter name of the output file: ")) + ".csv", "w")

    while enter == False:
        print("Enter aspect (n,e,s, or w): ")
        aspect = str(input())
        if aspect != "n" and aspect != "s" and aspect != "e" and aspect != "w":
            enter = False
        else:
            enter = True
        print("Enter slope value as a whole number without the percent sign: ")
        slope = int(input())
    enter = False
    while enter == False:
        print("Enter shading (if shading is greater than 50%, enter 'y', if not, enter 'n'): ")
        s = str(input())
        enter = True
        if s != "y" and  s != "n":
            enter = False
        if s == "y":
            shade = True
    enter = False
    for line in raws:
        # Separates a line at the "," and puts values into a list
        f = line.split(",")
        # Ignore index 0 because it's the name of the station
        date = f[1]
        # Some lines have missing data, if it finds missing data
        # it replaces the blank index with 0 and essentially throws the line out
        if f[2] == "":
            f[2] = 0
            f[3] = 0
            f[4] = 0
        elif f[3] == "":
            f[2] = 0
            f[3] = 0
            f[4] = 0
        elif f[4] == "":
            f[2] = 0
            f[3] = 0
            f[4] = 0
        # Assigning variables values and converts from a string to a number
        temp = round(float(f[2]))
        rh = round(float(f[3]))
        wind = float(f[4])
        # Date currently hold a string formatted like "01/01/2018 00:20 MST"
        # This splits the date at the "/" and assigns the value to its corresponding variable
        for section in date:
            full_date = date.split("/")
            month = int(full_date[0])
            day = int(full_date[1])
            # This checks to make sure that there isn't more than one burn window in a day
            if day == next_day:
                burnt = False
            year_time = full_date[2]
            # year_time holds a string like "2018 00:20 MST"
            # This splits the string at the spaces to separate the year and time
            for part in year_time:
                yt = year_time.split(" ")
                year = int(yt[0])
                time = yt[1]
                # This gets rid of the ":" in the time and combines the hour and minute
            for num in time:
                half = time.split(":")
                hour = half[0]
                mint = half[1]
                clock = hour + mint
                clock = int(clock)
        next_day = day + 1
        ''' This section uses the imported functions to calculate the 
         reference fuel moisture; correction for month and time; fine dead
         fuel moisture; probability of ignition; and weather or not the 
         given hour meets the burn parameters.
        '''
        ref = rfm(clock, rh, temp)
        correction = dfm(month, clock, aspect, slope, shade)
        fdfm = ref + correction
        prob = pig(fdfm, temp)
        burn_hour = param(fdfm, prob, wind)
        ''' This section counts the number of consecutive hours that meet
        all of the parameters. When the counter reaches four and another burn
        window hasn't already been established, it adds one to the total; it 
        then searches for the next hour that fails to meet the parameters. 
        Once the next failing hour is found, it finds the reason it failed, 
        then counts the number of times a certain parameter has been the reason
        that a burn window has ended. The variable term_count keeps track of weather 
        or not a reason for termination has been found. When found term_count is set
        equal to 1 so that the reason for termination doesn't change. 
        '''
        if burn_hour == 0:
            burn_count = burn_count + 1
            if burn_count >= 4 and burnt == False:
                burn_day = burn_day + 1
                burnt = True
                burn_count = 0
                term_count = 0
        elif burn_hour == 1:
            if burnt == True and term_count == 0:
                too_dry = too_dry + 1
                term_count = 1
        elif burn_hour == 2:
            if burnt == True and term_count == 0:
                too_wet = too_wet + 1
                term_count = 1
        elif burn_hour == 3:
            if burnt == True and term_count == 0:
                too_wind = too_wind + 1
                term_count = 1
    # Output for the number of possible burn days and the reasons why
    # each burn window ended
    burn.write("Station: " + f[0] + "\n" + "Year: " + str(year) + "\n")
    burn.write("Days with 4+ hour burn window: " + str(burn_day) + "\n")
    burn.write("Burn window ended (wet): " + str(too_wet) + "\n")
    burn.write("Burn window ended (dry): " + str(too_dry) + "\n")
    burn.write("Burn window ended (wind): " + str(too_wind) + "\n")
    # Closes input and output files
    raws.close()
    burn.close()
    print("File processed successfully." + '\n')
    # While loop will repeat if the user wants to enter another file
    print("Do you want to use another file? Enter y/n: ")
    answer = input()
    if answer == "y":
        repeat = True
    elif answer == "n":
        repeat = False
    else:
        wrong = True
        # Checks to see if the user entered either a "y" or "n"
        while wrong == True:
            print("Unexpected response, please enter y/n: ")
            print("Do you want to use another file? Enter y/n: ")
            answer = input()
            if answer == "y":
                repeat = True
                break
            elif answer == "n":
                repeat = False
                break
