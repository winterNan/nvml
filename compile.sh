#!/bin/bash
make clean
make EXTRA_CFLAGS="-D_ENABLE_FTRACE -Wno-error"
