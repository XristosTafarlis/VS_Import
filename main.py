import ui
import file_writer

def parse_ticket(data):
	# Split text into sections by "Top-up Simulation"
	sections = data.split("Top-up Simulation")
	msisdn_dict = {}

	for section in sections[1:]:
		lines = section.strip().splitlines()
		amount = lines[0].strip() # Extract the amounts
		
		msisdns = []  # Create an empty list to store MSISDNs
		for line in lines[1:]: # Start from the second line (The first has the top-up amounts)
			cleaned_line = line.strip() # Remove leading and trailing spaces
			if cleaned_line and "None" not in cleaned_line: # If the line is not empty and does not contain "None"
				msisdns.append(cleaned_line) # Add the cleaned line to the msisdns list
		# Creating the Dictionary
		msisdn_dict[amount] = msisdns
	return msisdn_dict

def transform_msisdn(msisdn):
	# Apply the transformation to each MSISDN
	return "31" + msisdn[1:]

def main():
	data = ui.window()
	parsed_data = parse_ticket(data)
	file_writer.save_to_json(parsed_data)
	file_writer.write_to_csv(parsed_data)

if __name__ == "__main__":
	main()