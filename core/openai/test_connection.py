from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Create the OpenAI client
client = OpenAI()

# Send a simple request
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Say exactly: Project Freedom is online."
)

# Print the response
print(response.output_text)