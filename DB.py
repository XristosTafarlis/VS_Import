import info
import oracledb
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
		
		# Even though using "with" for both connection and cursor closes them, I will close them also manualy just in case.
		cursor.close()
		connection.close()

	except oracledb.Error as e:
		print(f"{info.error}: {e}")
		exit(1) # Close the application.
		return False