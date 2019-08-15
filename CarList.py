#CarList class
from Car import Car

class Link:
    '''Class to hold the value of an object (Car), 
    and a variable to hold the next node in the linked list.    
    '''
    def __init__(self, make, color, year):
        #Creates an empty car link.
        self.car = Car(make, color, year)
        self.next = None

class CarList:
    #Wrapper to handle Car links. Creates empty head link.
    def __init__(self):
        self.head = None

    def addCar(self, make, color, year):
        '''Creates a new car
        creates a new link that points to that car
        '''
        newCar = Link(make, color, year)
        #adds it to the head of the list
        newCar.next = self.head
        self.head = newCar

    def findCar(self, make, color, year):
        '''Creates a temporary car with inputs
        make, color, year. Returns True if found.
        '''
        cur = self.head
        wantedCar = Car(make, color, year)
        while cur:
            if cur.car == wantedCar:
                return True
            else:
                cur = cur.next
        return False

    def removeHead(self):
        '''if list is empty, returns none. 
        Otherwise returns the car at the head of the list
        and removes it from the list
        '''
        if self.head:
            headCar = self.head.car
            self.head = self.head.next
            return headCar
        else:
            return None

    def __str__(self):
        #Creates string displaying cars in list.
        if self.head == None: 
            return "No cars in list."
        cur = self.head
        curList = []
        while cur:
            curList.append(str(cur.car))
            cur = cur.next
        #cars should be listed one per line.
        return '\n'.join(curList)

    def __len__(self):
        cur = self.head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        return total

    
