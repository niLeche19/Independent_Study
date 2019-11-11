#!/bin/bash

#function write_report {
#    echo -ne $1 > /dev/hidg0
#}

pins=(2 3 4 17 27 22 10 9 11 20 5 6 13 19 26 21)

printf "all the pins are setup"

#while $[0==$(</sys/class/gpio/gpio13/value)]; do
while true; do
	for f in ${pins[@]}; do
		if [ 1=="$(</sys/class/gpio/gpio"$f"/value)" ]; then
			printf "pin $f is down\n"
		else
			printf "CLOSED\n"
		fi
	done
	sleep 0.05
done

