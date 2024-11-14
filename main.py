import tkinter as tk
import json

# GUI Setup
def parse_text():
	data = text_box.get("1.0", tk.END)
	parsed_data = parse_ticket(data)
	save_to_json(parsed_data)  # Save parsed data to a JSON file for visualization

def parse_ticket(data):
	# Split text into sections by "Top-up Simulation"
	sections = data.split("Top-up Simulation")
	msisdn_dict = {}

	for section in sections[1:]:
		lines = section.strip().splitlines()
		amount = lines[0].strip()  # Extract the amount
		msisdns = [line.strip() for line in lines[1:] if line.strip() and "None" not in line]
		msisdn_dict[amount] = msisdns

	return msisdn_dict

def save_to_json(parsed_data):
	with open("parsed_msisdn_data.json", "w") as file:
		json.dump(parsed_data, file, indent=4)  # Save data in JSON format for readability

# Tkinter GUI Setup
root = tk.Tk()
text_box = tk.Text(root, height=15, width=50)
text_box.pack()
process_button = tk.Button(root, text="Process", command=parse_text)
process_button.pack()
root.mainloop()
