#!/bin/bash

#function write_report {
#    echo -ne $1 > /dev/hidg0
#}

pins=(2 3 4 17 27 22 10 9 11 20 5 6 13 19 26 21)

for i in ${pins[@]}; do
	echo "$i" > /sys/class/gpio/export
	echo "in" > /sys/class/gpio/gpio$i/direction
done

printf "all the pins are setup"

while true; do
	for f in ${pins[@]}; do
		if [0 == "$(</sys/class/gpio/gpio"$f"/value)" ]; then
			printf "pin $f is down"
		fi
	done
	sleep 0.05
done

