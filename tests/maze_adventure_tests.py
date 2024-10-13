from unittest import TestCase
from maze_adventure import MazeRoom, ROOM_KEY, TIME_NEEDED_KEY, Maze, TIME_TAKEN_TO_ARRIVE_HERE_KEY

class MazeAdventureTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_linear_path(self):
        map = {
            "A" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}]),
            "B" :  MazeRoom([{ROOM_KEY:"A", TIME_NEEDED_KEY:1}])
        }

        maze = Maze(map, "A", "B")
        solution = maze.solve_maze()
        self.validate_entry(solution.pop(), "B", 1)
        self.validate_entry(solution.pop(), "A", 0)
    
    def test_all_rooms_same_size(self):
        map = {
            "A" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"C", TIME_NEEDED_KEY:1}]),
            "B" :  MazeRoom([{ROOM_KEY:"D", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"A", TIME_NEEDED_KEY:1}]),
            "C" :  MazeRoom([{ROOM_KEY:"A", TIME_NEEDED_KEY:1},
                {ROOM_KEY:"E", TIME_NEEDED_KEY:1}]),
            "D" :  MazeRoom([{ROOM_KEY:"E", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"B", TIME_NEEDED_KEY:1}]),
            "E" :  MazeRoom([{ROOM_KEY:"D", TIME_NEEDED_KEY:1}])
            }
        maze = Maze(map, "A", "E")
        solution = maze.solve_maze()
        self.validate_entry(solution.pop(), "E", 1)
        self.validate_entry(solution.pop(), "C", 1)
        self.validate_entry(solution.pop(), "A", 0)

    def test_adventure_good_path(self):
        map = {
            "A" : MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"C", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"M", TIME_NEEDED_KEY:4}]),
            "B" :  MazeRoom([{ROOM_KEY:"E", TIME_NEEDED_KEY:3},
                {ROOM_KEY:"D", TIME_NEEDED_KEY:1}]),
            "C" :  MazeRoom([{ROOM_KEY:"F", TIME_NEEDED_KEY:1}]),
            "D" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"H", TIME_NEEDED_KEY:2}]),
            "E" :  MazeRoom([{ROOM_KEY:"D", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"H", TIME_NEEDED_KEY:1}]),
            "F" :  MazeRoom([{ROOM_KEY:"I", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"G", TIME_NEEDED_KEY:1}]),
            "G" :  MazeRoom([{ROOM_KEY:"M", TIME_NEEDED_KEY:1}]),
            "H" :  MazeRoom([{ROOM_KEY:"K", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"I", TIME_NEEDED_KEY:1}]),
            "I" :  MazeRoom([{ROOM_KEY:"C", TIME_NEEDED_KEY:1}]),
            "J" :  MazeRoom([]),
            "K" :  MazeRoom([{ROOM_KEY:"N", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"L", TIME_NEEDED_KEY:1}]),
            "L" :  MazeRoom([{ROOM_KEY:"O", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"J", TIME_NEEDED_KEY:1}]),
            "M" :  MazeRoom([{ROOM_KEY:"G", TIME_NEEDED_KEY:1}]),
            "N" :  MazeRoom([{ROOM_KEY:"O", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"Q", TIME_NEEDED_KEY:1}]),
            "O" :  MazeRoom([{ROOM_KEY:"P", TIME_NEEDED_KEY:1}]),
            "P" :  MazeRoom([{ROOM_KEY:"Q", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"R", TIME_NEEDED_KEY:1}]),
            "Q" :  MazeRoom([{ROOM_KEY:"T", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"R", TIME_NEEDED_KEY:1}]),
            "R" :  MazeRoom([{ROOM_KEY:"T", TIME_NEEDED_KEY:1}]),
            "T" :  MazeRoom([]),
            }

        maze = Maze(map, "A", "T")
        solution = maze.solve_maze()
        self.validate_entry(solution.pop(), "T", 1)
        self.validate_entry(solution.pop(), "Q", 1)
        self.validate_entry(solution.pop(), "N", 1)
        self.validate_entry(solution.pop(), "K", 1)
        self.validate_entry(solution.pop(), "H", 2)
        self.validate_entry(solution.pop(), "D", 1)
        self.validate_entry(solution.pop(), "B", 1)
        self.validate_entry(solution.pop(), "A", 0)

    def test_adventure_good_path_with_locks(self):
        map = {
            "A" : MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"C", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"M", TIME_NEEDED_KEY:4}]),
            "B" :  MazeRoom([{ROOM_KEY:"E", TIME_NEEDED_KEY:3},
                {ROOM_KEY:"D", TIME_NEEDED_KEY:1},
                {ROOM_KEY:"I", TIME_NEEDED_KEY:3}]),
            "C" :  MazeRoom([{ROOM_KEY:"F", TIME_NEEDED_KEY:1}]),
            "D" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"H", TIME_NEEDED_KEY:2}]),
            "E" :  MazeRoom([{ROOM_KEY:"D", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"H", TIME_NEEDED_KEY:1}]),
            "F" :  MazeRoom([{ROOM_KEY:"G", TIME_NEEDED_KEY:1}]),
            "G" :  MazeRoom([{ROOM_KEY:"M", TIME_NEEDED_KEY:1}]),
            "H" :  MazeRoom([{ROOM_KEY:"K", TIME_NEEDED_KEY:1}]),
            "I" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}], item="KEY"),
            "J" :  MazeRoom([]),
            "K" :  MazeRoom([{ROOM_KEY:"N", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"L", TIME_NEEDED_KEY:1}], requires="KEY"),
            "L" :  MazeRoom([{ROOM_KEY:"O", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"J", TIME_NEEDED_KEY:1}]),
            "M" :  MazeRoom([{ROOM_KEY:"G", TIME_NEEDED_KEY:1}]),
            "N" :  MazeRoom([{ROOM_KEY:"O", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"Q", TIME_NEEDED_KEY:1}]),
            "O" :  MazeRoom([{ROOM_KEY:"P", TIME_NEEDED_KEY:1}]),
            "P" :  MazeRoom([{ROOM_KEY:"Q", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"R", TIME_NEEDED_KEY:1}]),
            "Q" :  MazeRoom([{ROOM_KEY:"T", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"R", TIME_NEEDED_KEY:1}]),
            "R" :  MazeRoom([{ROOM_KEY:"T", TIME_NEEDED_KEY:1}]),
            "T" :  MazeRoom([]),
            }

        maze = Maze(map, "A", "T")
        if maze.implements_locked_room_extension():
            solution = maze.solve_maze()
            self.validate_entry(solution.pop(), "T", 1)
            self.validate_entry(solution.pop(), "Q", 1)
            self.validate_entry(solution.pop(), "N", 1)
            self.validate_entry(solution.pop(), "K", 1)
            self.validate_entry(solution.pop(), "H", 2)
            self.validate_entry(solution.pop(), "D", 1)
            self.validate_entry(solution.pop(), "B", 1)
            self.validate_entry(solution.pop(), "I", 3)
            self.validate_entry(solution.pop(), "B", 1)
            self.validate_entry(solution.pop(), "A", 0)

    def test_adventure_no_path(self):
        map = {
            "A" : MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"C", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"M", TIME_NEEDED_KEY:4}]),
            "B" :  MazeRoom([{ROOM_KEY:"E", TIME_NEEDED_KEY:3},
                {ROOM_KEY:"D", TIME_NEEDED_KEY:1}]),
            "C" :  MazeRoom([{ROOM_KEY:"F", TIME_NEEDED_KEY:1}]),
            "D" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"H", TIME_NEEDED_KEY:2}]),
            "E" :  MazeRoom([{ROOM_KEY:"D", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"H", TIME_NEEDED_KEY:1}]),
            "F" :  MazeRoom([{ROOM_KEY:"I", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"G", TIME_NEEDED_KEY:1}]),
            "G" :  MazeRoom([{ROOM_KEY:"M", TIME_NEEDED_KEY:1}]),
            "H" :  MazeRoom([{ROOM_KEY:"K", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"I", TIME_NEEDED_KEY:1}]),
            "I" :  MazeRoom([{ROOM_KEY:"C", TIME_NEEDED_KEY:1}]),
            "J" :  MazeRoom([]),
            "K" :  MazeRoom([{ROOM_KEY:"N", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"L", TIME_NEEDED_KEY:1}]),
            "L" :  MazeRoom([{ROOM_KEY:"O", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"J", TIME_NEEDED_KEY:1}]),
            "M" :  MazeRoom([{ROOM_KEY:"G", TIME_NEEDED_KEY:1}]),
            "N" :  MazeRoom([{ROOM_KEY:"O", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"Q", TIME_NEEDED_KEY:1}]),
            "O" :  MazeRoom([{ROOM_KEY:"P", TIME_NEEDED_KEY:1}]),
            "P" :  MazeRoom([{ROOM_KEY:"Q", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"R", TIME_NEEDED_KEY:1}]),
            "Q" :  MazeRoom([{ROOM_KEY:"A", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"R", TIME_NEEDED_KEY:1}]),
            "R" :  MazeRoom([{ROOM_KEY:"A", TIME_NEEDED_KEY:1}]),
            "T" :  MazeRoom([]),
            }


        maze = Maze(map, "A", "T")
        solution = maze.solve_maze()
        self.assertIsNone(solution)

    def test_adventure_no_path_with_locks(self):
        map = {
            "A" : MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"C", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"M", TIME_NEEDED_KEY:4}]),
            "B" :  MazeRoom([{ROOM_KEY:"E", TIME_NEEDED_KEY:3},
                {ROOM_KEY:"D", TIME_NEEDED_KEY:1},
                {ROOM_KEY:"I", TIME_NEEDED_KEY:3}]),
            "C" :  MazeRoom([{ROOM_KEY:"F", TIME_NEEDED_KEY:1}]),
            "D" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"H", TIME_NEEDED_KEY:2}]),
            "E" :  MazeRoom([{ROOM_KEY:"D", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"H", TIME_NEEDED_KEY:1}]),
            "F" :  MazeRoom([{ROOM_KEY:"G", TIME_NEEDED_KEY:1}]),
            "G" :  MazeRoom([{ROOM_KEY:"M", TIME_NEEDED_KEY:1}]),
            "H" :  MazeRoom([{ROOM_KEY:"K", TIME_NEEDED_KEY:1}]),
            "I" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:1}], item="KEY"),
            "J" :  MazeRoom([]),
            "K" :  MazeRoom([{ROOM_KEY:"N", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"L", TIME_NEEDED_KEY:1}], requires="KEY"),
            "L" :  MazeRoom([{ROOM_KEY:"O", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"J", TIME_NEEDED_KEY:1}]),
            "M" :  MazeRoom([{ROOM_KEY:"G", TIME_NEEDED_KEY:1}]),
            "N" :  MazeRoom([{ROOM_KEY:"O", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"Q", TIME_NEEDED_KEY:1}]),
            "O" :  MazeRoom([{ROOM_KEY:"P", TIME_NEEDED_KEY:1}]),
            "P" :  MazeRoom([{ROOM_KEY:"Q", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"R", TIME_NEEDED_KEY:1}]),
            "Q" :  MazeRoom([{ROOM_KEY:"A", TIME_NEEDED_KEY:1}, 
                {ROOM_KEY:"R", TIME_NEEDED_KEY:1}]),
            "R" :  MazeRoom([{ROOM_KEY:"A", TIME_NEEDED_KEY:1}]),
            "T" :  MazeRoom([]),
            }

        maze = Maze(map, "A", "T")
        if maze.implements_locked_room_extension():
            solution = maze.solve_maze()
            self.assertIsNone(solution)

    def validate_entry(self, stack, room_name, time):
        self.assertEqual(stack[ROOM_KEY], room_name)
        self.assertEqual(stack[TIME_TAKEN_TO_ARRIVE_HERE_KEY], time)


