#!/usr/bin/env python3
"""
Usage: Convert TDT to ET (first-order approximation).
       Input is TDT. Output is ET (used to interpolating 
                     the planetary ephemeris file.      
       This is < 2 millisecond variation, cyclical over 365.2596438 days 
       The remaining terms are < 21 microseconds (2-17, Moyer)
"""
usage = __doc__

import math
import sys
import argparse

def tdt2et(tdt, verbose=False):
   eccb = 0.01671
   # Mean anomaly of the Earth-Moon barycenter
   mb = 6.239996 + 1.99096871e-7 * tdt
   # Eccentric anomaly (first-order)
   eb = mb + eccb * math.sin(mb)
   # Return first-order approximation
   et = tdt + 1.657e-3 * math.sin(eb)
   return (et)

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute tdt time from gps time")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("tdt",            type=float,  help="tdt input" )
#  this allows for no input so we can use input from a pipe 
   parser.add_argument("tdt", nargs="*", type=float,  help="tdt input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "tdt2et.py 815302800")
      quit()
#  allow for pipe input here
   if not sys.stdin.isatty():
      input_data = sys.stdin.read()
      tdtstring = input_data.split()
      tdttime = float( tdtstring[0] )
   else:
      if ( len(args.tdt) < 1 ):
         print(usage)
         quit()
      tdttime = float( args.tdt[0] )
   if ( args.verbose ):
      print(usage)
      print("input time was:", tdttime )
      print("output time is:", end=" " )
   ettime = tdt2et(tdttime)
   print(f"{ettime:18.6f}")

if __name__ == "__main__":
   main()
