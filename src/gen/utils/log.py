'''
log.py
    - This provides functionality to log things to the game's logs
'''
import json
from colorama import Fore
import datetime
import pytz
import gen.utils.settings as settings

'''
Logger
    - Contains all the functions to manage logs
    - Functions beginning in _ are only really meant to be used in the class itself
'''
class Logger():
    def __init__(this):
        this.devSettings = settings.SettingsManager().getDevSettings()
    
    def _writeLogData(this, type, data):
        return f"[{this._getTimeDate()}] - {type}: {data}\n"

    def _getTimeDate(this):
        current = datetime.datetime.now(pytz.timezone('America/New_York'))
        return current.strftime('%x - %X')

    def info(this, data):
        if this.devSettings["logLevel"] != "all":
            return 0

        logMessage = this._writeLogData("INFO", data)

        if this.devSettings["printInfoLogs"]:
            print(logMessage)

        with open('./logs/all.log', 'a') as f:
            f.write(logMessage)
        
        return 1
    
    def error(this, data):
        logMessage = this._writeLogData("ERROR", data)

        if this.devSettings["printErrorLogs"]:
            print(logMessage)

        with open('./logs/all.log', 'a') as f:
            f.write(logMessage)
        
        return 1
    
    def warning(this, data):
        if this.devSettings["logLevel"] != "warning" or this.devSettings["logLevel"] != "all":
            return 0
    
        logMessage = this._writeLogData("WARNING", data)

        if this.devSettings["printWarningLogs"]:
            print(logMessage)

        with open('./logs/all.log', 'a') as f:
            f.write(logMessage)
        
        return 1