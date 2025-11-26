#!/usr/bin/env python3
"""
Usage: Convert sec from reference epoch calendar components.
       Input is seconds. Output is year, month, day, hour, minute, second, frac.
"""
usage = __doc__

import sys
import argparse
from sec2jd import sec2jd
from jd2cal import jd2cal

def sec2cal(sec,verbose=False):
    """
    Convert Julian date to calendar components.
    Returns:
      year, month, day, hour, minute, second, frac
    """
    frac = float (sec) - int (sec)
    if ( frac < 0.0 ):
       frac += 1

    jd = sec2jd( sec - frac + 0.5);
    year, month, day, hour, minute, second, temp = jd2cal(jd)
    secondfrac = float( second ) + frac

    return year, month, day, hour, minute, secondfrac

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gps", type=float, help="jdate input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("sec", nargs="*", type=float, help="jdate input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "sec2cal.py 815263861.123000" )
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      secstring = input_data.split()
      sec = float( secstring[0] )
   else:
      if ( len(args.sec) < 1 ):
         print(usage)
         quit()
      sec = float( args.sec[0] )
   if ( args.verbose ):
      print(usage)
      print("input time was:", sec )
      print("output:")
   year, month, day, hour, minute, secondfrac = sec2cal(sec)
   print(f"{year:4d} {month:02d} {day:02d} {hour:02d} {minute:02d} {secondfrac:10.6f}")

if __name__ == "__main__":
   main()
