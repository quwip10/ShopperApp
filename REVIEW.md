# Code Review 2019-09-24 

Coding Style 
===
~~1. Fix Python code style using pycodestyle main.py~~
<pre>
main.py:61:74: E202 whitespace before ')'  
main.py:66:80: E501 line too long (90 > 79 characters)  
main.py:90:1: W293 blank line contains whitespace  
main.py:97:47: W292 no newline at end of file  
</pre>

~~2. Place these comments closer to the if name == main block~~
<pre>
# Main  
# Created 9-24-19  
# Last updated 9-24-19  
# Aheidenreich  
</pre>

~~3. No need for comments that do not add any real information.~~
    * Imports
    * Global Variables
    * Functions

~~4. Avoid global variables at all cost. There probably isn't any
   legitimate reason to use them :)~~

5. Use Python logging versus commenting/uncommenting print statements

6. The print_menu function should be two or 3 separate functions.
    * Menu option function. This would remove the need for global variables  
    * Menu displace function. Sole purpose is to display menu.  
    * Menu input function sole purpose to accept and validate choice  
        * There might be sub-menu function to handle each menu option  
        * Note: sub-menu functions would allow for easy addition of menu
           options.
    * Investigate the possibility of creating your own ShopperMenu class  

~~7. Provide input guidance.~~

    * "Enter customer name (First Last)"  
    * "Enter today's date (YYYYMMDD)"  
    * default to today's date (computers know this kind of thing"  
    * Try and get the prompt and input on the same line.  
