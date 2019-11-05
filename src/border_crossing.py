import sys
import csv
import math

input_file = sys.argv[1]
output_file= sys.argv[2]
border_crossing = {}
measures_of_crossing = {}

def extract_month_year(x):  ### Helper - to extract month and year
	mm,dd,yyyy_tt = x.split("/")
	yyyy = yyyy_tt.split(" ")
	yyyy = str(yyyy[0])
	mm = str(mm)
	year_month = yyyy + mm
	year_month = int(year_month)
	return year_month

def normal_round(n):  	### Helper to overcome python rounding down issue with 0.5 --> 0 instead of 1
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)


with open(input_file ,"r") as f:
	reader = csv.reader(f)
	next(reader, None) #skip the header
	for x in reader:
		border_name=x[3]
		date_time = x[4]
		measure = x[5]
		value = int(x[6])
		yyyy_mm = extract_month_year(date_time)		### Extracting just the month and year
		if yyyy_mm not in border_crossing:				### Initialize any new month/year
			border_crossing[yyyy_mm] = {}
		if border_name not in border_crossing[yyyy_mm]:			### Initialize any new border
			border_crossing[yyyy_mm][border_name] = {}
		if measure not in border_crossing[yyyy_mm][border_name]:	### Initialize any new measure
			border_crossing[yyyy_mm][border_name][measure] = {}
			border_crossing[yyyy_mm][border_name][measure]['sum_value'] = 0
			border_crossing[yyyy_mm][border_name][measure]['running_average'] = 0

		### Calculating Sum/Value for each month/border/measure
		border_crossing[yyyy_mm][border_name][measure]['sum_value'] += value
		border_crossing[yyyy_mm][border_name][measure]['running_average'] = 0	### Initializing running average
		border_crossing[yyyy_mm]['date_to_disp'] = date_time			### To print in the final output CSV

		if border_name not in measures_of_crossing:
			measures_of_crossing[border_name] = {}
		if measure not in measures_of_crossing[border_name]: 			### Serves 2 purposes 1. List of all Measures 2. Holds the previous month info
			measures_of_crossing[border_name][measure] = {}
			measures_of_crossing[border_name][measure]['previous_months_sum'] = 0
			measures_of_crossing[border_name][measure]['previous_months_count'] = 0

	### Sort the main dict in ascending order - based on month/year and calculate running average
	for yyyy_mm in sorted(border_crossing):
		for border_name in border_crossing[yyyy_mm]:
			if border_name != 'date_to_disp':
				for measure in measures_of_crossing[border_name]:
					if measure not in border_crossing[yyyy_mm][border_name]:		### If a given measure is not used in the current month - then initialize the sum to 0
						border_crossing[yyyy_mm][border_name][measure] = {}
						border_crossing[yyyy_mm][border_name][measure]['sum_value'] = 0
						border_crossing[yyyy_mm][border_name][measure]['running_average'] = 0
					if measures_of_crossing[border_name][measure]['previous_months_count'] != 0:		### If the current month is the 1st month - then average = 0 previously initialized
						border_crossing[yyyy_mm][border_name][measure]['running_average'] = int(normal_round(measures_of_crossing[border_name][measure]['previous_months_sum']/measures_of_crossing[border_name][measure]['previous_months_count']))
					measures_of_crossing[border_name][measure]['previous_months_count'] += 1
					measures_of_crossing[border_name][measure]['previous_months_sum'] += border_crossing[yyyy_mm][border_name][measure]['sum_value']

	with open(output_file,'w',newline='\n', encoding='utf-8') as out:
		csv_out = csv.writer(out)
		csv_out.writerow(['Border','Date','Measure','Value','Average'])
		for yyyy_mm in sorted(border_crossing, reverse=True):
			list_for_sort = []
			for border_name in border_crossing[yyyy_mm]:
				if border_name != 'date_to_disp':
					for measure in border_crossing[yyyy_mm][border_name]:
						#print (border_name,border_crossing[yyyy_mm]['date_to_disp'],measure,border_crossing[yyyy_mm][border_name][measure]['sum_value'],border_crossing[yyyy_mm][border_name][measure]['running_average'])
						list_for_sort.append(tuple([border_name,border_crossing[yyyy_mm]['date_to_disp'],measure,border_crossing[yyyy_mm][border_name][measure]['sum_value'],border_crossing[yyyy_mm][border_name][measure]['running_average']]))
			sorted_by_sum_val = sorted(list_for_sort, key = lambda tup:tup[4], reverse=True)

			for x in sorted_by_sum_val:
				if x[3] != 	0:
					print (x)
					csv_out.writerow(x)



#csv_out.close()
