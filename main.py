import re
import csv
import json
import datetime
import tkinter

# GUI Setup
def parse_text():
	data = text_box.get("1.0", tkinter.END)
	parsed_data = parse_ticket(data)
	save_to_json(parsed_data)  # Save parsed data to a JSON file for visualization
	
	current_date = datetime.datetime.now().strftime("%Y%m%d")
	
	filename = f"VELSUR_{current_date}000000_000101.csv"
	
	# Open a CSV file to write the data
	with open(filename, mode = "w", newline = "\n") as file:
		writer = csv.writer(file, quoting = csv.QUOTE_MINIMAL, escapechar='\\')
		
		counter = 1 # Counter to create unique identifiers (e.g., "000001", "000002")
		
		# Iterate over each top-up amount and its MSISDNs
		for top_up_amount, msisdns in parsed_data.items():
			for msisdn in msisdns:
				# Use a regular expression to extract the numeric part of the top-up amount
				amount_number = re.search(r"\d+", top_up_amount).group()  # Extracts only digits
				amount_value = amount_number + "00"  # Append "00" to get the desired format
				
				# Create the unique identifier for each MSISDN (formatted as six digits)
				unique_id = f"{counter:06d}"
				counter += 1
				
				# Construct the row in the desired format
				row = [
					msisdn,
					f"0000000000000000000000000_00000_{unique_id}",
					amount_value,
					f"{current_date}000101",
					"Electronic Vouchers"
				]
				
				# Write the row to the CSV file
				writer.writerow(row)

def parse_ticket(data):
	# Split text into sections by "Top-up Simulation"
	sections = data.split("Top-up Simulation")
	msisdn_dict = {}

	for section in sections[1:]:
		lines = section.strip().splitlines()
		amount = lines[0].strip()  # Extract the amounts
		
		msisdns = []  # Create an empty list to store MSISDNs
		for line in lines[1:]:  # Start from the second line (The first has the top-up amounts)
			cleaned_line = line.strip()  # Remove leading and trailing spaces
			if cleaned_line and "None" not in cleaned_line:  # If the line is not empty and does not contain "None"
				msisdns.append(cleaned_line)  # Add the cleaned line to the msisdns list

		modified_msisdns = ["31" + msisdn[1:] for msisdn in msisdns] # Apply the transformation to each MSISDN
		msisdn_dict[amount] = modified_msisdns

	return msisdn_dict

def save_to_json(parsed_data):
	with open("parsed_msisdn_data.json", "w") as file:
		json.dump(parsed_data, file, indent = 4)  # Save data in JSON format for readability

# Tkinter GUI Setup
root = tkinter.Tk()
text_box = tkinter.Text(root, height = 15, width = 50)
text_box.pack()
process_button = tkinter.Button(root, text = "Process", command = parse_text)
process_button.pack()
root.mainloop()
