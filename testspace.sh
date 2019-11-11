#!/bin/bash

function write_report {
    echo -ne $1 > /dev/hidg0
}

for i in {1..5}
do
