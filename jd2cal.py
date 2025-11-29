#!/usr/bin/env python3
"""
Usage: Convert Julian date to calendar components.
       Input is Julian date. Output is year, month, day, hour, minute, second.frac.
"""
usage = __doc__

import sys
import argparse
from j2date import j2date

def jd2cal(jd,verbose=False):
    """
    Convert Julian date to calendar components.
    Returns:
      year, month, day, hour, minute, second.frac
    """
    sec_per_day = 86400.0
    jdplus = jd + 0.5
    jdint = int(jdplus)
    dsec = sec_per_day * (jdplus - jdint)
    if dsec > sec_per_day:
        jdint += 1
        dsec -= sec_per_day
    isec = int(dsec)
    # --- date ---
    year, month, day = j2date(jdint)
    # --- time ---
    hour = isec // 3600
    isec = int(isec - 3600 * hour)
    minute = isec // 60
    isec = int(isec - 60 * minute)
    second = isec
    # fractional seconds
    frac = dsec - int(dsec)
    # return second.frac
    secondfrac = float( second ) + float ( frac )

    return year, month, day, hour, minute, secondfrac

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gps", type=float, help="jdate input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("jd", nargs="*", type=float, help="jdate input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "jd2cal.py 2460981.0" )
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
      print("output:")
   year, month, day, hour, minute, secondfrac = jd2cal(jdtime)
   print(f"{year:4d} {month:02d} {day:02d} {hour:02d} {minute:02d} {secondfrac:10.6f}")

if __name__ == "__main__":
   main()
