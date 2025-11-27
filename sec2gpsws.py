#!/usr/bin/env python3
"""
Usage: Convert seconds past J2000 to gps week and seconds of week
       Input is J2000. Output is gps week and seconds of week
"""
usage = __doc__

import sys
import argparse

def sec2gpsws(sec,verbose=False):
    """
    Convert  seconds past J2000 to Julian Date
    """
    gps0 = -630763200.0
    sec -= gps0
    week = int ( sec/604800.0 )
    tow  = sec - 604800.0 * week
    return week, tow

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("sec", type=float, help="sec input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("sec", nargs="*", type=float, help="sec input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "sec2gpsws.py 815302800" )
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
      print("output:", )
   week, tow = sec2gpsws(sectime)
   print( f"{week:04d}", f"{tow:08.3f}" )

if __name__ == "__main__":
   main()
