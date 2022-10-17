#/bin/bash

# A really quick script to runt he container with a bind mount

docker run -t -w /src -v $(pwd):/src ecoadapt-container
