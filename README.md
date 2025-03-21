This is a simple bot controller with a graphical user interface. 

#Installation and Setup:
1. Clone the repository
  (i) Create a workspace (say: controller_ws)
  (ii) Inside the src folder clone the repository
  Terminal command:
    cd ~/controller_ws/src
    git clone https://github.com/yourusername/bot_controller_gui.git

2. Build the package
   (i) Inside the workspace, build the package using catkin_make command:
       cd ~/controller_ws
       catkin_make

3. Source the workspace and run:
   Source the workspace in the terminal. Command:
     source ~/controller_ws/devel/setup.bash
   And now the two python file:
     rosrun bot_controller_gui data_publisher.py
     rosrun bot_controller_gui gui_controller.py

4. Dependencies:
    ROS
    Tkinter
    TurtleBot3 (if running with Gazebo)
    roslaunch and rosrun utilities
