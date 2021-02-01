import numpy as np
import room
import mapbuilding
import actions
import character

np.random.seed(12345)

#  make the world
newWorld = mapbuilding.mapOfWorld(8)
newWorld.makeRandomMap()
newWorld.addRoomsToWorld()

# make characters
jacob = character.character(
    "jacob", 100, 20, "rain", "hello I am jacob", newWorld.worldRooms[0]
)

taco = character.character(
    "taco", 30, 2, "rain", "I am a taco", newWorld.worldRooms[5]
)

# execute the move
actions.moveCharacterUserDecision(newWorld, jacob)
