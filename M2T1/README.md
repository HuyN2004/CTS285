# M2T1 - Webapp #1

## goals:
- to learn basic Flask programming 
- to be able to repeat a server config
- maybe to have fun

## lessons
bash command you cannot live without:
- ls <- whatin this directory
- cd <-change directory
- source <- run a script (like activate)

## instructions
initial tutorial: https://blog.pythonanywhere.com/121/
but we're using codespaces instead of PA

install library:

first set up virtualenviroment
- pip install virtualenv
- virtualenv venv
- soure venv/bin/activate
now we have our "venv" enviroment, so we can install things in it
to  turn it off:
- source venv/bin/deactivate

start installing requirements:
- pip install flask
- pip freeze > requirements.txt

now we can write minimal Flask app to test it
TODO: write a Flask app that does something userful

to start:
- flask --debug --app hello run

## M2T2
Next, we start with "a first cut with dummy data"
- add main_page.html
