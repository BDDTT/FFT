#!/usr/bin/env bash

#original_compact  original_full  smaller_compact  smaller_full 
#compact  double_compact  half_compact
#1-10

#/original/compact/bfloat
for age in "reduced" "original"; do
  for size in "compact" "full"; do
    for hw in "half" "double" "bfloat16"  ; do
  		for n in {1..12}; do			
  			filename="/home/crc/sgen/$age/$size/$hw/$n/itproduct_utilization_placed.rpt"
  			echo $filename | python stats.py  > "${age}_${size}_${hw}_${n}.txt" #2>&1
#		echo "${age}_${size}_${hw}_${n}.txt"
  		done
  	done
  done
done
