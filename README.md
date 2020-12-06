<!-- https://pypi.org/project/discord.py -->

# Water
Water is a discord bot based on water and made with discord.py and [Python](https://python.org "Python - https://python.org")

## Running your own instance
*This tutorial assumes that you have python installed, that you are on windows and you have some basic coding knowledge.*  

---
*Clone the repo*
```sh
git clone https://github.com/Irian3x3/water.git
```
*Modify [config.example.py](src/config.example.py), change the name to config.py*

---
*Start the bot:*  
```sh
py -3 src/bot.py
```
If it worked it should print the following:  
[![](https://i.imgur.com/EFLrh8s.png)](/#)  
If not, please create an issue.

### Info on running your own instance:
To import config, you have to create an `__init__.py` file in the folder where you are importing config. For example, say you have this folder structure:
```
src/
    cogs/
        some_cog.py
    config.py
```
And you wanna access config from cogs/some_cog. So, create a file called `__init__.py` in the `cogs` directory. This should allow you to import config.

## Contributing
### Way 1:
Fork the repo, clone your fork, make and commit your changes, submit a pull request!
### Way 2:
Create an issue suggesting the changes. That's it.
## Problems
Create an issue describing your problem.