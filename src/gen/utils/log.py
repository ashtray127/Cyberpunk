'''
log.py
    - This provides functionality to log things to the game's logs
'''
import json
from colorama import Fore
import datetime
import pytz

'''
Logger
    - Contains all the functions to manage logs
    - Functions beginning in _ are only really meant to be used in the class itself
'''
class Logger():
    def __init__(this):
        with open('./gen/data/logLevel.json', 'r') as f:
            this.level = json.load(f)["logLevel"]
    
    # Returns the date and time
    def _getTimeDate(this):
        current = datetime.datetime.now(pytz.timezone('America/New_York'))
        return current.strftime('%x - %X')

    def info(this, data):
        if this.level != "all":
            return 0

        log = f"[{this._getTimeDate()}] - INFO: {data}\n"

        with open('./logs/all.log', 'a') as f:
            f.write(log)
    
    def error(this, data):

        log = f"[{this._getTimeDate()}] - ERROR: {data}\n"

        with open('./logs/all.log', 'a') as f:
            f.write(log)