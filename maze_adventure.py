from collections import deque
from copy import deepcopy
from typing import Deque, Dict, Generic, List, Set, Tuple, TypeVar
from xmlrpc.client import Boolean
from stack_queue import Stack, Queue
T = TypeVar("T")

ROOM_KEY = "room_name"
TIME_NEEDED_KEY = "time_needed"
TIME_SPENT_IN_ROOM_KEY = "time_spent"
TIME_TAKEN_TO_ARRIVE_HERE_KEY = "time_taken"
VISITED_ROOMS_KEY = "visited_rooms"

class MazeRoom:
    def __init__(self, rooms_you_can_go_to: List[Dict], item: str = None, requires: str = None) -> None:
        self.rooms_you_can_go_to: List[Dict] = rooms_you_can_go_to

class Maze:

    # Constructor
    def __init__(self, maze: Dict, start_room: str, end_room: str) -> None:  
        self.maze: Dict = maze
        self.start_room: str = start_room
        self.end_room: str = end_room
        # queue that will hold all the possible branches
        self.branches = Queue()
        # to keep track if a valid path has been found
        self.valid_path_found: bool = False
   

    def solve_maze(self) -> Stack[Dict]:
        '''enqueues a stack that just has one Dictionary that holds the room_name & time_taken'''
        start_room_dictionary: Dict = {ROOM_KEY:self.start_room, TIME_TAKEN_TO_ARRIVE_HERE_KEY:0, VISITED_ROOMS_KEY:{self.start_room}, TIME_SPENT_IN_ROOM_KEY : 0}
        beginning_stack: Stack = Stack()
        beginning_stack.push(start_room_dictionary)
        self.branches.enqueue(beginning_stack) 
        
        '''iterate over each stack in the queue while a valid path hasn't been found and the queue isn't empty'''
        while (not self.valid_path_found and not self.branches.is_empty()): 
            # dequeue a stack from self.branches, enqueue the proper amount of valid paths you can take
            current_path: Stack[Dict] = self.branches.dequeue()
            recent_room: Dict = current_path.peek()

            # increment time spent in the room (TIME_TAKEN_TO_ARRIVE_HERE_KEY)
            recent_room[TIME_SPENT_IN_ROOM_KEY] += 1

            # recent_room[TIME_TAKEN_TO_ARRIVE_HERE_KEY] = recent_room[TIME_TAKEN_TO_ARRIVE_HERE_KEY] + 1


            unvisited_rooms: Boolean = False
            room_added: Boolean = False
            if not len(self.maze[recent_room[ROOM_KEY]].rooms_you_can_go_to) == 0:
                # look at the rooms_you_can_go_to of the top room by accessing the corresponding MazeRoom object in self.maze using the room_name
                # List of rooms (dictionaries) recent_room can go to -> self.maze[recent_room[ROOM_KEY]].rooms_you_can_go_to
                for visitable_room in self.maze[recent_room[ROOM_KEY]].rooms_you_can_go_to:
                    # visitable_room is a Dict with a ROOM_KEY/"room_name" and TIME_NEEDED_KEY/"time_needed" of a room that recent_room can go to
                    # first check if you can go to this room (compare with set of visited rooms and also compare if you've spent enough time in the recent_room)
                    '''need to make sure if all the rooms you can go to have already been visited in the set. If so, just leave the stack dequeued'''
                    # check if the set from the recent_room contains the ROOM_KEY of visitable_room
                    # check if the time spent in recent_room (TIME_TAKEN_TO_ARRIVE_HERE_KEY) matches the time needed to go to visitable room (TIME_NEED_KEY)

                    if not visitable_room[ROOM_KEY] in recent_room[VISITED_ROOMS_KEY]:
                        unvisited_rooms = True
                        if recent_room[TIME_SPENT_IN_ROOM_KEY] == visitable_room[TIME_NEEDED_KEY]: 

                            # the visitable room is confirmed, now add the room to a copy of the stack and enqueue it, resetting any values like TIME_TAKEN_TO_ARRIVE_HERE_KEY
                            current_path_copy: Stack[Dict] = deepcopy(current_path)
                            recent_room[VISITED_ROOMS_KEY].add(visitable_room[ROOM_KEY])
                            carryover_set: set() = deepcopy(recent_room[VISITED_ROOMS_KEY])
                            carryover_set.add(visitable_room[ROOM_KEY])
                            #current_path_copy.peek()[VISITED_ROOMS_KEY].add(visitable_room[ROOM_KEY])
                            # carryover_set: set() = deepcopy(recent_room[VISITED_ROOMS_KEY])
                            #  current_path_copy.peek()[TIME_TAKEN_TO_ARRIVE_HERE_KEY] += 1

                            # the values I need to put into the room I am adding {ROOM_KEY, TIME_TAKEN_TO_ARRIVE_HERE_KEY, VISITED_ROOMS_KEY}
                            # add the valid room to a copy of the stack
                            # current_path_copy.push(recent_room) commenting this out
                            current_path_copy.push({ROOM_KEY : visitable_room[ROOM_KEY], TIME_TAKEN_TO_ARRIVE_HERE_KEY : visitable_room[TIME_NEEDED_KEY] , VISITED_ROOMS_KEY : carryover_set, TIME_SPENT_IN_ROOM_KEY : 0})
                            room_added = True
                            # check if the room you are going to is the end_room (meaning you're done!)
                            if visitable_room[ROOM_KEY] == self.end_room:
                                # current_path_copy.peek()[TIME_TAKEN_TO_ARRIVE_HERE_KEY] == 1 # probably not the solution
                                return current_path_copy
                            
                            
                            # enqueue this stack
                            self.branches.enqueue(current_path_copy)
                
                '''if all the visitable rooms have already been visited, you can dequeue the stack and forget 
                but if you just need to wait longer in this room, then requeue it'''
                if unvisited_rooms == True: #and room_added == False
                    # current_path.push(recent_room)
                    self.branches.enqueue(current_path)
                    unvisited_rooms = False
        return None
                    
                    
    def implements_locked_room_extension(self) -> bool:
        return False