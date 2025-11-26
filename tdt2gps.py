#!/usr/bin/env python3
"""
Usage: This function will return GPS time given TDT time.
       Input is TDT. Output is GPS.
"""
usage = __doc__

import sys
import argparse

def tdt2gps(tdt, verbose=False):
   gpstime = tdt - 51.184
   return (gpstime)

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
      print("example:", "tdt2gps.py 815302800")
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
   gpstime = tdt2gps(tdttime)
   print(f"{gpstime}")

if __name__ == "__main__":
   main()
