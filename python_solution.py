"""Mars Rover technical Challenge

Preamble
--------
The problem below requires some kind of input. You are free to implement any
mechanism for feeding input into your solution (for example, using hard coded data
within a unit test). 

You should provide sufficient evidence that your solution is complete by, 
as a minimum, indicating that it works correctly against the supplied test data.
We highly recommend using a unit testing framework such as JUnit or NUnit. 

Even if you have not used it before, it is simple to learn and incredibly useful.
The code you write should be of production quality, and most importantly, it should be
code you are proud of.


Problem
-------
A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the rovers so that their
on board cameras can get a complete view of the surrounding terrain to send back to
Earth.

A rover's position is represented by a combination of an x and y co-ordinates and a letter
representing one of the four cardinal compass points. The plateau is divided up into a
grid to simplify navigation. 

An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.
In order to control a rover, NASA sends a simple string of letters. 

The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively,
without moving from its current spot.

'M' means move forward one grid point, and maintain the same heading. 
Assume that the square directly North from (x, y) is (x, y+1).


Input
-----
The first line of input is the upper-right coordinates of the plateau, the lower-left
coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed.
Each rover has two lines of input. 

The first line gives the rover's position, and the second
line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding
to the x and y co-ordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to
move until the first one has finished moving.


Notes
-----
- There are multiple rovers
- Time is irrelevant, the number of steps is irrelevant as we just need the final coordinates here
- key attributes we need to store for movement are:
    - current x position
    - current y position
    - current direction the rover is facing options are (N, S, E, W). Only 90 degree movements are relevant here.


Program steps:
- Set plateau size. Top right corner will be the first input. in x * y matrix.
- program should error when a rover moves off the edge of the plateau
- program should error when one rover move into another.
"""

from dataclasses import Field, dataclass
from collections import namedtuple
from typing import ClassVar, Tuple, List

area = namedtuple('area', ['x', 'y'])
PLATEAU_SIZE = None
ROVER_LIST = []

def convert_to_cardinal(degree: int) -> str:
    degree_conversions = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    return degree_conversions[degree]

def convert_to_degree(cardinal: str) -> int:
    cardinal_conversions = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
    return cardinal_conversions[cardinal]
    

def check_edge_collision(coordinates: tuple) -> bool:
    if coordinates[0] < 0 or coordinates[0] > PLATEAU_SIZE.x:
        return True
    if coordinates[1] < 0 or coordinates[1] > PLATEAU_SIZE.y:
        return True

def check_rover_collision(coordinates: tuple) -> bool:
    for rover in ROVER_LIST:
        if rover.x_coordinate == coordinates[0] and rover.y_coordinate == coordinates[1]:
            return True


@dataclass
class Rover:
    """Basic representation of a Rover and it's attributes.
    """
    x_coordinate: int
    y_coordinate: int
    current_direction: str
    commands: List[str]

    def turn(self, turn: str) -> None:
        """90 degree turn method for the rover based on the rover's current_direction.
        
        NOTE: Inputs can only be 'L' (left) or 'R' (right).
        """
        if turn == 'L':
            degree = -90
        elif turn == 'R':
            degree = 90
        else:
            raise ValueError("Invalid Turn Commmand: {turn}")

        # convert cardinal direction to decimal for rotation changes
        self.current_direction = convert_to_cardinal((convert_to_degree(self.current_direction) + degree) % 360)

    def move(self):
        """Increment the Rover's coordinates based on it's current facing direction."""

        if self.current_direction == 'N':
            new_coordinates = (self.x_coordinate, self.y_coordinate + 1)

        elif self.current_direction == 'E':
            new_coordinates = (self.x_coordinate + 1, self.y_coordinate)

        elif self.current_direction == 'S':
            new_coordinates = (self.x_coordinate, self.y_coordinate - 1)

        elif self.current_direction == 'W':
            new_coordinates = (self.x_coordinate - 1, self.y_coordinate)

        if check_edge_collision(new_coordinates):
            raise ValueError("Rover cannot move at plateau edge.")

        if check_rover_collision(new_coordinates):
            raise ValueError("Rover cannot move into another rover.")

        self.x_coordinate = new_coordinates[0]
        self.y_coordinate = new_coordinates[1]

    def execute_commands(self):
        """Execute the saved 'commands' list attribute for this rover."""

        for command in self.commands:
            if command == 'M':
                self.move()
            elif command in ['L', 'R']:
                self.turn(command)
            else: 
                raise ValueError("Invalid Command: {command}")

    @property
    def current_orientation(self):
        return f'{self.x_coordinate} {self.y_coordinate} {self.current_direction}'


def parse_input_text(input_text: str) -> Tuple:
    """Converts the MARS ROVERS program input text to a useable format.""" 

    global PLATEAU_SIZE
    global ROVER_LIST

    input_list = input_text.split("\n")

    #get the plateau x and y Plateau from the first line of the input text.
    PLATEAU_SIZE = area(int(input_list[0].split(" ")[0]), int(input_list[0].split(" ")[1]))
    initial_orientations = input_list[1::2]
    commands_list = input_list[2::2]

    for orientation, commands in zip(initial_orientations, commands_list):
        orientation = orientation.split(" ")
        new_rover = Rover(int(orientation[0]), 
                          int(orientation[1]), 
                          orientation[2],
                          commands)
        ROVER_LIST.append(new_rover)


def main(input_text: str) -> str:

    parse_input_text(input_text)
    for id, rover in enumerate(ROVER_LIST):
        rover.execute_commands()
        print(rover)
    output = '\n'.join([rover.current_orientation for rover in ROVER_LIST])

    return output


if __name__ == '__main__':
    print(main("""5 5
1 2 N
MM
3 3 E
MM"""))