import os
import ui
import DB
import texts
import message
import file_writer

def main():
	desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
	
	text_input = ui.text_window()
	data = texts.data_extract(text_input)
	extracted_msisdns = texts.get_all_msisdns(data)
	active_msisdns = DB.check_status_in_db(extracted_msisdns)
	filename = file_writer.write_to_csv(data, active_msisdns, desktop_path)
	message.send_message(os.path.join(desktop_path, filename))
	ui.query_window(active_msisdns)

if __name__ == "__main__":
	main()