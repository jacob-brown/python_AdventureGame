class room:
    def __init__(self, roomID, name, description):
        self.__id = roomID  # map used to set newID
        self.__name = name
        self.__description = description

    @property
    def roomID(self):
        return self.__id

    @roomID.setter
    def roomID(self, idIn):
        self.__id = idIn

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nameIn):
        self.__name = nameIn

    @property
    def description(self):
        descriptionOfRoomToBePrinted = (
            "\nRoom: "
            + self.name
            + "\n-------\n"
            + self.__description
            + "\n-------\n"
        )
        return descriptionOfRoomToBePrinted

    @description.setter
    def description(self, descriptionIn):
        self.__description = descriptionIn
