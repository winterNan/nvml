#!/bin/bash
#make distclean
#./src/cleanup.sh

make clean
make all STATIC_LINK_PMEMBENCH=yes NVML_DEBUG=yes USE_NVML=yes STD=-std=gnu99 EXTRA_CFLAGS="-D_ENABLE_UTRACE -Wno-error" 
# make NVML_DEBUG=yes USE_NVML=yes STD=-std=gnu99 EXTRA_CFLAGS="-D_ENABLE_FTRACE -Wno-error -static -static-libgcc" EXTRA_LDFLAGS="-static"
#make NVML_DEBUG=yes USE_NVML=yes STD=-std=gnu99 EXTRA_CFLAGS="-Wno-error" 
