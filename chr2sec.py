#!/usr/bin/env python3
"""
Usage: Takes DD-MMM-YYYY HH:MM:SS.FFFF as input and computes secconds past refernce.
"""
usage = __doc__

import sys
import argparse
from date2j import date2j
from cal2sec import cal2sec

def chr2sec(ddmonyyyy, hhmmsecff, verbose=False):
    """
    Takes DD-MMM-YYYY HH:MM:SS.FFFF 
    Returns:
      sec past J2000.0 reference date
    """
    month_name = [
        "***", "jan", "feb", "mar", "apr", "may", "jun",
        "jul", "aug", "sep", "oct", "nov", "dec"
    ]
    tmp = ddmonyyyy.split("-")
    day = int( tmp[0] )
    month = int( month_name.index(tmp[1]) )
    year = int( tmp[2] )
    tmp = hhmmsecff.split(":")
    hour = int( tmp[0] )
    minute = int( tmp[1] )
    secondfrac = float( tmp[2] )
    sec = cal2sec( year, month, day, hour, minute, secondfrac )
    return sec


def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute year month day from Julian day number")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gps", type=float, help="jdate input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("dmyhmsf", nargs="*", type=str, help="DD-MMM-YYYY HH:MM:SS.FFFF as input")
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "chr2sec.py 1-NOv-2025 11:01:10.123")
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      dmyhmsf = input_data.split()
      ddmonyyyy = dmyhmsf[0].lower()
      hhmmsecff = dmyhmsf[1] if len(dmyhmsf) > 1 else "00:00:00.000"
   else:
      if ( len(args.dmyhmsf) < 1 ):
         print(usage)
         quit()
      ddmonyyyy = args.dmyhmsf[0].lower()
      hhmmsecff = args.dmyhmsf[1] if len(args.dmyhmsf) > 1 else "00:00:00.000"
   if ( args.verbose ):
      print(usage)
      print("input time was", ddmonyyyy, hhmmsecff )
      print("output time is:", end=" " )
   sec = chr2sec(ddmonyyyy, hhmmsecff )
   print(f"{sec:18.6f}")

if __name__ == "__main__":
   main()
