#!/usr/bin/env python3
"""
Usage: This function will return the difference
       TAI-UTC in seconds for the specified utc time.
       Input is UTC
"""
usage = __doc__

from loadleap import loadleap
import sys
import argparse
from taiutc import taiutc

def gpslpsec(utc, verbose=False):
   leap = loadleap(verbose)
   xs = leap["x"]

   # Initialize outputs
   lpsec = 0
   before = -1577880000.0  # default time before first leap

    # Find the last leap second before utc_time
   for x in xs:
       if utc >= x:
           before = x

   # Compute lpsec as (tai-utc + gps-tai)
   # gps-tai offset is 19 seconds
   lpsec = int(taiutc(utc)) - 19

   return lpsec, before

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute leapsec" )
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("utc", type=float, help="utc input" )
#  this allows for no input so we can use input from a pipe
   parser.add_argument("utc", nargs="*", type=float, help="utc input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outoup")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "gpslpsec.py 815302800")
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      utcstring = input_data.split()
      utctime = float( utcstring[0] )
   else:
      if ( len(args.utc) < 1 ):
         print(usage)
         quit()
      utctime = float( args.utc[0] )
   if ( args.verbose ):
      print(usage)
      print("input time was:", utctime )
      print("output:")
   lpsec, before = gpslpsec(utctime)
   print("lpsec: ", f"{lpsec}")
   print("before:", f"{before}")

if __name__ == "__main__":
   main()

