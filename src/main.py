'''
main.py
    - Main run file
'''
import gen.utils.sceneManager as sceneManager
import gen.utils.log as logger

FAILURE_CODE = 0
SUCCESS_CODE = 1
SCENE_CALL_CODE = 2



def main():
    Logger = logger.Logger()
    SceneManager = sceneManager.SceneManager(Logger)

    for scene in range(SceneManager.numSequenced):
        exit_code, *args = SceneManager.runSequencedScene(scene)


        if exit_code is SCENE_CALL_CODE:

            SceneManager.runExtraScene(args[0])


            SceneManager.runReturnScene(scene)
            

    


if __name__ == "__main__":
    main()