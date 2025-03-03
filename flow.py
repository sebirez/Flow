import pyexcel as p
import statistics
import os
import shutil

def convert_to_wsl_path(win_path):                                                          #function to convert Windows file path to WSL filepath                                                                                               
    win_path = win_path.strip('"')
    return os.popen(f"wslpath '{win_path}'").read().strip()

source_win_data = input("Enter the source data filepath: ")                                 #convert source 
destination_win_folder = input("Enter the destination folder path: ")
source_data = convert_to_wsl_path(source_win_data) 
destination_folder = convert_to_wsl_path(destination_win_folder)


flow_file = p.get_records(file_name=f"{source_data}")                                       #assign file data to variable
date_set = set()
flow_limit = flow_file                                                                      #define list of ordered dict for given range
flow_data_set = []

for row in flow_limit:                                                                      #identify unique dates in detail report                                                                                   
    event = f"{row["Event"]}"
    date_col = f"{row["DateTime"]}"
    date = date_col[0:10]
    if event == "FLG": 
        date_set.add(date)
date_list = list(date_set)                                                                  #convert set to list to conserve order
date_list.sort()
dates = [[date] for date in date_list]

for date in dates:                                                                          #analyze/generate report
    FL_total = 0
    FL_above_005 = 0
    FL_above_010 = 0
    FL_above_020 = 0
    FL_above_030 = 0
    FL_list = []
    for row in flow_limit:
        flow_entry = f"{row["Data/Duration"]}"  
        date_col = f"{row["DateTime"]}"  
        date_entry = date_col[0:10]
        event = f"{row["Event"]}"
        if event == "FLG":
            if date[0] == date_entry:
                if float(flow_entry) > 0:
                    FL_list.append(float(flow_entry))
                    FL_total += 1
                if float(flow_entry) > 0.05:
                    FL_above_005 += 1
                if float(flow_entry) > 0.10:
                    FL_above_010 += 1
                if float(flow_entry) > 0.20:
                    FL_above_020 += 1
                if float(flow_entry) > 0.30:
                    FL_above_030 += 1
    date.append(FL_total)
    date.append(FL_above_005)
    date.append(FL_above_010)
    date.append(FL_above_020)
    date.append(FL_above_030)

    if len(FL_list) > 0:
        FL_average = round((sum(FL_list)/len(FL_list)), 5)
        FL_max = max(FL_list)
        FL_median = statistics.median(FL_list)

        date.append(FL_average)
        date.append(FL_max)
        date.append(FL_median)

    else:
        FL_average = None
        FL_max = None
        FL_median = None
    
column_headings = ["Date", "Total", "Above 0.05", "Above 0.10", "Above 0.20", "Above 0.30", "Average", "Max", "Median"]
flow_report = dates
flow_report.insert(0, column_headings)
p.save_as(array=flow_report, dest_file_name="flow_data_report.ods")
shutil.move("flow_data_report.ods", destination_folder)    
print("Analysis complete. 'flow_data_report.ods' sent to your OSCAR folder.")