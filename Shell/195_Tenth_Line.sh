#!/bin/bash
sed -n 10p file.txt


# approach # 1
# (Another way of writing)

# awk 'NR == 10' file.txt

# approach # 2

# tail -n+10 file.txt|head -1

# approach # 3

cnt = 0
while read line && [$cnt -le 10]; do
    let 'cnt = cnt + 1'
    if [ $cnt -eq 10 ]; then
        echo $line
        exit 0
    fi
done < file.txt
