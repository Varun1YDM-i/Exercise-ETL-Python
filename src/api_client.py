import requests

# ExerciseAPIClient class is used to fetch the data from api by using request
class ExerciseAPIClient:
   # intializing the required values for making API calls
   def __init__(self, logger):
       self.url = "https://exercisedb.p.rapidapi.com/exercises"
       self.querystring = {"limit": "50", "offset": "0"}
       self.headers = {
           "x-rapidapi-key": "988f46d636msh9f72d813f19cfa3p1160ffjsn72b8c9dd2f8f",
           "x-rapidapi-host": "exercisedb.p.rapidapi.com"
       }
       self.logger = logger
   # fetching the API response and returning it in json format to the ExerciseETL class
   def fetch_exercises(self):
       self.logger.log("Sending request to ExerciseDB API")
       try:
           response = requests.get(self.url, headers=self.headers, params=self.querystring, timeout=10)
           response.raise_for_status()
           self.logger.log("Successfully fetched data from API")
           return response.json()
       except requests.exceptions.Timeout:
           self.logger.log("Error: Request timed out.")
       except requests.exceptions.HTTPError as err:
           self.logger.log(f"HTTP Error occurred: {err}")
       except requests.exceptions.RequestException as err:
           self.logger.log(f"Request failed: {err}")
       return None
