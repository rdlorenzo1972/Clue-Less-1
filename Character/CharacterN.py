'''
Created on Oct 25, 2017

@author: Zack
'''
from location import Room, Hallway
import inspect

class Character(object):
    '''
    Possible suspects that move to varies locations on the game board.
    
    TODO think of something better for location
    '''


    def __init__(self, characterType, location):
        '''
        Constructor
        '''
        self.characterType = characterType
        self.location = location
    
    def __str__(self):
        return self.characterType.name
    
    def __repr__(self):
        return self.characterType.name
        
    def current_location(self):
        print(self.location)
        
    def available_moves(self):
        
        print("{} is currently in the {}".format(self, self.location))
        self.location.show_connecting_locations()
        return self.location.return_connecting_locations()
         
    def move_location(self, selection):
        
        connectingLocations = self.available_moves()
        result = False
        
        for location in connectingLocations:
            if selection == location.__str__():
                if location.available_to_enter():
                    print('{} is available to enter {}'.format(location,location.available_to_enter()))
                    #Change current location to unoccupied
                    if isinstance(self.location, Hallway):
                        print("Freeing current location")
                        self.location.occupied = False
                    #if moving to a hallway change it to occupied
                    if isinstance(location, Hallway):
                        print("Occupied new Hallway")
                        location.occupied = True
                    print("{} was able to enter the {}".format(self, location))
                    self.location = location
                    result = True
                else:
                    print("Could not enter {}, it was occupied".format(location))
                break
        else:
            print("Input location not found")
            
    
        return result   
 