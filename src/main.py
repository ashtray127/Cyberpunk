'''
main.py
    - Calls scenes
    - Scene types:
        - Sequenced 
            - These are story scenes, where you progress through the sequence of them as it goes along.
        - Extra
            - These are scenes that can be called from other scenes, like battles
'''
import os
import importlib

'''
getScenes
    - Gets all the scenes inside of the scenes folder
    - Returns the list of sequenced scenes in a list and the extra scenes in a list
'''
def getScenes():
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
                raise Exception("Scene Sequence is double assigned") 
            sequencedScenes[sceneData.sequence] = sceneData
        else:
            extraScenes[sceneData.name] = sceneData
    
    return sequencedScenes, extraScenes

def main():
    sequencedScenes, extraScenes = getScenes()

    


if __name__ == "__main__":
    main()