#!/usr/bin/env python3
"""
Usage: This function will create a leap table and return on request.
"""
usage = __doc__

import sys
import argparse

def loadleap(verbose=False):
   # Static initialization using function attribute
   if not hasattr(loadleap, "leap"):
      loadleap.leap = {
         "x": [ -284040000,  # 01-JAN-1991
                -236779200,  # 01-JUL-1992
                -205243200,  # 01-JUL-1993
                -173707200,  # 01-JUL-1994
                -126273600,  # 01-JAN-1996
                 -79012800,  # 01-JUL-1997
                 -31579200,  # 01-JAN-1999
                 189345600,  # 01-JAN-2006
                 284040000,  # 01-JAN-2009
                 394372800,  # 01-JUL-2012
                 488980800,  # 01-JUL-2015
                 536500800,  # 01-JAN-2017
              ],
         "y": [ 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37 ]
      }
   leap = loadleap.leap
   return leap

def main():
#  this is shown with --help and -h
   parser = argparse.ArgumentParser(description = "load leap table" )
#  this inputs string to float, if mulitple inputs, use nargs="+"
#  this is a required/positional input
#  parser.add_argument("utc", type=float, help="utc input" )
#  this allows for no input so we can use input from a pipe
#  parser.add_argument("utc", nargs="*", type=float, help="utc input" ) # no inputs required
   parser.add_argument("-v","--verbose", action="store_true", help="Enable verbose outoup")
   parser.add_argument("-e","--example", action="store_true", help="Provide example")
   args = parser.parse_args()
   if ( args.example ):
      print(usage)
      print("example:", "loadleap.py" ) 
      quit()
#  allow for pipe input here
#  if not sys.stdin.isatty():
#     input_data = sys.stdin.read()
#     utcstring = input_data.split()
#     utctime = float( utcstring[0] )
#  else:
#     if ( len(args.utc) < 1 ):
#        print(usage)
#        quit()
#     utctime = args.utc[0]
#  if ( args.verbose ):
#     print(usage)
#     print("input time was:", utctime )
#     print("output time is:", end=" " )
   leaptable = loadleap()
   for i,j in zip( leaptable['x'],leaptable['y']):
       print( f"{i:14.2f}", f"{j:5d}" )

if __name__ == "__main__":
   main()

