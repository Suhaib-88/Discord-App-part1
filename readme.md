Gemini Discord Bot
This project involves creating a Discord bot that leverages Google Gemini pro Generative AI model to provide intelligent responses to text and image messages. The bot can summarize URLs, process attachments, and generate responses based on user input, offering an interactive and dynamic user experience.

## Technologies Used
- Discord.py: For creating the Discord bot.
- Google Generative AI (Gemini-1.5-flash): For text and image generation.
- aiohttp: For asynchronous HTTP requests.
- BeautifulSoup: For web scraping.
- PyMuPDF (fitz): For processing PDF attachments.
- YouTube Transcript API: For extracting transcripts from YouTube videos.

## Features:

- Responds to user mentions and direct messages.
- Uses a generative AI model to generate responses.
- Provides real-time typing indicators.
- Filters out harmful content using safety settings.

## Prerequisites:
Python 3.6+
Discord Bot Token
Google AI API Key'

### Setup Instructions:
Clone the Repository:
``` git clone https://github.com/Suhaib-88/Gemini-Bot.git ```
```cd Gemini-Bot```

### Install Dependencies:
```pip install -r requirements.txt```

### Set Up Environment Variables:
```
GOOGLE_AI_KEY=your_google_ai_key
DISCORD_BOT_TOKEN=your_discord_bot_token
```

### Run the Bot:
```python GeminiBasicBot.py```