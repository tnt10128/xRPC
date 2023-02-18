# 🎮 xRPC
Simple console program that lets you customize your Discord rich presence.

![GNU GPL v3](https://img.shields.io/github/license/tnt10128/xRPC?style=for-the-badge)
![Codefactor code quality](https://img.shields.io/codefactor/grade/github/tnt10128/xRPC?style=for-the-badge)

## ℹ️ Description
xRPC allows you to customize your Discord rich presence. You can specify your own text,
images, and buttons that will be displayed on your Discord profile whenever the program
is running.

## ❓ How to use
> **Before you begin:** Make sure **Python 3** is installed on your computer!

1. `git clone https://github.com/tnt10128/xRPC` and `cd xRPC`
2. `python3 -m pip install -r requirements.txt`
3. Go to the Discord Developer Portal, create a new application, and copy the Application ID. Paste it into the `client_id` section of the config.json file.  
4. Modify the values in config.json as you wish.
5. Start the app with `python3 main.py`. If your config file is not named "config.json", add the name of your config file as an argument.