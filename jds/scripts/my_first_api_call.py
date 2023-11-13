from openai import OpenAI
import os

# Fetch the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Ensure that the API key is not None
if not api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

# Instantiate the OpenAI client
client = OpenAI(
  api_key=api_key  # Corrected this line
)
# Get the prompt from the user
text = input("Enter Prompt Here: ")

# Call the Completion API with the updated method and access the response
completion = client.completions.create(
  model="text-davinci-003",
  prompt=text,
  max_tokens=60
)

# Access the response text from the Pydantic model
print(completion.choices[0].text.strip())