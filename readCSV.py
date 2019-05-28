#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="csv file name with extension")
parser.add_argument("--verbose", help="increase output verbosity", action="store_true") #optionel
args = parser.parse_args()

if args.verbose:
    print("Reading:", args.filename)

try:
  f = open(args.filename, encoding='utf-8')
except:
  print ("Could not read file:", args.filename)
  exit()


for line in f:
    field1, field2, field3=line.split(';')
    print(field1)

f.close()
