out=$(find . -name "*.c" -o -name "*.h" | grep -v ./push_swap_visualizer | grep -v ./push_swap_tester | xargs norminette); [ $(echo "$out" | grep -c 'OK!') -eq $(echo "$out" | wc -l) ] && echo "OK" || echo "error"
