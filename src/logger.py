from datetime import datetime
import os
# Logger class is used for logging the status of each step in the apllication
class Logger:
   # creating the log.txt file using write method
   def __init__(self, log_file='../logs/log.txt'):
       self.log_file = log_file
       # Check if the log file already exists
       if not os.path.exists(self.log_file):
           # Create it and write the creation time
           with open(self.log_file, mode='w') as f:
               f.write(f'Log file created at: {datetime.now()}')    # log method is used to append the status of the tasks to log.txt
   def log(self, message):
       # opening the log.txt file and appending the status and time log
       with open(self.log_file, mode='a') as f:
           f.write(f'\n{message} - {datetime.now()}')
