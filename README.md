# PyStrange
PyStrange is a strange attractor generator. The user can search for random attractors and plot them with Matplotlib. A detailed German description of this project can be found on my [website](http://jupiter-online.net/projekt-pystrange/). PyStrange can be used in **Random Search Mode** or **Single Search Mode**.
## Rquirements
PyStrange is based on Python 3. It requires the Python libraries **Numpy** and **Matplotlib**.
## Random Search Mode
Use PyStrange to plot random strange attractors. It is recommended to use large values for **-num** because most attractors are not visually appealing. The default value for -num is 10. The parameter **-num_points** defines the number of points to becalculated (default: 100 000). **-subtitle** defines a user specific subtitle for the Matplotlib plot. The default subtitle is "created with PyStrange".
## Single Search Mode
Use PyStrange to find an strange attractor using a specific parameter set. The parameters for the quadratic functions are encoded as a string of 12 capital letters (**-co_str**). PyStrange uses the notation introduced by Julien Clinton Sprott ([link to website](http://sprott.physics.wisc.edu/sprott.htm)). The parameter set ranges from -1.2 (letter A) to + 1.3 (letter Z). If -co_str is passed, -num will be ignored.
## Help
Use **-h** or **--help** to show the help text.
```
python3 pystrange.py -h
```
## Usage
All arguments are optional. If the program is executed without any arguments, it will search for 10 random attractors. If any are found, they will be plotted with Matplotlib and saved to PNG image files. 100 000 points will be calculated to render a scatter plot. 
```
python3 pystrange.py [-h] [-num NUM] [-num_points NUM_POINTS] [-subtitle SUBTITLE] [-co_str CO_STR]
```
## Examples
Try to find 10 random strange attractors:
```
python3 pystrange.py
```
Try to find 20 random strange attractors. Calculate 200000 points for each plot:
```
python3 pystrange.py -num 20 -num_points 200000
```
Try to find one attractor using the parameter set "ABCDEFGHIJKL". Calculate 50000 points.
```
python3 pystrange.py -num_points 50000 -co_str 'ABCDEFGHIJKL'
```
## Output
There are two possible outputs of the program. Many parameter sets will not create an attractor. In this case the output will look something like this:
```
Random attractor 1 of 20: attractor TLWENEDBKPXJ out of bounds at itertation 2 - 0.8719432 -3.1838048
```
In this case the program will continue with the next (random) parameter set. 
If on the other hand an attractor has been found, you will see a success message:
```
Random attractor 2 of 20: printing attractor LRFZJHFWCXRO
```
## Motto
The official motto of PyStrange:
>I am strangely attracted to strangely attractive strange attractors.
## Images
These images were created with PyStrange.
![alt text](https://github.com/jupiter-online/PyStrange/blob/master/images/Quadratic%20Map%20Attractor%20FXYBMTPHKDBA.png "Quadratic Map Attractor FXYBMTPHKDBA")

![alt text](https://github.com/jupiter-online/PyStrange/blob/master/images/Quadratic%20Map%20Attractor%20EWUFTYHDGDOQ.png "Quadratic Map Attractor EWUFTYHDGDOQ")

![alt text](https://github.com/jupiter-online/PyStrange/blob/master/images/Quadratic%20Map%20Attractor%20SJDRDCTQGMSE.png "Quadratic Map Attractor SJDRDCTQGMSE")

