#!/usr/bin/env bash

cat access.log | cut -d ' ' -f1 | sort  | uniq -c |  tr -s ' ' | sort -t ' ' -k2nr | head -n 10