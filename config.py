from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), ".env")

# Load file from the path.
load_dotenv(dotenv_path)

# sendgrid
API_KEY = getenv("API_KEY", "")
FROM_EMAIL = getenv("FROM_EMAIL", "")

SUCCESS_CODES = ['200', '202']
FAIL = '42'

# language
BY = '_by'
RU = '_ru'
