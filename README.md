# Bot Controller GUI

This is a simple bot controller with a graphical user interface.

## Installation and Setup

## 1. Clone the Repository
#### (i) Create a workspace (e.g., `controller_ws`)
#### (ii) Inside the `src` folder, clone the repository  
#### Run the following terminal commands:
```bash
cd ~/controller_ws/src
git clone https://github.com/sksakib01/bot_controller_gui.git
```
## 2. Build the Package
#### (i) Inside the workspace, build the package using catkin_make:
```bash
cd ~/controller_ws
catkin_make
```
## 3. Source the Workspace and Run
#### Source the workspace in the terminal:

```bash
source ~/controller_ws/devel/setup.bash
```
#### Then, run the two Python files:
```bash
rosrun bot_controller_gui data_publisher.py
rosrun bot_controller_gui gui_controller.py
```
## Dependencies
#### ROS
#### Tkinter
#### TurtleBot3 (if running with Gazebo)
#### roslaunch and rosrun utilities
