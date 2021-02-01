import sys
import numpy as np
import room
import mapbuilding
import character


def main(argv):
    # setup
    np.random.seed(12345)
    numberBlocksInWorld = 8

    # build world
    newWorld = mapbuilding.mapOfWorld(numberBlocksInWorld)
    newWorld.makeRandomMap()
    newWorld.addRoomsToWorld()

    # make characters
    jacob = character.character(
        "jacob", 100, 20, "rain", "hello I am jacob", newWorld.worldRooms[0]
    )
    taco = character.character(
        "taco", 30, 2, "hungry people", "taco, I am", newWorld.worldRooms[5]
    )

    print(jacob.location.roomID)
    print(taco.location.roomID)
    print(newWorld.worldMap)
    return 0


if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
