# NOTE - Check out [this repo](https://github.com/Awesome-Logic/Logic-BS-Server-Source) for non encrypted version.

# Logic Server

This is an encrypted copy of Logic Server for BombSquad.
This only works on Linux for now.

The data/scripts folder is untouched, so the host can still edit the scripts, add mods and further edit the server.

The server allows a single host to use his account_id and run multiple parties that use the same database. The data is saved on my servers, meaning that the host does not need to take stupid backups everyday to prevent data loss. It all just works!

## Installation

Just use the following commands on any Linux Machine (preferably hosted  on cloud) and you should have a working copy in a few minutes.

You also need to make a config.py and add your account_id to admin_id variable. You can also edit different server setting.

```bash
sudo apt -y update
sudo apt install -y python python2.7 libsdl2-2.0.0 libpython2.7 python-pip git
git clone https://github.com/Awesome-Logic/Logic-Server.git
cd Logic-Server
cp config-sample.py config.py
nano config.py
```


**Important: Make sure that you properly edit the config file to ensure proper functioning.**

## Usage

The Server automatically creates a 'data' folder outside the Logic-Server folder. The contents of this folder can be used to:
- Add some more words to the abusive filter (filtered-words.txt)
- Add a help page (help.txt)
- Add a flyer (text that appears in the beginning of every match and smoothly transitions out after sometime) (flyer.txt)

Once the server is up and running, use '/admin <player_name/id/cliend_id>' to make more admins

To update the server, simply use git pull.
```bash
cd Logic-Server
git pull
```
The server will stop working if it finds a new version and is not updated.

## Feature Requests
Discord - [RAGE](https://discord.com/invite/XwNTJDU)

Telegram - @AwesomeLogic

## Feature Requests
For changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

