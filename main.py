import os
import ui
import DB
import texts
import message
import file_writer

def main():
	desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
	
	text_input = ui.window()
	data = texts.data_extract(text_input)
	extracted_msisdns = texts.get_all_msisdns(data)
	active_msisdns = DB.check_status_in_db(extracted_msisdns)
	filename = file_writer.write_to_csv(data, active_msisdns, desktop_path)
	full_file_path = os.path.join(desktop_path, filename)
	message.send_message(full_file_path)
	# texts.copy_to_clipboard()

if __name__ == "__main__":
	main()