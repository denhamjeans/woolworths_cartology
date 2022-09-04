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
- Time is irrelevant, the number of steps is irrelevant as we just need the final location here
- key attributes we need to store for movement are:
    - current x position
    - current y position
    - current direction the rover is facing options are (N, S, E, W). Only 90 degree movements are relevant here.
    - 


Program steps:
- Set plateau size. Top right corner will be the first input. in x * y matrix.
- Set 

"""








from dataclasses import dataclass

@dataclass
class Rover:
    """Basic representation of a Rover and it's attributes."""
    x: int
    y: int
    direction: str

@dataclass
class Plateau:
    """A plateau on Mars within within which several rovers perform operations to return information"""




def main()


if __name__ == '__main__':
    main()