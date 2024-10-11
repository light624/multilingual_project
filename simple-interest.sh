#!/bin/bash
# simple-interest.sh
echo "Enter the principal amount:"
read principal
echo "Enter the rate of interest:"
read rate
echo "Enter the time (in years):"
read time
interest=$(echo "$principal * $rate * $time / 100" | bc -l)
echo "The simple interest is: $interest"
