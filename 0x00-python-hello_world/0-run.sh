#!/bin/bash

if [ -z "$PYFILE" ]; then
    echo "Error: The PYFILE environment variable is not set."
    exit 1
fi

if [! -f "$PYFILE" ]; then
    echo "Error: The specified Python file '$PYFILE' does not exist."
    exit 1
fi

python "$PYFILE"