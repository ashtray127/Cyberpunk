import json

class SettingsManager:
    def __init__(this):
        this.devSettingsFile = "./gen/data/devsettings.json"
    
    def getDevSettings(this):
        with open(this.devSettingsFile, "r") as f:
            devSettings = json.load(f) 

        return devSettings