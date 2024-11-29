import info
import oracledb
import winsound
from pathlib import Path
import uuid, getpass, secrets, asyncio # Needed libraries for oracledb to work.

home = str(Path.home())
oracledb.init_oracle_client(home + "\\instantclient")

def check_status_in_db(msisdns):
	# Function to check MSISDN status
	try:
		# Using "with" to ensure the connection is closed after the block
		with oracledb.connect(
			user = info.user,
			password = info.password,
			host = info.host,
			service_name = info.service
		) as connection:
			# Using "with" to ensure the cursor is closed after the block
			with connection.cursor() as cursor:
				# Query to check the MSISDNs"
				query = info.query1_p1 + msisdns + info.query1_p2
				cursor.execute(query)
				result = cursor.fetchall()
				active_msisdns = [row[0] for row in result] # Extract MSISDNs from tuples into a list
				return active_msisdns
	
	except oracledb.Error as e:
		winsound.MessageBeep(winsound.MB_ICONASTERISK)
		print(f"{info.error}: {e}")
		exit(1) # Close the application.
		return False

def check_results_in_db(msisdns):
	# Function to get back the results of the procedure
	formatted_msisdns = ", ".join(f"'{msisdn}'" for msisdn in msisdns)
	try:
		# Using "with" to ensure the connection is closed after the block
		with oracledb.connect(
			user = info.user,
			password = info.password,
			host = info.host,
			service_name = info.service
		) as connection:
			# Using "with" to ensure the cursor is closed after the block
			with connection.cursor() as cursor:
				# Query to check the MSISDNs"
				query = info.query3_p1 + formatted_msisdns + info.query3_p2
				cursor.execute(query)
				
				result = cursor.fetchall()
				
				if result:
					print("DB accessed, data returned")
					return result
	
	except oracledb.Error as e:
		winsound.MessageBeep(winsound.MB_ICONASTERISK)
		print(f"{info.error}: {e}")
		exit(1) # Close the application.
		return False
