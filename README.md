# DV-bongole
The folder "exercise1" contains only the ROS src files and the folder "exercise2" contains the visualization program

How I run the ros program:

1) Create 4 terminals or use terminator and navigate into catkin workspace which contains src folder contents as given.

2) In the all terminals run command: ```source ./devel/setup.bash```

3) In first terminal, run roscore with command: ```roscore```

4) Run publisher in next terminal with command: ```rosrun publisher talker.py```

5) Run subscriber in next terminal with command: ```rosrun subscriber listener.py```

6) To plot data using PlotJuggler, run in the last terminal this command: ```rosrun plotjuggler PlotJuggler ```

7) Choose streaming and then choose start topic subscriber and choose topic ```/kthfs/result``` and drag ```kthfs/result/data``` to white screen to plot graph.

How to run the Visualization program and its features:

1) Run using command: ```python Visualization.py```

2) The graph pops up which can be paused using mouse click, can be zoomed and moved around as well.

3) Can choose to speed up plotting speed using parameters for the initializing the Visualization object (in the python code).
