import re
import csv
import json
import datetime

def save_to_json(parsed_data):
	with open("parsed_msisdn_data.json", "w") as file:
		json.dump(parsed_data, file, indent = 4)  # Save data in JSON format for readability

def write_to_csv(parsed_data):
	current_date = datetime.datetime.now().strftime("%Y%m%d")
	
	filename = f"VELSUR_{current_date}000000_000101.csv"
	
	# Open a CSV file to write the data
	with open(filename, mode = "w", newline = "\n") as file:
		writer = csv.writer(file, quoting = csv.QUOTE_MINIMAL, escapechar='\\')
		
		counter = 1 # Counter to create unique identifiers (e.g., "000001", "000002")
		
		# Iterate over each top-up amount and its MSISDNs
		for top_up_amount, msisdns in parsed_data.items():
			for msisdn in msisdns:
				amount_value = extract_amount(top_up_amount)
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

def extract_amount(top_up_amount):
	# Use a regular expression to extract the numeric part of the top-up amount
	amount_number = re.search(r"\d+", top_up_amount).group()  # Extract digits
	return amount_number + "00" # Append "00" to get the desired format

def transform_msisdn(msisdn):
	# Apply the transformation to each MSISDN
	return "31" + msisdn[1:]
