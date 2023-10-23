import openai
import os
import time
import json
from dotenv import load_dotenv
from colorama import Fore, Style, init
import platform
if platform.system() == 'Windows':
    import pyreadline as readline
else:
    import readline
import argparse

# Initialize colorama
init()

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_config():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(dir_path, 'config.json')
    with open(config_path, 'r') as f:
        return json.load(f)


def chat(model):
    """
    This function initializes a chatbot using the OpenAI API and allows the user to interact with it through the command line.
    
    Args:
    - model (str): The name of the GPT model to use. Default is "gpt-4".
    """
    config = load_config()
    messages = config['messages']
    while True:
        try:
            user_message = input(f'{Fore.BLUE}>>> {Fore.RESET}')
            messages.append({"role": "user", "content": user_message})
        except (KeyboardInterrupt, EOFError):
            print(f'\n{Fore.RED}Exiting chat. Goodbye! {Fore.RESET}')
            exit()
        # Record the time before the request is sent
        start_time = time.time()

        # Send a ChatCompletion request with stream=True
        response_gen = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                **config['response_params']
            )
        
        # Create variables to collect the stream of chunks
        collected_chunks = []
        collected_messages = []        
        # Print the assistant's response label
        print(f'{Fore.GREEN}GPT-{model[-1]}: ', end='', flush=True)
        
        # Iterate through the stream of events
        for chunk in response_gen:
            collected_chunks.append(chunk)  # Collect chunks here
            chunk_message = chunk['choices'][0]['delta']  # Extract the message
            collected_messages.append(chunk_message)  # Save the message
            text_content = chunk_message.get('content', '')
            print(text_content, end='', flush=True)
        
        print(f'{Fore.RESET}\n', end='')  # Print a newline at the end of the streaming text, reset color
        
        # Update the messages list with the assistant's response
        full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
        messages.append({"role": "assistant", "content": full_reply_content})


def parse_args():
    parser = argparse.ArgumentParser(description="Chat with GPT!")
    parser.add_argument("--model", default="gpt-4", help="Name of the model to use")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    chat(args.model)
