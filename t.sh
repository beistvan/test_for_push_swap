#!/bin/bash

checker="./checker"

echo "Bonus 'checker' tests"

echo -n "Error handling tests: "
for i in {1..16}; do 
    ARG="$(cat push_swap_tester/trace_basic/error_files/test_case_$i.txt)"
    output=$($checker $ARG 2>&1 | grep -o "Error")
    if [ "$output" == "Error" ]; then
        echo -e -n "\e[32mOK\e[0m "
    else
        echo -e -n "\e[31mKO\e[0m "
    fi
done

echo
echo -n "Empty handling tests: "
ARG="$(cat push_swap_tester/trace_basic/identity_files/test_case_1.txt)"
output=$(./push_swap $ARG | $checker $ARG 2>&1)
if [ -z "$output" ]; then
    echo -e -n "\e[32mOK\e[0m "
else
    echo -e -n "\e[31mKO\e[0m "
fi

echo
echo -n "Identity handling tests: "
for i in {2..9}; do 
    ARG="$(cat push_swap_tester/trace_basic/identity_files/test_case_$i.txt)"
    output=$(./push_swap $ARG | $checker $ARG 2>&1 | grep -o "OK")
    if [ "$output" == "OK" ]; then
        echo -e -n "\e[32mOK\e[0m "
    else
        echo -e -n "\e[31mKO\e[0m "
    fi
done

echo
echo -n "Shuffle tests for 20 elements: "
for i in {1..20}; do 
    ARG=$(echo {1..500} | tr ' ' '\n' | shuf | tr '\n' ' ')
    output=$(./push_swap $ARG | $checker $ARG 2>&1)
    if [ "$output" == "OK" ]; then
        echo -e -n "\e[32mOK\e[0m "
    else
        echo -e -n "\e[31mKO\e[0m "
    fi
done

#ARG="4 67 3 87 23"; ./push_swap $ARG | funcheck ./checker $ARG 

#ARG="4 67 3 87 23"; ./push_swap $ARG | valgrind --leak-check=full ./checker $ARG
