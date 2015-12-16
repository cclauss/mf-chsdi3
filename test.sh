#!/bin/sh

cd /wwwwwwwwww/

exit_code=$?

if [ "$exit_code" -gt "0" ]; then
  echo "Exit code is:"
  echo "$exit_code"
fi
