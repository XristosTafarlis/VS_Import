import DB
import sys
import info
import tkinter
import winsound

def text_window():
	text_in = ""
	# Main function to handle the Tkinter UI and process user input.
	def on_submit(text_box):
		nonlocal text_in  # Declare text_in as nonlocal to modify it within the nested function
		# Callback function to process input text and close the UI.
		text_in = text_box.get("1.0", tkinter.END).strip()
		if text_in:
			root.destroy()
			return text_in
		else:
			print("No text detected")
	
	# Create the Tkinter window
	root = tkinter.Tk()
	root.configure(bg = "gray9")
	root.title(info.title)
	
	# Center the window on the screen
	window_width = 600
	window_height = 400
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x_position = (screen_width // 2) - (window_width // 2)
	y_position = (screen_height // 2) - (window_height // 2)
	root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
	
	# Make the window not resizable by setting its resizable attribute to False
	root.resizable(False, False)
	
	# Set the on_close callback
	root.protocol("WM_DELETE_WINDOW", on_close)
	
	# Bind the ESC key to close the window
	root.bind('<Escape>', lambda _: on_close())
	
	# Add a text box for input
	text_box = tkinter.Text(
		root,
		width = 59,
		height = 18,
		bd = 0,
		fg = "gray80",
		bg = "gray20",
		font = ("Courier New", 12))
	
	text_box.pack(pady = 10)
	
	# Add a Submit button
	submit_button = tkinter.Button(
		root,
		text = "Submit",
		width = 20,
		bd = 0,
		bg = "gray50",
		font = ("Courier New", 14),
		relief= "solid",
		activebackground = "gray30",
		activeforeground = "gray80",
		command = lambda: on_submit(text_box))
	
	submit_button.bind('<Enter>', on_hover)
	submit_button.bind('<Leave>', on_default)
	
	submit_button.pack(pady = 5)
	
	root.mainloop()
	return text_in

def query_window(msisdns):
	place_holder_text = "No data retrived from the Database..." # The text displayed on the text_box before the script gets and displays the data from the DB.
	
	# Call the DB to get the final results
	def call_db():
		print("Checking DB")
		data = DB.check_results_in_db(msisdns)
		if data:
			formatted_data = "h2. (i) *10 Euros*\n\n"
			previous_value = None
			for row in data:
				if previous_value is not None and row[2] != previous_value:
					formatted_data += f"\nh2. (i) *{row[2]}*\n\n"
				# Format the row as a string with pipe separators and append a newline
				formatted_data += "|" + "|".join(row[:2]) + "|\n"
				previous_value = row[2]
			
			text_box.config(state = 'normal')
			text_box.delete("1.0", tkinter.END)
			text_box.insert(tkinter.END, formatted_data)
			text_box.config(state = "disabled")
		
		
			root.lift()
			root.attributes('-topmost', True)  # Temporarily make the window topmost
			root.attributes('-topmost', False) # Allow it to behave normally again
			winsound.MessageBeep(winsound.MB_ICONASTERISK)
		
		root.after(60000, call_db)
	
	def copy_to_clipboard_and_exit(text_box):
		# Get all the text from the Text widget
		text_to_copy = text_box.get("1.0", tkinter.END).strip()
		
		# Check if the text box is empty or contains the default message
		if not text_to_copy or text_to_copy == place_holder_text:
			print("No data to copy.")
		else:
			# Copy the text to the clipboard
			text_box.clipboard_clear()
			text_box.clipboard_append(text_to_copy)
			root.after(1000, sys.exit) # 100ms delay before exiting to ensure the text is copied
	
	# Creating a new Tkinter window, similar to the 1st
	root = tkinter.Tk()
	root.configure(bg = "gray9")
	root.title(info.title)
	
	# Center the window on the screen
	window_width = 600
	window_height = 400
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x_position = (screen_width // 2) - (window_width // 2)
	y_position = (screen_height // 2) - (window_height // 2)
	root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
	
	# Make the window not resizable by setting its resizable attribute to False
	root.resizable(False, False)
	
	# Set the on_close callback
	root.protocol("WM_DELETE_WINDOW", on_close)
	
	# Bind the ESC key to close the window
	root.bind('<Escape>', lambda _: on_close())
	
	# Add a text box for input
	text_box = tkinter.Text(
		root,
		width = 74,
		height = 21,
		bd = 0,
		fg = "gray80",
		bg = "gray20",
		font = ("Courier New", 10))
	
	text_box.pack(pady = 5)
	text_box.insert(tkinter.END, place_holder_text)
	text_box.config(state = "disabled")
	
	# Add a Copy button
	copy_button = tkinter.Button(
		root,
		text = "Copy & Exit",
		width = 20,
		bd = 0,
		bg = "gray50",
		font = ("Courier New", 14),
		relief= "solid",
		activebackground = "gray30",
		activeforeground = "gray80",
		command = lambda: copy_to_clipboard_and_exit(text_box)
		)
	
	copy_button.bind('<Enter>', on_hover)
	copy_button.bind('<Leave>', on_default)
	
	copy_button.pack(padx = 30, pady = 5)
	
	call_db() # Start the first DB query immediately
	root.mainloop()

def on_hover(event):
	event.widget.configure(bg = "gray70")

def on_default(event):
	event.widget.configure(bg = "gray50")

def on_close():
		print("Exiting...")
		sys.exit() # Exit the script