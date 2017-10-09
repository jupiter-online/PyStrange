# PyStrange
PyStrange is a (strange) attractor generator. The user can search for random attractors and plot them with Matplotlib, Plotly or export them as wavefront file. A detailed German description of this project can be found on my [website](http://jupiter-online.net/projekt-pystrange/). A Gallery with 90 2D Examples (so far) can be found [here](http://pystrange.jupiter-online.net/). PyStrange can be used in **Random Search Mode** or **Single Search Mode**.
## Rquirements
PyStrange is based on Python 3. It requires the Python libraries **Numpy**, **Matplotlib** and **Plotly**.
## Random Search Mode
Use PyStrange to plot 2D or 3D attractors in Random Search
Mode or Single Search Mode. You can choose between two quadratic
and two cubic maps/flows and one quartic map/flow ("2d_12", "3d_30", "2d_20", "3d_60", "3d_105").
It is recommended to use large values for option "-n", especially
if maps with 30 or 60 coefficients are used.
## Single Search Mode
To use Single Search Mode you can use a specific parameter set (option "-s") in the form
of a character string (12, 20, 30, 60 or 105 capital letters).
Parameters for the coefficients of the quadratic and cubic functions
range from -1.2 (letter A) to + 1.3 (Letter Z).
If option "-s" is passed, option "-n" will be ignored.
## Output
Attractors can be exported in three different formats (option "-o"):
"png" (via matplotlib), "html" (via plotly) or "obj" (wavefront).
3D Plots via plotly will produce interactive Javascript visualizations.
The wavefront format can be used to import points clouds to Blender.
You can specify multiple output formats, for example "-o png html".
Set the number of points to calculated with option "-p".
You can specify to plot only every n'th point with option "-j".
You can start plotting at a certain index with option "-f".
You can define a time interval with option "-t" (only available for 3D output).
Yout can define an interpolation factor.
## Help
Use **-h** or **--help** to show the help text.
```
python3 pystrange.py -h
```
## Usage
All arguments are optional except m. This parameter specifies the type of map/flow ("2d_12", "3d_30", "2d_20", "3d_60", "3d_105").
```
python3 pystrange.py [-h] [-n NUMBER] [-p POINTS] [-t TIME] [-s STRING]
                    [-o [OUTPUT [OUTPUT ...]]] [-j JUMP] [-f FIRST]
                    [-i INTERPOLATE]
                    m
```
## Examples
Try to find 10 random attractors using a 2D quadratic map with 12 coefficients:
```
python3 pystrange.py  2d_12 -n 10
```
Try to find 100 random attractors using a 3D cubic map with 60 coefficients, output to png and html
```
python3 pystrange.py  3d_60 -n 100 -o png html
```
Try to find one attractor using the parameter set "ABCDEFGHIJKL", calculate 50000 points, start plotting at index 15000,
```
python3 pystrange.py 2d_12  -p 50000 -s AGWXDCUKEANF -f 15000
```
Try to find 1000 random attracors with 105 coeffitions in flow mode, time intervall 0.1, output png + html
```
python3 pystrange.py 3d_105 -t 0.1 -n 1000 -o png html
```
## Motto
The official motto of PyStrange:
>I am strangely attracted to strangely attractive strange attractors.
## Images
These images were created with PyStrange (and Blender).

![Attractor](https://github.com/jupiter-online/PyStrange/blob/master/images/Seltsamer%20Attraktor%202.jpg "3D Attractor")

![Attractor](https://github.com/jupiter-online/PyStrange/blob/master/images/3D%20Attractor%20OUNBOAZRBZSWNMSDZTMEHQPRAWHDTG%2050000%20Vertices.png "Quadratic Map Attractor FXYBMTPHKDBA")

![Attractor](https://github.com/jupiter-online/PyStrange/blob/master/images/Quadratic%20Map%20Attractor%20FXYBMTPHKDBA.png "Quadratic Map Attractor FXYBMTPHKDBA")

![Attractor](https://github.com/jupiter-online/PyStrange/blob/master/images/Quadratic%20Map%20Attractor%20EWUFTYHDGDOQ.png "Quadratic Map Attractor EWUFTYHDGDOQ")

![Attractor](https://github.com/jupiter-online/PyStrange/blob/master/images/Quadratic%20Map%20Attractor%20SJDRDCTQGMSE.png "Quadratic Map Attractor SJDRDCTQGMSE")

