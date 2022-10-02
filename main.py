# pin-out 
from time import sleep
from robot.main import mainFunc as robot
from UpdateUtil.main import main as runUpdate


updatePin:bool = True
robotPin:bool = False


if __name__ == "__main__":
    # run main robot script
    while True:
        if (robotPin):
            robot()
        # run updater script
        elif (updatePin):
            runUpdate()
        else:
            sleep(0.2)
        

