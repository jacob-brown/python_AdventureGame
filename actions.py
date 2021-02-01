def characterMoveOptions(mapObj, characterObj):
    tmpWorldMapList = list(mapObj.worldMap)
    indexCurrentLoc = tmpWorldMapList.index(characterObj.location.roomID)
    indexNextToCurrent = [indexCurrentLoc - 1, indexCurrentLoc + 1]
    directionOptions = [tmpWorldMapList[i] for i in indexNextToCurrent]
    return directionOptions


def userInputUntilCorrect(validCases, prompt="", exitMessage=""):
    adjustedPrompt = "> " + prompt + "\t"
    while True:
        userInput = int(input(adjustedPrompt))
        if userInput in validCases:
            print(exitMessage)
            break
        else:
            print("impossible! try again...")
            continue
    return int(userInput)


def executeUpdateCharacterLocation(mapObj, characterObj, newLocationIndex):
    # i can refactor from here
    print(
        characterObj.name
        + " is moving from the "
        + characterObj.location.name
        + " to the "
        + mapObj.worldRooms[newLocationIndex].name
    )
    # to here
    characterObj.location = mapObj.worldRooms[newLocationIndex]
    return 0


def moveCharacterUserDecision(mapObj, characterObj):
    moveOptions = characterMoveOptions(mapObj, characterObj)
    moveText = "where would you like to move? " + str(moveOptions)

    moveSelection = userInputUntilCorrect(
        validCases=moveOptions,
        prompt=moveText,
        exitMessage="",
    )
    executeUpdateCharacterLocation(mapObj, characterObj, moveSelection)
    return 0