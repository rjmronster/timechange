#!/usr/bin/env python3
"""
Usage: This function will return TDT time given UTC time.
       Input is UTC. Output is TDT.
"""
usage = __doc__

import sys
import argparse
from taiutc import taiutc

def utc2tdt(utc, verbose=False):
   return (taiutc(utc) + utc + 32.184)

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "compute tdt time from utc time")
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("utc",            type=float,  help="utc input" )
#  this allows for no input so we can use input from a pipe 
   parser.add_argument("utc", nargs="*", type=float,  help="utc input" )
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outout")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "utc2tdt.py 815302800")
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
   tdttime = utc2tdt(utctime)
   print(f"{tdttime}")

if __name__ == "__main__":
   main()
