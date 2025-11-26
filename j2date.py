#!/usr/bin/env python3
"""
Usage: Convert integer Julian day number to (year, month, day)
       Input is integer Julian date. Output is year, month, day.
"""
usage = __doc__

import sys
import argparse

def j2date(jd,verbose=False):
    """
    Convert Julian day number to (year, month, day)
    
    Parameters:
        jd (int): Julian day number
    
    Returns:
        year (int), month (int), day (int)
    """
    j = jd - 1721119
    y = (4 * j - 1) // 146097
    j = 4 * j - 1 - 146097 * y
    d = j // 4
    j = (4 * d + 3) // 1461
    d = 4 * d + 3 - 1461 * j
    d = (d + 4) // 4
    m = (5 * d - 3) // 153
    d = 5 * d - 3 - 153 * m
    d = (d + 5) // 5
    y = 100 * y + j
    if m < 10:
        m = m + 3
    else:
        m = m - 9
        y = y + 1
    return y, m, d

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gps", type=float, help="jdate input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("jd", nargs="*", type=int, help="integer jdate input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "j2date.py 2460981" )
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      jdstring = input_data.split()
      jdtime = int( jdstring[0] )
   else:
      if ( len(args.jd) < 1 ):
         print(usage)
         quit()
      jdtime = int( args.jd[0] )
   if ( args.verbose ):
      print(usage)
      print("input time was:", jdtime )
      print("output:")
   year, month, day = j2date(jdtime)
   print( f"{year:4d}", f"{month:02d}", f"{day:02d}")

if __name__ == "__main__":
   main()
