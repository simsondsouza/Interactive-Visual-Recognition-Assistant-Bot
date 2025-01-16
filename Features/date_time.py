import datetime #inbuilt module in python and it works on date and time

def day(): #Function to tell Day of the week
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        try:
            day_of_the_week = Day_dict[day]
        except Exception as e:
            print(e)
            day_of_the_week = "Didn't Hear you, can you say again"
        return day_of_the_week

def date():
    try:
        date = datetime.datetime.now().strftime("%b %d %Y")
    except Exception as e:
        print(e)
        date = "Didn't Hear you, can you say again"
    return date


def time():
    try:
        time = str(datetime.datetime.now())
        hour = time[11:13]
        min = time[14:16]
        time = "The time is " + hour + "Hours and" + min + "Minutes"
    except Exception as e:
        print(e)
        time = "Didn't Hear you, can you say again"
    return time