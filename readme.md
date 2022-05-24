# Telegram Dev News Bot 

A Telegram bot that gathers news from multiple sources in one location so you don't have to.

## Latest Update (v0.1.2)

4/05/2022

**Click on badge to run it on repl.it 👉🚀
[![Run on Repl.it](https://repl.it/badge/github/amrohan/ChatBot)](https://replit.com/@amrohan/chatbot)**

Changes to the bot now allow you to host fully on Replit.com without having to configure anything. Simply replace the scretes.

Also added new commands:

- /tldr - Get a tldr news
- /devto - Get a dev.to news according to your interests
- /hackernews - Get a HackerNews all 30 news 
- /techcrunch - Get a techcrunch top 20 posts
- /medium - Articles from medium ( Tech related )
- /quotes - Get a random quote


## Demo

Test the bot here 👉 [Chat-Bot](https://t.me/amrohan_bot)

<p align="center">
<img src="https://res.cloudinary.com/amrohan/image/upload/v1650983650/Images/xtkerudyi6sul1xfqlui.jpg" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="40%" height="40%" />
</p>

## Create Bot

The first thing you need to do is tell Telegram that you want to create a bot. For this, you’ll need a Telegram account – install their app on your phone, and get it set up.

Next, start a conversation with the “[BotFather](https://t.me/BotFather)”. This is a bot that Telegram themselves run, and it controls the creation and registration of bots on their platform. On the Android version of their app, here’s what you do (other platforms are similar)

- To start a new chat, tap the start conversation button in the bottom right corner.
- Tap the magnifying glass “Search” icon near the top right.
- Type “botfather”. or click on [@botfather](https://t.me/BotFather)
- Tap on the “@BotFather” that appears. Make sure it has a blue checkmark next to it.
- It will show a greeting message.
- Click the “Start” button.
- Send it a message “/newbot”
- It will prompt you to give your bot a name. I'm going to title mine "amrohanbot," but you should come up with something original.
- It will then ask for a username, which I will use as "amrohanbot."
- If everything goes well, it will print a message stating that the bot has been created. There's one crucial piece of information in there that you'll need later: the HTTP API access token. It'll be a long string of alphanumeric characters, possibly including a colon. I copied the message to my phone and then emailed it to myself to save it for later — not super-secure, but probably safe enough if you're not going to put anything sensitive into your bot.

So, even if your bot isn't very vocal right now, let's double-check that it's been made. Start a conversation with it by following the same steps that you did with the BotFather. Hopefully, you'll be able to find it and start a chat, but nothing happens when you hit the "Start" button.

No big surprise there. Let’s make it do something.

Begin the installation process after the bot has been created.

## Installation

The steps to execute this on your local machine are as follows:

1. Clone the given repo :

```
  git clone https://github.com/amrohan/ChatBot
```

1. After that install requirement.txt

```
 pip instal -r requirement.txt
```

OR

You can manually install packages by using the commands listed below.

`pip install python-telegram-bot`

Because with dot env installed, we can save and import our telegram bot api key.

```
pip install python-dotenv
```

Create .env file in the root folder of your cloned GitHub repo and add your botfather telegram bot token.

```
Bot_Token = {Telegram Bot Token}
Dev_Token = {dev.to api token}
```

Now just run the `[main.py](http://main.py)` in terminal.

Now that your python bot is fully functional, simply modify the file in response py to add responses, and in mainpy, you'll notice def functions that are used in the telegram bot. Simply build the function and add it to the command handeler.

## Deploying bot on Heroku :

1. If you don't already have one, create one on Heroku [Login](https://id.heroku.com/login)
2. Now just create new app on Heroku.
3. Connect your GitHub repository, which is where you have uploaded your code.
4. After connecting it just click on deployed
5. Simply go to settings and add config variables while it's being deployed. Add API Key and your Telegram bot token in value by clicking on it.
6. Go to dyno and turn it on; your bot will now be fully functional.
7. Now all you have to do is go to Telegram and start using it.

### Deploying tutorial :

[![Python Telegram Bot Video](https://res.cloudinary.com/marcomontalbano/image/upload/v1628913692/video_to_markdown/images/youtube--XnoZ9zxwnCQ-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/XnoZ9zxwnCQ "Python Telegram Bot")
That's how you got your Telegram bot up and running on Heroku.

### Contact

If you have any questions or don't understand any of the instructions, please let me know. 👉 [@amrohan](mailto:hello@rohan.ml) .
