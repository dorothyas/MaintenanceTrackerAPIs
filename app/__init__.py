from flask import Flask
#Initialise the app

app= Flask(__name__, instance_relative_config=True)

# setting instance_relative_config to True, we can use
#app.config.from_object('config') to load the config.py file.

#Load the views
from app import views

#Load config file
app.config.from_object('config')