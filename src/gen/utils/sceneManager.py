import importlib
import os

'''
SceneManager
    - Manages Scenes
        - Gets scenes
        - Calls scenes
    - Scene types:
        - Sequenced 
            - These are story scenes, where you progress through the sequence of them as it goes along.
        - Extra
            - These are scenes that can be called from other scenes, like battles
'''
class SceneManager:
    def __init__(this, Logger):
        this.sequencedScenes, this.numSequenced, this.extraScenes = this.getScenes()
        this.Logger = Logger

    '''
    getScenes
        - Gets all the scenes inside of the scenes folder
        - Returns the list of sequenced scenes in a list and the extra scenes in a list
    '''
    def getScenes(this):
        sequencedScenes = [None] * 50
        extraScenes = {}

        for scene in os.listdir('./scenes'):
            if "pycache" in scene:
                continue 
            
            if not scene.endswith('.py'):
                continue 
            
            sceneData = importlib.import_module(f'scenes.{scene[:-3]}').Scene()

            if sceneData.type == "sequenced":
                if sequencedScenes[sceneData.sequence] is not None:
                    this.Logger.warning("Scene "+str(sceneData.sequence)+" is double assigned!")
                sequencedScenes[sceneData.sequence] = sceneData
            else:
                extraScenes[sceneData.name] = sceneData

        sequencedScenes = list(filter(lambda x: x is not None, sequencedScenes))

        return sequencedScenes, len(sequencedScenes), extraScenes

    '''
    runSequencedScene
        - Runs the code of a scene
    '''
    def runSequencedScene(this, sceneNum):
        return this.sequencedScenes[sceneNum].scene()
    
    '''
    runReturnScene
        - This will run the second part of a scene if that scene called a extra scene
    word salad
    '''
    def runReturnScene(this, sceneNum):
        return this.sequencedScenes[sceneNum].return_scene()

    '''
    runExtraScene
        - Runs extra scenes
    '''
    def runExtraScene(this, sceneName):
        return this.extraScenes[sceneName].scene()


