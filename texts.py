import pyperclip

def get_all_msisdns(parsed_data):
	unique_msisdns = set() # Using a set to store only unique MSISDNs
	
	# Collect all MSISDNs from all top-up amounts
	for msisdns_list in parsed_data.values():
		for msisdn in msisdns_list:
			unique_msisdns.add(f"'{msisdn[1:]}'")  # Adding single quotes for SQL format
	
	# Join MSISDNs with commas to form the SQL IN clause
	msisdns = ",\n".join(sorted(unique_msisdns))
	
	# Copy to clipboard
	pyperclip.copy(msisdns)
