#!/usr/bin/env python3
"""
Usage: Takes the components of a calendar date and time to character.
       input year, month, day, hour, minute, second.frac
       and returns 06-jan-2039 20:40:31.000 for example
"""
usage = __doc__

import sys
import argparse
from date2j import date2j

def cal2chr(year, month, day, hour, minute, second, frac, verbose=False):
    """
    Takes the components of a calendar date and time
            Year, Month, Day , Hour , Minute , Second.Frac
    Returns:
      sec past J2000.0 reference date
    """
    month_name = [
        "***", "jan", "feb", "mar", "apr", "may", "jun",
        "jul", "aug", "sep", "oct", "nov", "dec"
    ]

    real_sec = float (second) + frac

    return f"{day:2d}-{month_name[month]}-{year:04d} {hour:02d}:{minute:02d}:{real_sec:09.6f}"

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gps", type=float, help="jdate input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("ymdhrms", nargs="*", type=float, help="cal input yyyy month day hour minute second.frac" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "cal2chr.py 2025 11 1 10 11 01.123")
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      ymdhrms = input_data.split()
      year   = int  ( ymdhrms[0] )
      month  = int  ( ymdhrms[1] if len(ymdhrms) > 1 else   1 )
      day    = int  ( ymdhrms[2] if len(ymdhrms) > 2 else   1 )
      hour   = int  ( ymdhrms[3] if len(ymdhrms) > 3 else   0 )
      minute = int  ( ymdhrms[4] if len(ymdhrms) > 4 else   0 )
      frac   = float( ymdhrms[5] if len(ymdhrms) > 5 else 0.0 )
      second = int( frac )
      frac  -= float( second )
   else:
      if ( len(args.ymdhrms) < 1 ):
         print(usage)
         quit()
      year = int( args.ymdhrms[0] )
      month  = int  ( args.ymdhrms[1] if len(args.ymdhrms) > 1 else   1 )
      day    = int  ( args.ymdhrms[2] if len(args.ymdhrms) > 2 else   1 )
      hour   = int  ( args.ymdhrms[3] if len(args.ymdhrms) > 3 else   0 )
      minute = int  ( args.ymdhrms[4] if len(args.ymdhrms) > 4 else   0 )
      frac   = float( args.ymdhrms[5] if len(args.ymdhrms) > 5 else 0.0 )
      second = int( frac )
      frac  -= float( second )
   if ( args.verbose ):
      print(usage)
      print("input time was", f"{year:4d} {month:02d} {day:02d} {hour:02d} {minute:02d} {second:02d} {frac:10.6f}")
      print("output time is:", end=" " )
   chr = cal2chr( year, month, day, hour, minute, second, frac )
   print(chr)

if __name__ == "__main__":
   main()
