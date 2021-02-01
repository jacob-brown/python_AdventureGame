import numpy as np
import room


class mapOfWorld:
    def __init__(self, mapSizeBlocks):
        self.mapSizeBlocks = mapSizeBlocks
        self.worldMap = []
        self.worldRooms = {}

    @property
    def worldMap(self):
        return self.__worldMap

    @worldMap.setter
    def worldMap(self, newMap):
        self.__worldMap = newMap

    def makeRandomMap(self):
        self.__worldMap = np.arange(self.mapSizeBlocks)
        np.random.shuffle(self.__worldMap)

    def addRoomsToWorld(self):
        roomTypes = [
            "kitchen",
            "dinning",
            "lounge",
            "bathroom",
            "cave",
            "library",
        ]

        descriptionTypes = [
            "kitchen description",
            "dinning description",
            "lounge description",
            "bathroom description",
            "cave description",
            "library description",
        ]

        for i in self.worldMap:

            # randomly select room and description
            roomSelectedRandomly = np.random.choice(roomTypes, replace=False)

            descriptionSelectedRandomly = np.random.choice(
                descriptionTypes, replace=False
            )

            # make a dictionary of room objects
            self.worldRooms[i] = room.room(
                roomID=i,
                name=roomSelectedRandomly,
                description=descriptionSelectedRandomly,
            )