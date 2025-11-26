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

def taiutc(utc, verbose=False):
   leap = loadleap(verbose)
   xs = leap["x"]
   ys = leap["y"]
   # Find first leap.x[i] > utc by iterating like in C
   i = 0
   size = len(xs)
   while i < size and xs[i] <= utc:
      i += 1
   return ys[i - 1]  # same l

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute tai - utc" )
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
      print("example:", "taiutc.py 815302800")
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
      print("output time is:", end=" " )
   tai_minus_utc = taiutc(utctime)
   tai_minus_utc = taiutc(utctime)
   print(f"{tai_minus_utc}")

if __name__ == "__main__":
   main()

