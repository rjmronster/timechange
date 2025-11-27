#!/usr/bin/env python3
"""
Usage: This function will return UTC time given GPS time.
       Input is GPS. Output is UTC.
"""
usage = __doc__

import sys
import argparse
from taiutc import taiutc
from gpslpsec import gpslpsec

def gps2utc(gps, verbose=False):
   lpsec, b4lp =  gpslpsec(gps)
   utc_t1 = gps - lpsec
   if ( utc_t1 == b4lp ):
      return( gps - lpsec)
   lpsec, b4lp =  gpslpsec(utc_t1)
   return( gps - lpsec )

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute utc time from gps time")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gps", type=float, help="gps input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("gps", nargs="*", type=float, help="gps input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "gps2utc.py 815302800")
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      gpsstring = input_data.split()
      gpstime = float( gpsstring[0] )
   else:
      if ( len(args.gps) < 1 ):
         print(usage)
         quit()
      gpstime = float( args.gps[0] )
   if ( args.verbose ):
      print(usage)
      print("input time was:", gpstime )
      print("output time is:", end=" " )
   utctime = gps2utc(gpstime)
   print(f"{utctime:18.6f}")

if __name__ == "__main__":
   main()
