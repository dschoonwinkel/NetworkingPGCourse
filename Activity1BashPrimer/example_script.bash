#!/bin/bash
# example_script.bash

#Example if statement
if [[ $1 == '1' ]]; then
	echo $1

else
	echo "Why did you not type 1?"
fi

# Example for loop
for i in `seq 1 3`;
do
	echo $i
done