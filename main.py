import ui
import DB
import file_writer
import texts

def main():
	data = ui.window()
	parsed_data = texts.parse_ticket(data)
	unique_msisdns = texts.get_all_msisdns(parsed_data)
	active_msisdns = DB.check_status_in_db(unique_msisdns)
	file_writer.write_to_csv(parsed_data, active_msisdns)

if __name__ == "__main__":
	main()