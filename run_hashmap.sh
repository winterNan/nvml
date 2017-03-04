#!/bin/bash

export PMEM_TRACE_ENABLE=y     # y or n
export PMEM_NO_MOVNT=1
export PMEM_MMAP_HINT=0x0000100000000000
export PMEM_IS_PMEM_FORCE=1
LD_LIBRARY_PATH=./src/debug:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=./src/debug:$LD_LIBRARY_PATH
dir=/dev/shm/hashmap-testfile

action=$1

bin="./src/benchmarks/pmembench map_insert"

if [[ $action == '-h' ]]
then
        $bin -h
else
	$bin -f $dir -d 128 -n 102400 -t 4 -r 1 -T hashmap_tx
fi

#strace -f -e trace=write ./src/benchmarks/pmembench map_insert -f $dir -d 128 -n 1 -t 1 -r 1 -T ctree   
#gdb --args ./src/benchmarks/pmembench map_insert -f $dir -d 128 -n 1 -t 1 -r 1 -T ctree   


