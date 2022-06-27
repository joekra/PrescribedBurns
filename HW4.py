import PySimpleGUI as sg
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
enter = False
shade = False

sg.theme("Tan Blue")  # change your theme

# All of the stuff inside of the window
layout = [
    # Organization of each element. Keys have been attempted to be added to each element in the hope that we may access them as a dictionary
    # in the if event statement in the while loop I have tried to print out or assign the 'key' but have gotten some weird results
    # I am trying to make the keys work so we can set the new variables = dictionary keys
    #

    [sg.Text('Select the input file:'), sg.FileBrowse("Upload File", size=(10, 2), key='upload_file')],
    [sg.Text('Enter the name of th output file:'), sg.InputText(size=(40, 100), key="file_write")],
    [sg.Text('What is the angle of the slope'),
     sg.Slider(range=(0, 100), default_value=0, size=(30, 20), orientation='horizontal', key="slope")],
    [sg.Text('Is the region have shaded? (Yes for grater than 50%):'), sg.Radio("Yes", 'Radio1', default=True),
     sg.Radio("No", 'Radio1', default=True), ],
    [sg.Text('Select aspect'), sg.Combo(['N', 'E', 'S', 'W'])],
    [sg.Button('Submit', size=(8, 1)), sg.Button("Cancel", size=(8, 1))]

]

# Create the window
window = sg.Window("Prescribed Burn Calculator", layout)

# Event loop to process the events and get the value of the inputs as values
while True:
    event, values = window.read()
    if event is None or event == "Cancel":
        break
    if event == "Submit":
        # variable = values dictionary with key
        raws = open(values['upload_file'], 'r')
        burn = open(values['file_write'] + ".csv", 'w')
        slope = values['slope']
        if values[0] == True:
            shade = True
        if values[1] == True:
            shade = False
        aspect = str(values[2])

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
    # Output for the number of possible burn days and the reasons how
    # each burn window ended
    burn.write("Station: " + f[0] + "\n" + "Year: " + str(year) + "\n")
    burn.write("Days with 4+ hour burn window: " + str(burn_day) + "\n")
    burn.write("Burn window ended (wet): " + str(too_wet) + "\n")
    burn.write("Burn window ended (dry): " + str(too_dry) + "\n")
    burn.write("Burn window ended (wind): " + str(too_wind) + "\n")
    # Closes input and output files
    raws.close()
    burn.close()
    # popup that presents the same information that was written to the output
    # file for easier viewing
    sg.Popup("Station: " + f[0] + "\n" + "Year: " + str(year),
             "Days with 4+ hour burn window: " + str(burn_day),
             "Burn window ended (wet): " + str(too_wet),
             "Burn window ended (dry): " + str(too_dry),
             "Burn window ended (wind): " + str(too_wind))


window.close()
