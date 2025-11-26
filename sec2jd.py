#!/usr/bin/env python3
"""
Usage: Convert seconds past J2000 to Julian Date
       Input is J2000. Output is Julian Date
"""
usage = __doc__

import sys
import argparse

def sec2jd(sec,verbose=False):
    """
    Convert  seconds past J2000 to Julian Date
    """
    sec_per_day = 86400.0
    jdref = 2451545.0    # J2000.0 (January 1, 2000, 12 hours)
    jd = sec/sec_per_day + jdref
    return jd

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("sec", type=float, help="sec input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("sec", nargs="*", type=int, help="sec input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "sec2jd.py 815302800" )
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      secstring = input_data.split()
      sectime = float( secstring[0] )
   else:
      if ( len(args.sec) < 1 ):
         print(usage)
         quit()
      sectime = float ( args.sec[0] )
   if ( args.verbose ):
      print(usage)
      print("input time was:", sectime )
      print("output time is:", end=" " )
   jdtime = sec2jd(sectime)
   print( f"{jdtime}" )

if __name__ == "__main__":
   main()
