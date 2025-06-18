import csv
# CSVWriter class is used for creating the csv files and adding the context from API.
class CSVWriter:
   def __init__(self, filename='../output/exercise.csv', logger=None):
       self.filename = filename
       self.logger = logger

   def write_data(self, exercises):
       # columns of the dataset
       headers = [
           'bodyPart', 'equipment', 'gifUrl', 'id', 'name', 'target',
           'secondaryMuscles', 'instructions', 'description', 'difficulty', 'category'
       ]

       try:
           # writing each row into the exercise.csv file
           with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
               writer = csv.writer(file)
               writer.writerow(headers)
               if self.logger:
                   self.logger.log("Header row written to CSV")
               # writing each row into the file
               for row in exercises:
                   writer.writerow([
                       row.get(headers[0], ''),
                       row.get(headers[1], ''),
                       row.get(headers[2], ''),
                       row.get(headers[3], ''),
                       row.get(headers[4], ''),
                       row.get(headers[5], ''),
                       row.get(headers[6], []),
                       row.get(headers[7], []),
                       row.get(headers[8], ''),
                       row.get(headers[9], ''),
                       row.get(headers[10], '')
                   ])
               if self.logger:
                   self.logger.log("Successfully inserted records into the CSV")
       except IOError as e:
           # Handiling file I/O error
           if self.logger:
               self.logger.log(f"File I/O error: {e}")
