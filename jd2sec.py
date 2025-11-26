#!/usr/bin/env python3
"""
Usage: Convert Julian Date to seconds past J2000 
       Input is Julian Date. Output is seconds past refernce epoch.
"""
usage = __doc__

import sys
import argparse
from jd2cal import jd2cal
from cal2sec import cal2sec

def jd2sec(jd,verbose=False):
    """
    Convert Julian Date to seconds past J2000
    """

    year, month, day, hour, minute, second, frac = jd2cal(jd)
    sec = cal2sec(year, month, day, hour, minute, second, frac)
    return sec

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("jd", type=float, help="sec input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("jd", nargs="*", type=float, help="sec input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "jd2sec.py 2460981.375")
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      jdstring = input_data.split()
      jdtime = float( jdstring[0] )
   else:
      if ( len(args.jd) < 1 ):
         print(usage)
         quit()
      jdtime = float( args.jd[0] )
   if ( args.verbose ):
      print(usage)
      print("input time was:", jdtime )
      print("output time is:", end=" " )
   sec = jd2sec(jdtime)
   print( f"{sec}" )

if __name__ == "__main__":
   main()
