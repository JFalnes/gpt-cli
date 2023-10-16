# GPT-4 CLI Chatbot

This project contains a command-line interface (CLI) chatbot powered by OpenAI's GPT-4 model. It allows users to interact with the GPT-4 model in a conversational manner directly from the terminal.

## Features

- Real-time interaction with the GPT-4 model.
- Colored prompts for better user experience.
- Ability to stream the model's response back to the user.
- Configurable settings via an external JSON file.

## Installation

Ensure you have the necessary libraries installed using pip:

```bash
pip install -r requirements.txt
```

## Configuration
1. Create a `.env` file in the project root and add your OpenAI API key like so:

```plaintext
OPENAI_API_KEY=your-api-key-here
```

2. Edit the `config.json` file in the project root with the following structure:

```json
{
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }
    ],
    "response_params": {
        "temperature": 0.3,
        "stream": true
    }
}
```

- The `messages` array contains the initial messages to set the behavior of the model.
- The `response_params` object contains parameters for the `openai.ChatCompletion.create` method to control the behavior of the model.

## Usage

Run the script using Python:

```bash
python main.py
```

You'll be greeted with a prompt (`>>>`). Here, you can type your message to the GPT-4 model. The model's response will be streamed back to you in real-time.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. Any contributions are welcome!
