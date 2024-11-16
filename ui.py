import tkinter

def window():
	data = ""
	# Main function to handle the Tkinter UI and process user input.
	def on_submit(text_box):
		nonlocal data  # Declare data as nonlocal to modify it within the nested function
		# Callback function to process input text and close the UI.
		data = text_box.get("1.0", tkinter.END).strip()
		if data:
			root.destroy()
			return data

	# Create the Tkinter window
	root = tkinter.Tk()
	root.title("MSISDN Processor")

	# Add a text box for input
	text_box = tkinter.Text(root, width=80, height=20)
	text_box.pack(pady=10)

	# Add a Submit button
	submit_button = tkinter.Button(root, text = "Submit", command = lambda: on_submit(text_box))
	submit_button.pack(pady = 5)

	root.mainloop()
	return data
