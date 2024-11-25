import os
from dotenv import load_dotenv

load_dotenv()

newpasss = os.getenv('PASSWORD')

print (newpasss)

