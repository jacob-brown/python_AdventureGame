class character:
    def __init__(
        self, name, healthPoint, strength, weakness, greeting, location
    ):
        self.name = name
        self.healthPoint = healthPoint
        self.strength = strength
        self.weakness = weakness
        self.greeting = greeting
        self.location = location  # room object
        self.killedList = []

    # health
    @property
    def healthPoint(self):
        return self.__healthPoint

    @healthPoint.setter
    def healthPoint(self, newHealthPoint):
        if newHealthPoint <= 0:
            print(self.name + " has died.")
            self.__healthPoint = 0
        else:
            self.__healthPoint = newHealthPoint

    # speaking and information
    def speak(self):
        print(self.greeting)
        return 0

    def getKills(self):
        print(self.name + " has killed the following characters: ")
        print(self.killedList)
        return 0

    # attacking and healing
    def attack(self, opponent):
        print(self.name + " is attacking " + opponent.name)
        opponent.healthPoint = opponent.healthPoint - self.strength
        if opponent.healthPoint > 0:
            print(opponent.name + "(hp): " + str(opponent.healthPoint))
        else:
            self.killedList.append(opponent.name)
        return 0

    def heal(self, healValue):
        self.__healthPoint = self.__healthPoint + healValue
        print(self.name + " was healed.")
        print(self.name + "(hp): " + str(self.__healthPoint))

    # location and movement
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, newlocation):
        self.__location = newlocation
