import pyexcel, statistics, os, shutil, numpy
from datetime import datetime, timedelta




# def convert_to_wsl_path(win_path):                                                          #function to convert Windows file path to WSL filepath                                                                                               
#     win_path = win_path.strip('"')
#     return os.popen(f"wslpath '{win_path}'").read().strip()
# source_win_data = input("Enter the source data filepath: ")                                 #convert source 
# destination_win_folder = input("Enter the destination folder path: ")
# source_data = convert_to_wsl_path(source_win_data) 
# destination_folder = convert_to_wsl_path(destination_win_folder)\\\

source_data = "docs/input/OSCAR_seb_Details_2023-06-26_2025-03-08.csv"
destination_folder = "docs/output/"


flow_data = pyexcel.get_records(file_name=f"{source_data}")                                       #assign file data to variable

date_set = set()                                                                    #define list of ordered dict for given range
flow_data_set = []

for row in flow_data:                                                                      #identify unique dates in detail report                                                                                   
    event = f"{row["Event"]}"
    date_col = f"{row["DateTime"]}"
    date = date_col[0:10]
    time = date_col[10:]
    if event == "FLG": 
        date_set.add(date)




date_list = list(date_set)                                                                  #convert set to list to conserve order
date_list.sort()
dates = [[date] for date in date_list]



