#!/bin/bash

set -e
if [ -f "./.git-hook-set-env.sh" ]; then
    . ./.git-hook-set-env.sh
fi

make migrations-check
