Pitch Perfect
=============

Project 1 from the Udacity Full-Stack Nanodegree program. Simple single-page 
display of several movies with ability to click for the trailer. This initial 
project is designed to help the learner get comfortable with the basic syntax 
and structure of Python code as well as a gentle introduction to object-
oriented programming.

The project simply displays a single web page with the movie posters for 6 
pre-defined movies (hard-coded into entertainment_center.py). Upon clicking a 
movie "poster", the user is able to watch the Youtube trailer associated with 
that movie.

REQUIREMENTS
============

This program requires Python 2.x as well as any modern web browser. To verify
your version of Python, execute

    python -V
    
from the command line and examine the output for version information.

Note that platform-specific instructions are not provided. Please refer to
www.python.org for detailed instructions on how to install Python and
verify operation as well as how to run scripts from the command line.

INSTALLATION
============

To install the program, simply copy all .py and .html files to a single 
directory on your machine.

RUNNING THE PROGRAM
===================

After installing the program as described above, run your Python interpreter
passing entertainment_center.py as the script to execute. Example:

    python entertainment_center.py

Your web browser should then open and display the page consisting of the
"posters" (thumbnails) for 6 different movies. Simply click on a poster to 
show the Youtube trailer associated with the movie.

MODIFYING THE PROGRAM
=====================

If you would like to show different movies, you can directly edit the
entertainment_center.py file to include the appropriate movie data.
NOTE: changes are at your own risk. Do not attempt any modifications if you
are not very comfortable with object-oriented programming and Python in
particular.

If you choose to add new movies, the format for each movie object is:
    Name of Movie
    Synopsis of Movie
    URL to an image to display as a movie "poster"
    URL to the Youtube trailer to show when the poster is clicked

New movie objects should be inserted at line 41 of entertainment_center.py
and each element (name, synopsis, URL's) must be enclosed in quotes as
the existing entries are in the provided entertainment_center.py file. It is
also critical to define the movie object using the order listed above.

In addition to creating a movie object, the new object needs to be included in 
the array that ison lines 45 & 46 otherwise your new movie object will not be 
displayed.

Further details of the structure of a movie object can be obtained by
examining the media.py file which is the class definition for the Movie
object.

AUTHOR
======
Greg Palen
codingvirtual@gmail.com