for date in dates:                                                                          #analyze/generate report
    FL_total = 0
    FL_list = []
    time_stamps = []
    FL_durations = []
    total_FL_time = 0
    FL_nonzero = []
    FL_0_05 = 0
    FL_05_1 = 0
    FL_1_15 = 0
    FL_15_2 = 0
    FL_2_25 = 0
    FL_25_3 = 0
    FL_3_35 = 0
    FL_35_4 = 0
    FL_4_45 = 0
    FL_45_5 = 0
    FL_5_55 = 0
    FL_55_6 = 0
    FL_6_65 = 0
    FL_65_7 = 0
    FL_7_75 = 0
    FL_75_8 = 0
    FL_8_85 = 0
    FL_85_9 = 0
    FL_9_95 = 0
    FL_95_1 = 0

    for row in flow_data:
        flow_entry = f"{row["Data/Duration"]}"  
        date_col = f"{row["DateTime"]}"  
        date_entry = date_col[0:10]
        event = f"{row["Event"]}"
        time_format = "%H:%M:%S"
        time = datetime.strptime((date_col[11:]), time_format)
        if event == "FLG":
            if date[0] == date_entry:
                FL_list.append(flow_entry)
                time_stamps.append(time)
                if float(flow_entry) == 0:
                    FL_total += 1
    for i in range(len(time_stamps)-1):
        time1 = time_stamps[i]
        time2 = time_stamps[i+1]
        FL_time = time2 - time1
        FL_time_int = int(FL_time.total_seconds())
        if float(FL_list[i]) > 0 and float(FL_list[i]) <= 0.05:
            FL_0_05 += FL_time_int
        if float(FL_list[i]) > 0.05 and float(FL_list[i]) <= 0.1:
            FL_05_1 += FL_time_int     
        if float(FL_list[i]) > 0.1 and float(FL_list[i]) <= 0.15:
            FL_1_15 += FL_time_int 
        if float(FL_list[i]) > 0.15 and float(FL_list[i]) <= 0.2:
            FL_15_2 += FL_time_int 
        if float(FL_list[i]) > 0.2 and float(FL_list[i]) <= 0.25:
            FL_2_25 += FL_time_int 
        if float(FL_list[i]) > 0.25 and float(FL_list[i]) <= 0.3:
            FL_25_3 += FL_time_int 
        if float(FL_list[i]) > 0.3 and float(FL_list[i]) <= 0.35:
            FL_3_35 += FL_time_int 
        if float(FL_list[i]) > 0.35 and float(FL_list[i]) <= 0.4:
            FL_35_4 += FL_time_int 
        if float(FL_list[i]) > 0.4 and float(FL_list[i]) <= 0.45:
            FL_4_45 += FL_time_int 
        if float(FL_list[i]) > 0.45 and float(FL_list[i]) <= 0.5:
            FL_45_5 += FL_time_int 
        if float(FL_list[i]) > 0.5 and float(FL_list[i]) <= 0.55:
            FL_5_55 += FL_time_int 
        if float(FL_list[i]) > 0.55 and float(FL_list[i]) <= 0.6:
            FL_55_6 += FL_time_int 
        if float(FL_list[i]) > 0.6 and float(FL_list[i]) <= 0.65:
            FL_6_65 += FL_time_int 
        if float(FL_list[i]) > 0.65 and float(FL_list[i]) <= 0.7:
            FL_65_7 += FL_time_int 
        if float(FL_list[i]) > 0.7 and float(FL_list[i]) <= 0.75:
            FL_7_75 += FL_time_int 
        if float(FL_list[i]) > 0.75 and float(FL_list[i]) <= 0.8:
            FL_75_8 += FL_time_int 
        if float(FL_list[i]) > 0.8 and float(FL_list[i]) <= 0.85:
            FL_8_85 += FL_time_int 
        if float(FL_list[i]) > 0.85 and float(FL_list[i]) <= 0.9:
            FL_85_9 += FL_time_int 
        if float(FL_list[i]) > 0.9 and float(FL_list[i]) <= 0.95:
            FL_9_95 += FL_time_int 
        if float(FL_list[i]) > 0.95 and float(FL_list[i]) <= 1:
            FL_95_1 += FL_time_int         
        if float(FL_list[i]) > 0:
            FL_nonzero.append(float(FL_list[i]))
            total_FL_time += FL_time_int


    sleep_seconds = (time_stamps[-1] - time_stamps[0]).total_seconds()
    total_FL = FL_total - 2
    sleep_hours = round((sleep_seconds/3600), 2)
    FL_portion = total_FL_time/sleep_seconds
    FL_perc = round((FL_portion * 100), 2)
    FL_average = round((sum(FL_nonzero)/len(FL_nonzero)), 3)
    FL_max = max(FL_nonzero)
    FL_median = statistics.median(FL_nonzero)
    FL_hour = round((total_FL/sleep_hours), 2)

    # FL_95 = numpy.percentile(FL_list, 95)

    date.extend([
        sleep_hours, total_FL, FL_perc, FL_hour, FL_max, FL_average, FL_median,
        round(FL_0_05/sleep_seconds, 2),
        round(FL_05_1/sleep_seconds, 2),
        round(FL_1_15/sleep_seconds, 2),
        round(FL_15_2/sleep_seconds, 2),
        round(FL_2_25/sleep_seconds, 2),
        round(FL_25_3/sleep_seconds, 2),
        round(FL_3_35/sleep_seconds, 2),
        round(FL_35_4/sleep_seconds, 2),
        round(FL_4_45/sleep_seconds, 2),
        round(FL_45_5/sleep_seconds, 2),
        round(FL_5_55/sleep_seconds, 2),
        round(FL_55_6/sleep_seconds, 2),
        round(FL_6_65/sleep_seconds, 2),
        round(FL_65_7/sleep_seconds, 2),
        round(FL_7_75/sleep_seconds, 2),
        round(FL_75_8/sleep_seconds, 2),
        round(FL_8_85/sleep_seconds, 2),
        round(FL_85_9/sleep_seconds, 2),
        round(FL_9_95/sleep_seconds, 2),
        round(FL_95_1/sleep_seconds, 2)])

dates_adjusted = []
for date in dates:
    date_adj = (datetime.strptime(date[0], "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    date[0] = date_adj

column_headings = ["Date", "Sleep Duration", "FL Events", "FL/Sleep", "FL/HR", "Max FL", "Avg. FL", "Median FL",     
    "0-.05",
    ".05-.1",
    ".1-.15", 
    ".15-2",
    ".2-.25",
    ".25-.3",
    ".3-.35",
    ".35-.4",
    ".4-.45",
    ".45-.5",
    ".5-.55",
    ".55-.6",
    ".6-.65",
    ".65-.7",
    ".7-.75",
    ".75-.8",
    ".8-.85",
    ".85-.9",
    ".9-.95",
    ".95-1.0"]

flow_report = dates
flow_report.insert(0, column_headings)
pyexcel.save_as(array=flow_report, dest_file_name="flow_limit_report.csv")
shutil.move("flow_limit_report.csv", destination_folder)    
print("Analysis complete. Your report has been sent to the destination folder.")