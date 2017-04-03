#!/bin/python3
# Primzahlen herausfinden
# Primtzahl ist eine Zahl, die nur durch 1 und sich selbst ganzzahlig teilbar ist

#parse command-line options and arguments
import sys
# Get first Argument from Terminal and set it as end
end = list(sys.argv)

#Startwert
i=3
#Definition der kleinsten Startprimzahl, die beide eigenschaften in sich vereint
prims=[2]

while (i <= int(end[1])):
  b = True
  for prim in prims:
    if (i % prim == 0):
      b = False
      break
  if (b == True):
    # Print each Prime after its calculation
    print(i)
    prims.append(i)
  # +2 because even numbers (except of 2) can't be prims
  i += 2

# Print Primes-Vector at the end of the run
#print(prims)
