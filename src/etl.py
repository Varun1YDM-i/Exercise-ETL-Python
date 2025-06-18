from logger import Logger
from api_client import ExerciseAPIClient
from csv_writer import CSVWriter

# main ETL class
class ExerciseETL:
   def __init__(self):
       self.logger = Logger()
       self.api_client = ExerciseAPIClient(self.logger)
       self.csv_writer = CSVWriter(logger=self.logger)

   def run(self):
       self.logger.log("\nETL process started")
       try:
           data = self.api_client.fetch_exercises()
           if data:
               self.csv_writer.write_data(data)
           else:
               self.logger.log("ETL terminated: No data fetched.")
       except Exception as e:
           self.logger.log(f"Unexpected error during ETL run: {e}")
       finally:
           self.logger.log("ETL process completed")

if __name__ == "__main__":
   etl = ExerciseETL()
   etl.run()
   print("ETL run complete. Check Log files in /logs  and csv file in /output.")
