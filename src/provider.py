import os
from typing import Callable
from datetime import datetime
from openai import OpenAI


# Load our open AI key from environment variable OPENAI_API_KEY
# We'll load this via pass with something like this:
# export OPENAI_API_KEY=`pass OPENAI_API_KEY`
# We would never store keys in the codebase.

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_prompt(prompt: str):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    location = "Beach Lake, PA"
    return f"""You are acting as a voice assistant. Be very brief.
    About the user: The current date is {timestamp}
    Current location is {location}, here is the what they've asked: {prompt}"""


def send_to_openai(text: str, process_chunk: Callable[[str], None]):
    try:
        response = ""
        prompt = get_prompt(text)
        stream = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            stream=True,
            model="gpt-4",
        )

        # Stream the results back
        for chunk in stream:
            content = chunk.choices[0].delta.content or ""
            response += content
            if process_chunk:
                process_chunk(content)

        return response
        # print (chat_completion)
        # return chat_completion.choices[0].message["content"]

    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return "Sorry, I couldn't process that."
