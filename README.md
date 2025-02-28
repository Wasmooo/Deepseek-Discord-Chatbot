Discord Chat Bot that uses Deepseek.

[![X (formerly Twitter) URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Fx.com%2Fyesttd)](https://x.com/yesttd)
[![PayPal](https://img.shields.io/badge/PayPal-003087?logo=paypal&logoColor=fff)](https://paypal.me/waseemkurabi)



Setting custom personalities for different users is possible.
The default prompt of the bot is always used, adding custom personalities gives it info about a specific user.
needs alot of work, but it functions

# **Instructions**


After making the bot in the developer hub, scroll down to the "Privileged Gateway Intents" section.
Enable "Message Content Intent" (this allows the bot to read messages).
Click "Save Changes".


Click "OAuth2" > "URL Generator".
Under "Scopes", select "bot".
Under "Bot Permissions", select:
Read Messages
Send Messages
Mention Everyone
Use Slash Commands
Message Content (IMPORTANT)
Copy the generated URL and open it in your browser.
Select your server and click authorize

in the requirements.in folder all the modules you need to install are listed.
put bot and api token in the .env
all other manually entered stuff is shown in bot.py
to set and remove personalities for specific people use the /setpersonalities command and /removepersonalities


