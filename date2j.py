#!/usr/bin/env python3
"""
Usage: Convert year, month, day to Julian int day.
       Input is year, month, day and output is int Julian date.
       Defaults for month and day are 1.
"""
usage = __doc__

import sys
import argparse

def date2j(year, month, day, verbose=False):
    """
    Convert (year, month, day) to Julian int day
    
    Returns:
        year (int), month (int), day (int)
    """
    Y = year
    M = month
    D = day

    if M > 2:
        M -= 3
    else:
        M += 9
        Y -= 1
    C = Y // 100
    YA = Y - 100 * C
    jd = (146097 * C) // 4 + (1461 * YA) // 4 + (153 * M + 2) // 5 + D + 1721119

    return jd

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gps", type=float, help="jdate input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("ymd", nargs="*", type=int, help="jdate input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "date2j.py 2025 11 1" )
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      jdstring = input_data.split()
      year  = int ( jdstring[0] )
      month = int ( jdstring[1] if len(jdstring) > 1 else 1 )
      day   = int ( jdstring[2] if len(jdstring) > 2 else 1 )
   else:
      if ( len(args.ymd) < 1 ):
         print(usage)
         quit()
      year  = int ( args.ymd[0] )
      month = int ( args.ymd[1] if len(args.ymd) > 1 else 1 )
      day   = int ( args.ymd[2] if len(args.ymd) > 2 else 1 )
   if ( args.verbose ):
      print(usage)
      print("input time was:", year, month, day )
      print("output time is:", end=" " )
   jdtime = date2j(year, month, day)
   print(f"{jdtime:18.6f}")

if __name__ == "__main__":
   main()
