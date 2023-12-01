# ChatGPT-AutoBot-Chrome

## Introduction
ChatGPT-AutoBot-Chrome is a Python library designed to automate interactions with Google Bard, HuggingChat, and OpenAI's ChatGPT webpages. It simplifies the process of sending automated prompts and managing responses, and reduces the need for repeated logins by saving user credentials. This library is based on the [TalkingHeads](https://github.com/ugorsahin/TalkingHeads) project.

![](result.gif)


## Features
- Automated prompt handling for GPT-3.5, GPT-4, and GPTs.
- One-time login with credential saving for future sessions.
- Support for various login methods, including Google and manual login.
- Easy-to-use interface for seamless communication with AI models.

## Installation
Clone the repository:
```bash
git clone https://github.com/yueyueL/ChatGPT-AutoBot-Chrome
cd ChatGPT-AutoBot-Chrome
```
Install required dependencies:
```bash
pip install -r requirements.txt
```

## Initial Run
The first time you run the program, you will be prompted to enter your login credentials. You can choose to login with Google or manually enter your username and password. 

- Choose your preferred login type (normal, google, or manually).
- Set the user_data_dir parameter to save your login session.
- Perform the initial login based on the selected method.


### ChatGPTClient Parameters

- **username:** (Type: String) - The email address used for logging into the ChatGPT service.

- **password:** (Type: String) - The password associated with the email address for the ChatGPT service. Keep this secure.

- **skip_login:** (Type: Boolean) - If set to True, the client will attempt to use a saved session for login, avoiding the need for credentials. Useful for repeated runs.

- **headless:** (Type: Boolean) - Determines whether the browser runs in headless mode (no GUI). Set to False to see the browser UI.

- **incognito:** (Type: Boolean) - If True, the browser launches in incognito mode, ensuring no cookies or history from previous sessions are used.

- **user_data_dir:** (Type: String) - Path to the directory where user data (like cookies and login sessions) is stored, allowing for session persistence between runs.

- **target_url (Optional):** (Type: String) - The URL of the ChatGPT service. Useful for specifying the exact model or version, such as GPT-4 and GPTs.

- **login_type (Optional):** (Type: String) - Specifies the type of login to be used (normal, google, manually). Determines how the automated login process is handled.

### First-Time Use

For first-time use, initialize the `ChatGPTClient` as follows:

```python
from chatbot import ChatGPTClient
chathead = ChatGPTClient(username="your_email@gmail.com", password="your_password", skip_login=False, login_type="normal", incognito=False, user_data_dir='/path/to/your/user/')
```

### Subsequent Uses and Skipping Login
To skip the login process and use a saved session, you can set `skip_login = True` and `incognito=False`. You can also specify whether to use incognito mode (True for a fresh session or False to use the saved session).
```python
from chatbot import ChatGPTClient

# For subsequent uses
chathead = ChatGPTClient(username="your_email@gmail.com", password="your_password", skip_login=True, incognito=False, user_data_dir='/path/to/your/user/')
```

### Automating Prompts
Save your prompts in `a .txt` file and use the library to read and send them line by line.
```python
prompts_file = "path/to/prompts.txt"
with open(prompts_file, "r") as file:
    prompts = [line.strip() for line in file]

for prompt in prompts:
    response = chathead.interact(prompt)
    print(response)
```

### Accessing GPT-4 or GPTs

For ChatGPT plus users, to access GPT-4 or GPTs, you can set the `target_url` parameter when initializing the `ChatGPTClient`. Here's how you can do it:

```python
from chatbot import ChatGPTClient

# Set the target_url to access GPT-4
target_url = "https://chat.openai.com/?model=gpt-4"

# Initialize the ChatGPTClient with the target_url
chathead = ChatGPTClient(username="your_email@gmail.com", password="your_password", skip_login=True, incognito=False, headless=False, login_type="normal", user_data_dir='/path/to/your/user/', target_url=target_url)
```

Additionally, you can also set the `target_url` to access specific chat groups or discussions related to GPTs, like this:
```python
from chatbot import ChatGPTClient

# Set the target_url to GPTs
target_url = "https://chat.openai.com/g/g-kB3tDzYUb-academic-writing-assistant"

# Initialize the ChatGPTClient with the target_url
chathead = ChatGPTClient(username="your_email@gmail.com", password="your_password", skip_login=True, incognito=False, headless=False, login_type="normal", user_data_dir='/path/to/your/user/', target_url=target_url)
```


## Acknowledgment

We would like to express our appreciation to the [TalkingHeads](https://github.com/ugorsahin/TalkingHeads) project and its developers for their pioneering work in automated interactions with AI models. Their efforts have greatly influenced and inspired the development of ChatGPT-AutoBot-Chrome. Additionally, we extend our thanks to the Selenium and ChromeDriver communities for their valuable contributions to web automation.

## Disclaimer

**Disclaimer:** This software is experimental and is provided without any warranty. By using this software, you agree to the following terms and conditions:

1. This software is experimental in nature.
2. You are solely responsible for the use of this software.
3. The developer is not responsible for any outcomes resulting from the use of this software.
4. Users must adhere to the terms of use of OpenAI's ChatGPT. For more details, please visit [OpenAI's terms of use](https://openai.com/terms).

If you do not agree to these terms, you should not use this software.

