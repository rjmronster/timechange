#!/usr/bin/env python3
"""
Usage: This function will return TDT time given GPS time.
       Input is GPS. Output is TDT.
"""
usage = __doc__

import sys
import argparse

def gps2tdt(gps, verbose=False):
   tdttime = gps + 51.184
   return (tdttime)

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute gps time from tdt time")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("gpd",            type=float,  help="gps input" )
#  this allows for no input so we can use input from a pipe 
   parser.add_argument("gps", nargs="*", type=float,  help="gps input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "gps2tdt.py 815302800")
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
   tdttime = gps2tdt(gpstime)
   print(f"{tdttime}")

if __name__ == "__main__":
   main()
