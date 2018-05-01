"""
This module reads in a csv file containg state information and stores each state as
a State object in a list. It then presents a menu to the user, providing the options
1) Print a state report, 2) Sort by state name, 3) Sort by population, 4) Find and
print a state, 5) Quit. A choice carries out the specified action on the list of
states and allows the user to make other menu choices until they quit the program.
Python Version: 2.7.14

Author: Joseph Allen
Version: 1/26/2018
Email: joseph.allen@unf.edu
"""
from random import randint
import csv

class State:
    """
    This class creates State objects that store information about a US state and
    provides methods to get and set data attributes, compare two states based on
    name, and to return a printable string of State info.
    """
    numStateObjects = 0

    def __init__(self, name, cap, abbrv, pop, region, seats):
        """
        This function is the constructor for a State object. It is called with 6
        parameters: name, cap, abbrv, pop, region, and seats.
        :param name: The name of a US state & the 1st csv read.
        :param cap: The capital city of a US state & the 2nd csv read.
        :param abbrv: The abbreviation of a US state & the 3rd csv read.
        :param pop: The population of a US state & the 4th csv read.
        :param region: The geographical region a US state is in & the 5th csv read.
        :param seats: THe # of US House seats a state has & the 6th csv read.
        """
        self.name = name
        self.cap = cap
        self.abbrv = abbrv
        self.pop = pop
        self.region = region
        self.seats = seats
        State.numStateObjects += 1

    def __gt__(self, other):
        """
        This function compares the names of two State objects and returns True if
        the State object it is called on has a name that is (by ASCII values) greater
        than the name of the State object that is passed as the parameter 'other', and
        returns False otherwise.
        :param other: The State object to be compared
        :return: Returns True if the name of the state object it is called on has a
        name that is (by ASCII values) greater than the name of the State object that
        is passed as the parameter 'other', and returns False otherwise.
        """
        if self.getName() > other.getName():
            return True
        else:
            return False

    def __str__(self):
        """
        This function returns a string containing all of a State object's information.
        It is used to print out a state report to the program user.
        :return: Returns a string of State infromation.
        """
        return self.name.ljust(17)+self.cap.ljust(15)+self.abbrv.center(15)+self.pop.rjust(11)+"    "+self.region.ljust(17)+self.seats.rjust(12)

    def setName(self, name):
        """
        This function is used to update the name of a state.
        :param name: The name of a state.
        :return: Returns nothing.
        """
        self.name = name

    def getName(self):
        """
        This function is used to get the name of a state.
        :return: Returns a string containing the name of a State object.
        """
        return self.name

    def setCap(self, cap):
        """
        This function is used to update the capital city of a state.
        :param cap: The capital city of a state.
        :return: Returns nothing.
        """
        self.cap = cap

    def getCap(self):
        """
        This function is used to get the capital city of a state.
        :return: Returns the capital city of a State object.
        """
        return self.cap

    def setAbbrv(self, abbrv):
        """
        This function is used to set the abbreviation of a state's name.
        :param abbrv: The abbreviation of a state's name.
        :return: Returns nothing.
        """
        self.abbrv = abbrv

    def getAbbrv(self):
        """
        This function is used to get the abbreviation for a state's name.
        :return: Returns the abbreviation for the state name of a State object.
        """
        return self.abbrv

    def setPop(self, pop):
        """
        This function is used to set the population of a State object.
        :param pop: The population of a state.
        :return: Returns nothing.
        """
        self.pop = pop

    def getPop(self):
        """
        This function is used to get the population of a state.
        :return: Returns the population of a State object.
        """
        return self.pop

    def setRegion(self, region):
        """
        This function is used to specify which region a state is in.
        :param region: The geographical region of a state.
        :return: Returns nothing.
        """
        self.region = region

    def getRegion(self):
        """
        This function is used to get the region of a state.
        :return: Returns the region a particular state is in.
        """
        return self.region

    def setSeats(self, seats):
        """
        This function is used to specify the number of US House seats a state has.
        :param seats: The state's number of US House seats.
        :return: Returns nothing.
        """
        self.seats = seats

    def getSeats(self):
        """
        This function is used to get the number of US House seats a state has.
        :return: Returns the number of US House seats a state has.
        """
        return self.seats

    @classmethod
    def printNumStateObjects(cls):
        """
        This is a class method used to print the number of State objects created.
        :return: Returns nothing.
        """
        print(str(cls.numStateObjects)+" state records read.")
#//////////////////////////////////////////////////////////////////////////////////////////////////////
def printMenu():
    """
    This function is used to print the menu options for a user.
    :return: Returns nothing.
    """
    print("""\n1. Print a state report\n2. Sort by state name\n3. Sort by population\n4. Find and print a given state\n5. Quit""")
#-----------------------------------------------------------------------------------------------------
def printStateReport(states):
    """
    This function prints a state report by printing the type of the state information
    as column headers, and then calling __str__() on each state in the list parameter.
    :param states: The list containing State objects.
    :return: Returns nothing.
    """
    print("\nState Name".ljust(17)+"Capital City".ljust(15)+"State Abbr".center(15)+"Population".rjust(11)+"     Region".ljust(17)+"US House Seats".rjust(20))
    print("--------------------------------------------------------------------------------------------------")
    for state in states:
        print(state.__str__())
