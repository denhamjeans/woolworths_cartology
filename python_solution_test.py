"""Unit testing code for the MARS ROVERS portion of the Woolworths Cartology technical test.

The MARS ROVERS program is detailed in 'python_solutions.py' 
"""

import pytest
from python_solution import main, parse_input_text, check_rover_collision, check_edge_collision, Rover, area


example_rovers = [
    (Rover(1, 2, 'N', 'LMLMLMLMM'), 'W'),
    (Rover(1, 2, 'E', 'LMLMLMLMM'), 'N'),
    (Rover(1, 2, 'S', 'LMLMLMLMM'), 'E'),
    (Rover(1, 2, 'W', 'LMLMLMLMM'), 'S')
]
@pytest.mark.parametrize("input, expected_output", example_rovers)
def test_rover_left_turn(input, expected_output):
    input.turn("L") 
    output = input.current_direction
    assert output == expected_output

example_rovers = [
    (Rover(1, 2, 'N', 'LMLMLMLMM'), 'E'),
    (Rover(1, 2, 'E', 'LMLMLMLMM'), 'S'),
    (Rover(1, 2, 'S', 'LMLMLMLMM'), 'W'),
    (Rover(1, 2, 'W', 'LMLMLMLMM'), 'N')
]
@pytest.mark.parametrize("input, expected_output", example_rovers)
def test_rover_right_turn(input, expected_output):
    input.turn("R") 
    output = input.current_direction
    assert output == expected_output


test_data = [
("""5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM""",
"""1 3 N
5 1 E""")
]

@pytest.mark.parametrize("input, expected_output", test_data)
def test_success_main(input, expected_output):
    assert main(input) == expected_output


def test_edge_failure_main():
    with pytest.raises(ValueError):
        main(("""5 5
5 5 N
M"""))