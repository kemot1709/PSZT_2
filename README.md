# Implementation and usage of the ant algorithm
This algorithm has been written during my studies at Warsaw University of Technology for the PSZT (Fundamentals of AI) course.

This repository is an example implementation of ant algorithm. Algorithm has been verified using USA roads network from site http://sndlib.zib.de/home.action.
![image](https://github.com/kemot1709/PSZT_2/blob/master/graphs/myplot.png)

Every edge is defined by:
- source - start point
- target - end point
- capacity - how many cars (ants) can be on edge
- cost - length of edge

# Usage
Run with Python 3 (tested with Python 3.7)

```
python ./main.py [options]
```

Example usage:
```
python ./main.py -e1 -d=452 -generations=2000
```

## Options
```
-i, --generations   Number of generations that ants are trained. Value between 100 and 10000 (default 1000)
-m, --ph_min        Minimal value of pheromone that have to be on edge. Value between 0 and 2.0 (default 0.1)
-r, --ph_res        Part of pheromone that stays on edge between iterations. Value between 0.1 and 0.999 (default 0.75)
-d, --demand        Nr of predefined source, target and requirement, described in source file. For usa.xml value is between -1 and 649 (default -1). Value -1 means that source, target and requirement are defined by user, if not then they are random.
-s, --source        Start of optimized path. Value is one of available points from graph.
-t, --target        Finish of optimized path. Value is one of available points from graph.
-c, --requirement   Required traffic between source and target. Value between 1 and 200 (default 64)
-e, --elimination   Test option to eliminate after some time the most used edge. This option allow to observe how ant algorithm dynamically adapt to changing environment. Value is 0 or 1 (default 0)
```
