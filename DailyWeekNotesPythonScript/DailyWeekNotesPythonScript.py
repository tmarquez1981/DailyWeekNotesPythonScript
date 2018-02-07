from datetime import date, datetime, timedelta
import calendar
import os
from pathlib import Path

#class DailyNotes:

def main():

    #################### set the contents of the daily text file ###########
    #gets todays date
    now = date.today()
    #print(now)

    contents = now.strftime('%m/%d/%Y') + '\n' + '\n' + 'TASKS:' + '\n' + '\n' + 'OUTCOME:'

    #print(contents)

    ################## finish text file ####################################

    #find the directory text file will be placed
    #based on the current week ending date
    day = now.strftime('%b/%d/%Y')
    dt = datetime.strptime(day, '%b/%d/%Y')
    start = dt - timedelta(days=dt.weekday())
    end = start + timedelta(days=5) 
    week_end_date = end.strftime('%b%d') 

    #the string for the directories name
    week_end_date_str = 'WE_' + week_end_date

    #write file
    #first, check if the current directory for week ending has been created
    #path of weekly directories = \\itfs01\home\marquez_thomas\Desktop\Notes\Weekly_Work_Notes
    parent_path = Path(__file__).parents[2]

    #concatenate directory of weekly folders and this current week ending
    path_of_week = os.path.join(parent_path, week_end_date_str)

    is_path = False

    #loop through directories to see if the current week ending directory has already been created
    for f in os.listdir(parent_path):
        if f == week_end_date_str:
            is_path = True
        
    #if current week ending folder has not been created, create it
    if not is_path:
        #os.makedirs(week_end_date_str)
        os.makedirs(path_of_week)

    #if current week is already created, get the path
    current_week_path = os.path.join(parent_path, week_end_date_str)

    #gets the day of the week
    day_of_week = calendar.day_name[now.weekday()]

    #if day of week is not Saturday or Sunday
    if day_of_week != 'Saturday' or day_of_week != 'Sunday':

        #name of text file
        name_of_file = day_of_week + '.txt'

        #complete file name
        completeName = os.path.join(current_week_path, name_of_file)

        #finally, write the file if file has not been created
 
        file = open(completeName, "w")
        file.write(contents)
        file.close

if __name__ == "__main__":
    main()

