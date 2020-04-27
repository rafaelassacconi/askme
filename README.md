# AskMe

AskMe is a Python program that allow you to search questions and answers on the internet using keywords.


## 1. Links

- [Original instructions](https://github.com/rafaelassacconi/askme/blob/master/docs/TEST.md)
- Project activities on [Trello Kaban Board](https://trello.com/b/bd38bLJn/askme)
- Starck Overflow [Wrapper on GitHub](https://github.com/rafaelassacconi/stackoverflow)

## 2. Running the program

### 2.1 Virtualenv

Install pip, virtualenv and virtualenvwrapper packages:
```
sudo apt-get install python3-pip
sudo pip3 install virtualenv virtualenvwrapper
```
For configure the VirtualEnvWrapper, edit the file `/home/user/.bashrc`:
Include the content bellow at the end of the file:
```
# Python Virtualenvs 
export WORKON_HOME=/home/user/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
source /usr/local/bin/virtualenvwrapper.sh 
export PIP_REQUIRE_VIRTUALENV=true 
```
Restart the terminal and run the command bellow to create a virtualenv:
```
mkvirtualenv askme
```

### 2.2 Prepare the project
Clone this repository and access to the folder:
```
git clone https://github.com/rafaelassacconi/askme.git
```
Activate the virtualenv:
```
workon askme
```
Install the packages required:
```
pip install -r requirements.txt
```

### 2.3 Run the command line program
Run the command bellow to execute the program:
```
python askme.py
```
For execute the program with all the parameters:
```
python askme.py --keywords=html --items=20
```
To get help, use the `--help` parameter:
```
python askme.py --help
```
Help command result:
```console
Usage: askme.py [OPTIONS]

  AskMe use keywords to search related questions  and answers on the
  internet.

Options:
  --keywords TEXT  Keywords to search related questions and answers.
  --items INTEGER  Max number of items that will be returned.
  --help           Show this message and exit.
```

### 2.4 Run as a Telegram bot
Run the command bellow to start bot:
```
python askme_telegram_bot.py
```

On Telegram, chat with the user `@askme_telegram_bot`.

Press `Ctrl-C` on the command line to stop.


### 2.5 Tests
For run the tests, install the `pytest` package and run the command bellow:
```
pytest
```