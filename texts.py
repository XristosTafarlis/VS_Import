def data_extract(text_input):
	# Split text into sections by "Top-up Simulation"
	sections = text_input.split("Top-up Simulation")
	msisdn_dict = {}

	for section in sections[1:]:
		lines = section.strip().splitlines()
		amount = lines[0].strip() # Extract the amounts
		
		msisdns = [] # Create an empty list to store MSISDNs
		for line in lines[1:]: # Start from the second line (The first has the top-up amounts)
			cleaned_line = line.strip() # Remove leading and trailing spaces
			if cleaned_line and "None" not in cleaned_line: # If the line is not empty and does not contain "None"
				msisdns.append(cleaned_line) # Add the cleaned line to the msisdns list
		# Creating the Dictionary
		msisdn_dict[amount] = msisdns
	return msisdn_dict

def get_all_msisdns(parsed_data):
	unique_msisdns = set() # Using a set to store only unique MSISDNs
	
	# Collect all MSISDNs from all top-up amounts
	for msisdns_list in parsed_data.values():
		for msisdn in msisdns_list:
			unique_msisdns.add(f"'{msisdn[1:]}'")  # Adding single quotes for SQL format
	
	# Join MSISDNs with commas to form the SQL IN clause
	msisdns = ",\n".join(sorted(unique_msisdns))
	
	return msisdns
