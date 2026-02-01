#!/bin/bash
echo "test"
echo "arg1: $1"
echo "arg2: $2"
VAR=$(echo "echo arg3: $3")
$VAR
echo "$#"
