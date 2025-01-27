import re
import os
import csv
import info
import datetime

def extract_top_up_amount(top_up_amount):
	# Use a regular expression to extract the numeric part of the top-up amount
	amount_number = re.search(r"\d+", top_up_amount).group()  # Extract digits
	return amount_number + "00" # Append "00" to get the desired format

def transform_msisdn(msisdn):
	# Apply the transformation to each MSISDN
	return "31" + msisdn[1:]

def write_to_csv(parsed_data, active_msisdns, desktop_path):
	# Creating the full file name and path
	current_date = datetime.datetime.now().strftime("%Y%m%d")
	filename = f"VELSUR_{current_date}000000_000101.csv"
	full_file_path = os.path.join(desktop_path, filename)
	
	inactive_msisdns = set() # Using a set to store inactive MSISDNs
	
	# Open a CSV file to write the data
	with open(full_file_path, mode = "w", newline = "\n") as file:
		writer = csv.writer(file, quoting = csv.QUOTE_MINIMAL, escapechar='\\')
		
		counter = 1 # Counter to create unique identifiers (e.g., "000001", "000002")
		
		# Iterate over each top-up amount and its MSISDNs
		for top_up_amount, msisdns in parsed_data.items():
			for msisdn in msisdns:
				if msisdn[1:] in active_msisdns: # Check if the MSISDN is active
					amount_value = extract_top_up_amount(top_up_amount)
					modified_msisdn = transform_msisdn(msisdn)
					
					# Create the unique identifier for each MSISDN (formatted as six digits)
					unique_id = f"{counter:06d}"
					counter += 1
					
					# Construct the row in the desired format
					row = [
						modified_msisdn,
						f"0000000000000000000000000_00000_{unique_id}",
						amount_value,
						f"{current_date}000101",
						"Electronic Vouchers"
					]
					
					# Write the row to the CSV file
					writer.writerow(row)
				else:
					inactive_msisdns.add(msisdn)
		# Write the total MSISDN count without a newline
		file.write(str(counter - 1))
	write_to_txt(sorted(inactive_msisdns), desktop_path)
	return filename

def write_to_txt(inactive_msisdns, desktop_path):
	# New txt file path and name
	full_file_path = os.path.join(desktop_path, "inactive_msisdns.txt")
	# Write all the inactive MSISDNs to a .txt file.
	if inactive_msisdns:
		msisdns_query_string = ",\n".join(f"		'{msisdn[1:]}'" for msisdn in inactive_msisdns)
		with open(full_file_path, mode = "w") as txt_file:
			txt_file.write(info.query2 + msisdns_query_string + "\n	)")
