class Scene():
    def __init__(this):
        this.type = "sequenced"
        this.sequence = 0
        this.desc = "Introduction"
    
    def scene(this):
        print("First part of scene")

        return 2, "fight"

    def return_scene(this):
        print("Second part of scene")

        return 1