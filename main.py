import ui
import DB
import texts
import file_writer

def main():
	text_input = ui.window()
	data = texts.data_extract(text_input)
	extracted_msisdns = texts.get_all_msisdns(data)
	active_msisdns = DB.check_status_in_db(extracted_msisdns)
	file_writer.write_to_csv(data, active_msisdns)
	texts.copy_to_clipboard()

if __name__ == "__main__":
	main()