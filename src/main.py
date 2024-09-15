'''
main.py
    - Main run file
'''
import gen.utils.sceneManager as sceneManager
import gen.utils.log as logger
import gen.utils.settings as settings

FAILURE_CODE = 0
SUCCESS_CODE = 1
SCENE_CALL_CODE = 2

def main():
    Logger = logger.Logger()
    SceneManager = sceneManager.SceneManager(Logger)
    SettingsManager = settings.SettingsManager()

    for scene in range(SceneManager.numSequenced):
        Logger.info("Running sequeunced scene " + str(scene))
        exit_code, *args = SceneManager.runSequencedScene(scene)
        Logger.info("Scene " + str(scene) + " returned with exit code " + str(exit_code))

        if exit_code is SCENE_CALL_CODE:
            Logger.info("Running extra scene " + args[0])
            extra_exit_code = SceneManager.runExtraScene(args[0])
            Logger.info("Extra scene " + args[0] + " returned with code " + str(extra_exit_code))

            Logger.info("Running return scene of sequenced scene " + str(scene))
            return_exit_code = SceneManager.runReturnScene(scene)
            Logger.info("Return scene " + str(scene) + " returned with code " + str(return_exit_code))
            

    


if __name__ == "__main__":
    main()