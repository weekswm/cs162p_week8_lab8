#Car class
class Car:
    '''Creates a class Car
    attributes: make, color, and year
    '''
    def __init__(self, make = 'Ford', color = 'black', year = 1910):
        '''Creates a car with the provided make, color, year.
        Defaults to Ford black 1910.
        '''
        self.make = make
        self.color = color
        self.year = year

    '''Getters and Setters for make, color, and year
    '''
    #Getter and Setter for make
    def getMake(self):
        return self.make

    def setMake(self, newMake):
        self.make = newMake

    #Getter and Setter for color
    def getColor(self):
        return self.color

    def setColor(self, newColor):
        self.color = newColor

    #Getter and Setter for year
    def getYear(self):
        return self.year

    def setYear(self, newYear):
        self.year = newYear

    # Overloading equality operator
    def __eq__(self, differentCar):
        '''Overloaded equality operator.  
        Returns True if color, year, and make match
        '''
        return (self.make == differentCar.make and self.color == differentCar.color and self.year == differentCar.year)

    def __str__(self):
        #Returns string of color, year, and make of Car 
        return ("%s %s %s" % (self.color, self.year, self.make))