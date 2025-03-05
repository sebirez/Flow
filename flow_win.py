import pyexcel, statistics, os, shutil #numpy
from datetime import datetime, timedelta


# def convert_to_wsl_path(win_path):                                                          #function to convert Windows file path to WSL filepath                                                                                               
#     win_path = win_path.strip('"')
#     return os.popen(f"wslpath '{win_path}'").read().strip()

# source_win_data = input("Enter the source data filepath: ")                                 #convert source 
# destination_win_folder = input("Enter the destination folder path: ")

source_data = input("Enter the source data filepath: ")
destination_folder = input("Enter the destination folder path: ")

# source_data = "tests/FLG.csv"
# destination_folder = "/home/sebirez/workspace/github.com/sebirez/Flow/tests"


flow_file = pyexcel.get_records(file_name=f"{source_data}")                                       #assign file data to variable
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
    FL_average = round((sum(FL_list)/len(FL_list)), 5)
    #print(FL_list)
    FL_max = max(FL_list)
    FL_median = statistics.median(FL_list)
    #flow_95 = numpy.percentile(FL_list, 95)
    date.append(flow_95)
    date.append(FL_average)
    date.append(FL_max)
    date.append(FL_median)
    date.append(FL_total)
    date.append(FL_above_005)
    date.append(FL_above_010)
    date.append(FL_above_020)
    date.append(FL_above_030)

dates_adjusted = []
for date in dates:
    date_adj = (datetime.strptime(date[0], "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
    date[0] = date_adj

column_headings = ["Date", "Average", "Max", "Median", "Total #", "# > 0.05", "# > 0.10", "# > 0.20", "# > 0.30"]


flow_report = dates
flow_report.insert(0, column_headings)
pyexcel.save_as(array=flow_report, dest_file_name="flow_limit_report.csv")
shutil.move("flow_limit_report.csv", destination_folder)    
print("Analysis complete. Your report has been sent to the destination folder.")