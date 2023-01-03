# COVID-19 Twitter Bot
This is a Twitter bot that tweets Nepal's COVID-19 cases updates on Twitter every day. The bot uses data from the Nepal's Ministry of Health and Population to get the latest numbers and then tweets them out to its followers.

## Installation
To use this bot, you will need to have Python 3 and pip installed on your system. You will also need to have a Twitter account and create a developer account in order to use the Twitter API.

1. Clone the repository:
```
git clone https://github.com/atitkh/covid19-twitter-bot.git
```

2. Navigate to the project directory:
```
cd covid19-twitter-bot
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Create .env file and fill in the required variables as follows:
```
CONSUMER_KEY: Your Twitter API consumer key.
CONSUMER_SECRET: Your Twitter API consumer secret.
ACCESS_TOKEN: Your Twitter API access token.
ACCESS_TOKEN_SECRET: Your Twitter API access token secret.
```

5. Run the bot:
```           
python main.py
```

## Usage
The bot will tweet the latest COVID-19 cases in Nepal every day at a specified time (which you can customize in the main.py file). 

## Contributing
If you find any bugs or have any suggestions for improvement, please feel free to open an issue or create a pull request.
