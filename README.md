# PyStrange
PyStrange is a strange attractor generator. The user can search for random attractors and plot them with matplotlib. PyStrange can be used in **Random Search Mode** or **Single Search Mode**
## Random Search Mode
Use PyStrange to plot random strange attractors. It is recommended to use large values for **-num** because most attractors are not visually appealing. The default value for -num is 10. The parameter **-num_points** defines the number of points to becalculated (default: 100 000). **-subtitle** defines a user specific subtitle for the matplotlib plot.
## Single Search Mode
Use PyStrange to find an strange attractor using a specific parameter set. The parameters for the quadratic functions are encoded as a string of 12 capital letters (**-co_str**). PyStrange uses the notation introduced by Julien Clinton Sprott ([link to website](http://sprott.physics.wisc.edu/sprott.htm)). The parameter set ranges from -1.2 (letter A) to + 1.3 (letter Z). If -co_str is passed, -num will be ignored.
## Help
```
python3 pystrange.py -h
```
