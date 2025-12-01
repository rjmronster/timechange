#!/usr/bin/env python3
"""
Usage: Convert sec from reference epoch to DD-MMM-YYYY HH:MM:SS.FFFF
"""
usage = __doc__

import sys
import argparse
from sec2cal import sec2cal

    month_name = [
        "***", "jan", "feb", "mar", "apr", "may", "jun",
        "jul", "aug", "sep", "oct", "nov", "dec"
    ]


def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute DD-MMM-YYYY HH:MM:SS.FFFF from seconds")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gps", type=float, help="jdate input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("sec", nargs="*", type=float, help="seconds input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "sec2chr.py  815266870.123000" )
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
    
   year, month, day, hour, minute, secondfrac = sec2chr(sec)
   print(f"{day:02d}-{month}-{year:04d} {hour:02d}:{minute:02d}:{secondfrac:06.3f}")

if __name__ == "__main__":
   main()
