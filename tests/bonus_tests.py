from unittest import TestCase
from maze_adventure import MazeRoom, ROOM_KEY, TIME_NEEDED_KEY, Maze, TIME_TAKEN_TO_ARRIVE_HERE_KEY

class maze_adventure_bonus_tests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_bonus_case(self):
        

        # testing for infinite loops where pretty much all rooms can go back to all attached rooms

        map = {
            "A" : MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:5}]),

            "B" :  MazeRoom([{ROOM_KEY:"A", TIME_NEEDED_KEY:5}, {ROOM_KEY:"D", TIME_NEEDED_KEY:1}, {ROOM_KEY:"C", TIME_NEEDED_KEY:3}]),

            "C" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:3}, {ROOM_KEY:"E", TIME_NEEDED_KEY:3}]),

            "D" :  MazeRoom([{ROOM_KEY:"B", TIME_NEEDED_KEY:2}, {ROOM_KEY:"E", TIME_NEEDED_KEY:2}]),

            "E" :  MazeRoom([{ROOM_KEY:"D", TIME_NEEDED_KEY:1}, {ROOM_KEY:"F", TIME_NEEDED_KEY:2}]),

            "F" :  MazeRoom([{ROOM_KEY:"E", TIME_NEEDED_KEY:1}]),

            "G" :  MazeRoom({ROOM_KEY:"F", TIME_NEEDED_KEY:10})
            }

        maze = Maze(map, "A", "T")
        solution = maze.solve_maze()
        self.assertIsNone(solution)