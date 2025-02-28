Discord Chat Bot that uses Deepseek.

![paypal.me/waseemkurabi](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)
![[Discord](https://discordapp.com/users/1274480796547289222)](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
![[X](https://x.com/yesttd)](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)

Setting custom personalities for different users is possible.
The default prompt of the bot is always used, adding custom personalities gives it info about a specific user.


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

needs alot of work, but it functions
