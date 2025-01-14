# **ReadMyChatPlease**

A solo-developed Twitch chat message-forwarding program, made for self-use, but feel free to do as you wish.

## Description

This project combines a TwitchAPI bot with a client-side socket server to forward Twitch chat messages to a designated socket server. It operates as follows:

1. **TwitchAPI Bot**: The bot connects to a Twitch channel and listens for incoming messages in real-time.

2. **Client-Side Socket Server**: The client-side socket server establishes a persistent connection to a pre-configured external socket server.

3. **Message Forwarding**: The bot captures Twitch chat messages and logs them into a temporary .txt file. A watchdog module monitors this file, captures new messages, then forwards them to the socket server that the client is connected to.


It was built originally for personal use, but I liked the idea so I made it more maintanable and improved it. 

## Requirements:

You can install these dependencies manually, but ReadMyChat please will do it for you automatically upon running `main.py` (provided you have Python installed)

**TwitchAPI**:
```
python -m pip install twitchapi
```
**Python-dotenv**:
```
python -m pip install python-dotenv
```
**watchdog**:
```
python -m pip install watchdog
```

# How to use:

- Clone the repository in any directory

```
git clone https://github.com/davididwhat/readmychatplease.git
```

- Navigate to the `./readmychatplease/` directory and open **`.env`** in an editor of your choice

| Variables  | Values |
| ------------- |:-------------:|
| CLIENT_ID      | Twitch application ID     |
| APP_SECRET      | Twitch application secret    |
| CHANNEL_NAME      | Twitch channel username|
|-------------------|---------------------------|
|ADDRESS|Socket server host IP|
|PORT|Socket server running port|
|-------------------|---------------------------|
|TEMP_FILE|temp.txt, don't change|

*Get your ID and Secret at [Twitch Developer Console](https://dev.twitch.tv/console/)*

- in `./readmychatplease/standalone/` you will find **`server.py`** , you may use your own but I will continue writing this part assuming you are using the socket server provided as an example in this project.
- Transfer **`server.py`** onto a device you plan to use as your reading screen (Make sure the device uses the same LAN as your main device, otherwise you will have to port-forward), and change the variables `HOST` and `PORT` at the bottom according to the comment.

- Run the server (assuming from within its directory)::
```
python server.py
```

- Run ReadMyChatPlease (assuming from within its directory):
```
python ./src/main.py
```

You should now have a bond between both devices and your Twitch messages should be forwarded to the socket server instantly.


### \*gulp*

![](https://raw.githubusercontent.com/davididwhat/readmychatplease/refs/heads/main/mascot.png)

