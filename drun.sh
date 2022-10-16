#/bin/bash

# A really quick script to runt he container with a bind mount

docker run -w /src -v $(pwd):/src ecoadapt-container