#-----------------------------------------------------------------------------------------------------
def sortByName(states):
    """
    This function is a Quick Sort which sorts a list of states according to state name.
    It is recursive in nature with the base case being when the function is passed a list
    with one state. The single element list is returned such that a string is built with
    all the states in proper order.
    :param states: The list of states to sort.
    :return: Returns a list of states sorted by name from lowest to highest (A-Z)
    """
    if len(states)<=1:
        return states
    lesser, same, greater = [],[],[]
    pivot = states[randint(0, len(states) -1)]          #pivot is chosen randomly
    for x in states:
        if x.__gt__(pivot):
            greater.append(x)
        elif x.getName() == pivot.getName():
            same.append(x)
        else:
            lesser.append(x)
    return sortByName(lesser) + same + sortByName(greater)
#------------------------------------------------------------------------------------------------------
def getMaxPopLength(states):
    """
    This function is used to find the number of digits in the largest state population.
    :param states: The list of states.
    :return: Returns the number of digits in the largest state population.
    """
    maxLength = 0
    for state in states:
        length = len(str(state.getPop().replace(',','')))       #ignores commas in the numbers
        if (maxLength < length):
            maxLength = length
    return maxLength
#-----------------------------------------------------------------------------------------------------
def sortByPop(states):
    """
    This function is a Radix Sort which sorts a list of states according to population.
    A bucket is allocated for each digit 0-9, and the population of each state determines
    which bucket it goes into. The least significant digit (righmost) of a population
    is considered on the first loop, and moves left after each subsequent loop. When all the
    states are in a bucket, the states are appended back to the states list from which they
    came. This process repeats until it has been done for each digit.
    :param states: The list of states to sort by population.
    :return: The list of states sorted by population.
    """
    buckets = [[],[],[],[],[],[],[],[],[],[]]               #buckets for digits 0-9
    base = 10
    numLoops = 0                        #will be used to signifiy the current digit as well
    maxLength = getMaxPopLength(states)
    while(numLoops < maxLength):        #until each digit has been sorted
        for state in states:
            factor = (base**(numLoops))     #number to divide the population by (gets rid of sorted numbers)
            bucketNum = (int(state.getPop().replace(',','')) / factor) % base
            buckets[bucketNum].append(state)
        del states[:]
        for z in range (0,base):            #buckets[x]
            bucket = buckets[z]
            for state in bucket:            #buckets[bucket[x]]
                states.append(state)
            del bucket[:]
        numLoops += 1
#-----------------------------------------------------------------------------------------------------
def binarySearch(states, key):
    """
    This function performs a binary search on a sorted list of State objects for a
    state with a specified name. It eliminates recursion by using a while loop
    and bisecting the range of the list after each pass. The current index changes
    depending on whether the state at that index in the list has a name that is the
    key, is greater than the key, or is less than the key.
    :param states: The sorted list of State objects.
    :param key: The string which is the state name to be searched for.
    :return: Returns the State object whose name matches the key, and None otherwise.
    """
    low = 0
    high = len(states) - 1
    while(True):
        current = (low + high) / 2
        if (states[current].getName() == key):
            return states[current]
        elif (low > high):
            return None
        else:
            if (states[current].getName() < key):
                low = current +1
            else:
                high = current - 1
#-----------------------------------------------------------------------------------------------------
def linearSearch(states, key):
    """
    This function performs a simple iterative search on the list of State objects.
    It iterates through the list comparing the name of each state object to the key.
    :param states: The unsorted list of states.
    :param key: The string which is the state name to be searched for.
    :return: Returns the State object whose name matches the key, and None otherwise.
    """
    for state in states:
        if state.getName().lower() == key.lower():
            return state
    return None
#-----------------------------------------------------------------------------------------------------
def printState(state):
    """
    This function prints a report for a single state.
    :param state: The State object whose information will be printed.
    :return: Returns nothing.
    """
    print("State Name:".ljust(20) + state.getName().ljust(15))
    print("Capital City:".ljust(20) + state.getCap().ljust(15))
    print("State Abbreviation:".ljust(20) + state.getAbbrv().ljust(15))
    print("State Population:".ljust(20) + state.getPop().ljust(15))
    print("Region:".ljust(20) + state.getRegion().ljust(15))
    print("US House Seats:".ljust(20) + state.getSeats().ljust(15))
#/////////////////////////////////////////////////////////////////////////////////////////////////////
#File Processing
filename = raw_input("Enter the file name: ")
states = []
try:
    f = open(filename, 'r')
except IOError:
    print 'Cannot open file'
reader = csv.reader(f, delimiter=',')
reader.next()           #skip first line headers
for row in reader:
    x = State(row[0], row[1], row[2], "{:,}".format(int(row[3])), row[4], row[5])
    states.append(x)
f.close()
State.printNumStateObjects()

#Program Interface
useMenu = True
sortedByName = False
while(True):
    if (useMenu == True):
        printMenu()
    choice = raw_input("Enter your choice: ")
    if (choice == '1'):
        printStateReport(states)
        useMenu = True
        continue
    elif (choice == '2'):
        states = sortByName(states)
        print("\nStates have been sorted by name.")
        sortedByName = True
    elif (choice == '3'):
        sortByPop(states)
        print("\nStates have been sorted by population.")
        sortedByName = False
    elif (choice == '4'):
        key = raw_input("Enter the state name: ")
        if (sortedByName == True):
            print("Binary search\n")
            state = binarySearch(states, key)
            if (state == None):
                print("Error: State {} not found.".format(key))
            else:
                printState(state)
        else:
            print("Linear search\n")
            state = linearSearch(states, key)
            if (state == None):
                print("Error: State {} not found.".format(key))
            else: printState(state)
    elif (choice == '5'):
        print("\nFarewell!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        useMenu = False