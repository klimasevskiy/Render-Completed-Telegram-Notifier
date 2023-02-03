# Render Completed Telegram Notifier Add-on

![Group (2).png](Render%20Completed%20Telegram%20Notifier%20f167d06371a041b59f3c60094bde3b83/Group_(2).png)

# **A Simple Blender Add-on that sends a Telegram message when a render is complete.**

## Features

- Sends a message to Telegram indicating that a render has completed.
- Includes project filepath in the message.
- Change **bot`s token** and **chat id** directly in blender

## Requirements

1. Blender 3.3.0 (if you tested this addon on other versions, contact me: [telegram](https://file+.vscode-resource.vscode-cdn.net/d%3A/python/telegram%20notificator%20addon/t.me/klimasevskiy))
2. A Telegram bot with a valid bot token and a chat ID

## Installation

1. Download the repository and extract "Telegram render notifier.py".
2. Open Blender and go to **Edit > Preferences > Add-ons**
3. Click Install... and select the **"Telegram render notifier.py"**.
    
    ![Untitled](Render%20Completed%20Telegram%20Notifier%20f167d06371a041b59f3c60094bde3b83/Untitled.png)
    
4. Enable the Add-on in the preferences panel.
    
    ![Untitled](Render%20Completed%20Telegram%20Notifier%20f167d06371a041b59f3c60094bde3b83/Untitled%201.png)
    

## Usage

1. In Blender, go to **Edit > Preferences > Add-ons > Render Completed Telegram Notifier.**
2. Enter your Telegram **bot's token** and **chat ID** in the Render Completed Telegram Notifier section.
    
    ![Untitled](Render%20Completed%20Telegram%20Notifier%20f167d06371a041b59f3c60094bde3b83/Untitled%202.png)
    
3. Start a render and the Add-on will send a message to Telegram once the render is complete.
    
    ![Untitled](Render%20Completed%20Telegram%20Notifier%20f167d06371a041b59f3c60094bde3b83/Untitled%203.png)
    

## How to create a Telegram bot and receive a bot token and chat ID:

1. Start a chat with the [BotFather](https://t.me/BotFather) by searching for @BotFather in Telegram.
    
    ![Untitled](Render%20Completed%20Telegram%20Notifier%20f167d06371a041b59f3c60094bde3b83/Untitled%204.png)
    
2. Send the command /newbot to create a new bot.
3. Enter a name for your bot and choose a username for it. *The username must end with bot.*
    
    ![Untitled](Render%20Completed%20Telegram%20Notifier%20f167d06371a041b59f3c60094bde3b83/Untitled%205.png)
    
4. The BotFather will give you a token, which is your bot's API key.
5. Start a chat with your newly created bot.
6. Send the command /start.
7. Find the chat_id by sending a message to the bot and then sending a GET request to ***https://api.telegram.org/bot<BOT_TOKEN>/getUpdates*** in your web browser.
8. The chat_id will be found in the response, under the key message.chat.id. 
    
    ![Untitled](Render%20Completed%20Telegram%20Notifier%20f167d06371a041b59f3c60094bde3b83/Untitled%206.png)
    

## Uninstalling

1. Go to Edit > Preferences > Add-ons.
2. Find the Render Completed Telegram Notifier in the list
3. click Remove.
