# Discord Auto Chat

A Discord bot for auto-leveling with automated message sending, supporting multiple accounts.

## Features

- Supports multiple accounts (tokens)
- Auto deletes messages after sending
- Channel timeout detection
- Handles rate limits and slow mode
- Comprehensive error handling
- Customizable delay between messages
- 54 variations of random messages

## Requirements

- Python 3.7+
- discord.py 1.7.3
- asyncio
- colorama

## Installation

1. Clone this repository:
```bash
git clone https://github.com/synthinks-og/discordchat.git
cd discordchat
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Create a `token.txt` file and add Discord tokens (one token per line):
```
TOKEN1
TOKEN2
TOKEN3
```

2. Run the script:
```bash
python jawa.py
```

3. Enter the required information:
- Channel ID
- Number of messages to send
- Delay between each message (in seconds)

## How to Get a Discord Token

1. Open Discord in a browser
2. Press F12 to open Developer Tools
3. Go to the Network tab
4. Type "api" in the filter
5. Find a request with the "authorization" header
6. Copy the token value from there

## How to Get a Channel ID

1. Enable Developer Mode in Discord (User Settings > App Settings > Advanced > Developer Mode)
2. Right-click on the channel
3. Select "Copy ID"

## Warnings

⚠️ **IMPORTANT**:
- Using self-bots violates Discord’s Terms of Service
- Use at your own risk
- It is recommended to set a minimum delay of 10 seconds between messages
- Ensure that the tokens used are valid and fresh

## Error Handling

The script will handle various types of errors:
- Invalid/expired token
- Channel not found
- Channel timeout
- Rate limits
- Slow mode
- No permission to send/delete messages
- Voice channel detection

## Usage Tips

1. Use a safe delay:
   - At least 10 seconds between messages
   - Avoid spamming too many messages

2. If an error occurs:
   - Invalid token: Update the token in `token.txt`
   - Rate limit: The script will automatically wait
   - Timeout: Wait until the timeout expires
  
     
