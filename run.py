#!/usr/bin/env python

import argparse
import sys
import os
from subprocess import Popen, PIPE

#/*
sim_sizes = {'hashmap' : {'test':'sudo bash run_hashmap.sh'},
            'ctree' : {'test' : 'sudo bash run_ctree.sh'}}

def runCmd(cmd, err, out):
    """
    Takes two strings, command and error, runs it in the shell
    and then if error string is found in stdout, exits.
    For no output = no error, use err=""
    """
    print cmd
    (stdout, stderr) = Popen(cmd, shell=True, stdout=PIPE).communicate()
    if stdout:
        print stdout
    if stderr:
        print stderr
    if err is None:
        if stdout != "":
            print "Error: %s" %(out,)
            print "Truncated stdout below:"
            print '... ', stdout[-500:]
            sys.exit(2)
    else:
        if err in stdout:
            print "Error: %s" %(out,)
            print "Truncated stdout below:"
            print '... ', stdout[-500:]
            sys.exit(2)

def main(argv): 
    """
    Parses the arguments and cleans and/or builds the specified
    workloads of the whisper suite
    """
    parser = argparse.ArgumentParser(description='Runs nvml workloads from the whisper suite.')
    parser.add_argument('benchmarks', metavar='workload', type=str, nargs=1,
                help='workloads to be run: ctree/hashmap')
    parser.add_argument('--sim_size', dest='sim_size', action='store', 
            default='test', help='Simulation size: test')

    args = parser.parse_args()
    print 'Running a ' + str(args.sim_size) + ' simulation for ' + str(args.benchmarks)
        
    if args.sim_size in sim_sizes[args.benchmarks[0]]:
        runCmd(sim_sizes[args.benchmarks[0]][args.sim_size], "Error", "Simulation failed")    
    else:
        print "Simulation size: " + str(args.sim_size) + " not found for workload:" + str(args.benchmarks[0])

if __name__ == "__main__":
    main(sys.argv[1:])
