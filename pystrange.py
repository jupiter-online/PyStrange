"""
Program:     PyStrange
Description: search for random strange attractors
             and plot them with matplotlib
Author:      Anton Neururer - jupiter-online.net
External libraries:
             numpy, matplotlib
License:

PyStrange is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as published by
the Free Software Foundation.

PyStrange is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

# import modules
import numpy as np
import matplotlib.pyplot as plt
import random
import sys
import argparse
import re

# use syle seaborn
plt.style.use('seaborn')

# map letters to coefficients
coeff = {'A': -1.2, 'B': -1.1, 'C': -1.0,
         'D': -0.9, 'E': -0.8, 'F': -0.7,
         'G': -0.6, 'H': -0.5, 'I': -0.4,
         'J': -0.3, 'K': -0.2, 'L': -0.1,
         'M':  0.0, 'N':  0.1, 'O':  0.2,
         'P':  0.3, 'Q':  0.4, 'R':  0.5,
         'S':  0.6, 'T':  0.7, 'U':  0.8,
         'V':  0.9, 'W':  1.0, 'X':  1.1,
         'Y':  1.2, 'Z':  1.3}


# get all (12) coefficients for coeff_string
def get_coefficient(coeff_string, coefficients):
    return [coefficients[value] for value in coeff_string]


# calculate coordinates of the Quadratic Map
def qardratic_map(x, y, c):
    x_next = c[0] + c[1] * x + c[2] * x * x + c[3] * x * y + c[4] * y + c[5] * y * y
    y_next = c[6] + c[7] * x + c[8] * x * x + c[9] * x * y + c[10] * y + c[11] * y * y
    return x_next, y_next


# create a random string (12 capital letters)
def get_random_string(coefficients):
    return ''.join(random.choice(list(coefficients.keys())) for i in range(12))


# try to find an attractor for a specific parameter string
# in case an attractor has been found, it will be plotted
# with matplotlib and saved to a PNG image file
def get_attractor(co_str, num_points, subtitle):
    x = np.empty(num_points)
    y = np.empty(num_points)

    c = get_coefficient(co_str, coeff)

    # initialize start values
    x[0], y[0] = (0.1, 0.1)

    # calculate all x and y coordinates
    for i in range(num_points-1):
        dx, dy = qardratic_map(x[i], y[i], c)
        x[i + 1] = dx
        y[i + 1] = dy

        # values out of bounds -> abort
        if abs(x[i]) > 2 or abs(y[i]) > 2:
            print('attractor', co_str, 'out of bounds at itertation', i, '-', x[i], y[i])
            return False

    # draw scatter plot
    plt.scatter(x, y, c='b', marker='.', s=0.1)

    # label diagram
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Quadratic Map Attractor " + co_str + '\n' + subtitle)

    # status report
    print('printing attractor {} '.format(co_str))

    # save image
    plt.savefig('Quadratic Map Attractor ' + co_str + '.png')

    # delete current plot
    plt.cla()

    # return success
    return True


# check user input for errors
def check_user_input_random_mode(num, num_points):
    if num < 1:
        sys.exit('Error: num must be at least 1')

    if num_points < 1:
        sys.exit('Error: num_points must be at least 1')


# check user input for errors
def check_user_input_single_mode(num_points, co_str):
    if num_points < 1:
        sys.exit('Error: num_points must be at least 1')

    if len(co_str) != 12:
        sys.exit('Error: co_str must be of length 12')

    if re.match(r'([A-Z]{12})', co_str) is None:
        sys.exit('Error: Only capital letters are allowed for co_str')


# create random attractors
def get_random_attractors(num=10, num_points=100000, subtitle='created with PyStrange'):
    found = 0

    # search for random attractors
    for i in range(num):
        print('Random attractor {} of {}:'.format(i + 1, num), end=' ')
        if get_attractor(get_random_string(coeff), num_points, subtitle):
            found += 1

    # print number of found attractors
    if found == 0:
        print('No attractor has been found')
    elif found == 1:
        print('One attrator has been found')
    elif found > 1:
        print(found, 'attrators have been found')


# main function
def main():
    # create argument parser
    parser = argparse.ArgumentParser(
        description='''Random search mode: Use PyStrange to plot random strange attractors.
                       It is recommended to use large values for -num because
                       most attractors are not visually appealing. The
                       default value for -num is 10. The parameter -num_points defines the 
                       number of points to becalculated. -subtitle defines a user
                       specific subtitle for the matplotlib plot.
                       Singel search mode: you can use a specific parameter set (-co_str) in the form
                       of a 12 character string (all capital letters). 
                       Parameters for the coefficients of the two quadratic functions
                       range from -1.2 (letter A) to + 1.3 (Letter Z).
                       If -co_str is passed, -num will be ignored.
                    ''',
        epilog='''I am strangely attracted to strangely attractive strange attractors.''')
    parser.add_argument('-num', type=int, default=10, help='number of test subjects (int)')
    parser.add_argument('-num_points', type=int, default=100000, help='number of points for plot (int)')
    parser.add_argument('-subtitle', type=str, default='created with PyStrange', help='subtitle for plot (str)')
    parser.add_argument('-co_str', type=str, default='', help='coefficient string (str with 12 capital letters)')

    # parse arguments
    args = parser.parse_args()

    # switch search mode (single or random)
    if args.co_str != '':
        check_user_input_single_mode(args.num_points, args.co_str)
        get_attractor(args.co_str, args.num_points, args.subtitle)
    else:
        check_user_input_random_mode(args.num, args.num_points)
        get_random_attractors(args.num, args.num_points, args.subtitle)


# execute only if run as a script
if __name__ == "__main__":
    main()
