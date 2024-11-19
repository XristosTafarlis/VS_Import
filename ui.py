import sys
import tkinter
import info

def window():
	text_in = ""
	# Main function to handle the Tkinter UI and process user input.
	def on_submit(text_box):
		nonlocal text_in  # Declare text_in as nonlocal to modify it within the nested function
		# Callback function to process input text and close the UI.
		text_in = text_box.get("1.0", tkinter.END).strip()
		if text_in:
			root.destroy()
			return text_in
	
	def on_close():
		print("Window closed without input. Exiting...")
		sys.exit()  # Exit the script
	
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

def on_hover(event):
	event.widget.configure(bg = "gray70")

def on_default(event):
	event.widget.configure(bg = "gray50")