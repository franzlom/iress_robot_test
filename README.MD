### Hi Iress Team

#### Author: Franz Lomibao
#### IDE: PyCharm


Thanks for taking the time to look at my code for the IRESS Robot Code Challenge Done in python

### How does this solution work?
* This is a command Line interface application and currently can only be exited by Ctrl+c
* 3 Class file with 2 test files
* Probably the most complicated part of the code is in the main app for the `PLACE` case, its lengthy
and has a lot of comprehensions to help parse the code - I would like to talk further about this code
* There was also confusion around the initial value
* Since Origin was explicitly described, single `PLACE` is a valid command and will 
 PLACE the robot at 0,0 as well as `PLACE 1,1,NORTH`
* `f` in `PLACE x,y,f` has been replaced with `NORTH, SOUTH, EAST or WEST`
* The robot wont fall off the edge corners

### How to use
* Won't Accept any command until `PALCE`/`PLACE x,y,f`
* after place the robot these commands are available `MOVE LEFT RIGHT REPORT`
* `MOVE` if legal position move forward in the direction the robot is facing
* `LEFT` Change direction 90 Degrees to the left - changes direction
* `RIGHT` Change direction 90 Degrees to the RIGHT - Changes direction
* `REPORT` Robot says orientation and position
* Ctrl+c to exit

### Unit Test
* unit test can be run with `python -m unittest` - will want to further talk about this

### How to Start the program?
1. install python 3.10.0 or greater
2. run `python main.py`


### Version: Python _3.10.0_ or Greater
* This is very important due to the fact that this code is using *switch/case statements* which is only available at python
3.10.0 or greater

### Requirements.txt
* _requirements.txt_ is intentionally empty as there are no third part library used for this solution