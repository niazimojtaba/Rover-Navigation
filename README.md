# Rover Navigation

I hame some assumtions to solve this problem as:
* I used the x and y boundary to raise exception not more, but update the next position too.
* For other stream input and output it was easy to consider eof or etc, but for stdin there is no way to detect ending input, So it was handled by try and catch.

I consider two implementation for solving this, the first one is same challenge code, just writing the solution as fast I can, and another one has written with more structure. The structured have some advance features like reuseable, encapsulated, testbale and optional with type of streaming input.

For runngin test you should execute just this command in root folder:

`python3.8 -m unittest`

To run easy code like challenge code:

`python3.8 challenge_code.py`

To run structured code which in default work with stdin adn stdout, you can run by this command:

`python3.8 rover.py`
