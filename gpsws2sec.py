#!/usr/bin/env python3
"""
Usage: Convert seconds past J2000 to gps week and seconds of week
       Input is J2000. Output is gps week and seconds of week
"""
usage = __doc__

import sys
import argparse

def gpsws2sec(week, tow, verbose=False):
    """
    Convert  seconds past J2000 to Julian Date
    """
    gps0 = -630763200.0
    early_week = ( (96-80) * 365.25 ) / 7 
    if ( week < early_week ):
        week += 1024
    sec = tow + week*604800.0 + gps0
    return sec

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gpsws", type=float, help="sec input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("gpsws", nargs="*", type=float, help="sec input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "gpsws2sec.py 2390 594000.000" )
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      gpswsstring = input_data.split()
      week = int( gpswsstring[0] )
      tow  = float ( gpswsstring[1] if len(gpswsstring) > 1 else 0 )
   else:
      if ( len(args.gpsws) < 1 ):
         print(usage)
         quit()
      week = int( args.gpsws[0] )
      tow  = float ( args.gpsws[1] if len(args.gpsws) > 1 else 0 )
   if ( args.verbose ):
      print(usage)
      print("input time was:", sectime )
      print("output time is:", end=" " )
   sec = gpsws2sec(week, tow)
   print(f"{sec:18.6f}")

if __name__ == "__main__":
   main()
