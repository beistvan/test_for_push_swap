#!/bin/bash
python3 chk35.py
echo
python3 chk100.py
echo
python3 pstester.py
echo
./t.sh
echo 
echo "Norm:"
./n.sh
