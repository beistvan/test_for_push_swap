import itertools
import random
import subprocess
from termcolor import colored
import sys

def apply_operation(stack_a, stack_b, operation):
    if operation == 'sa' and len(stack_a) > 1:
        stack_a[0], stack_a[1] = stack_a[1], stack_a[0]
    elif operation == 'sb' and len(stack_b) > 1:
        stack_b[0], stack_b[1] = stack_b[1], stack_b[0]
    elif operation == 'ss':
        apply_operation(stack_a, stack_b, 'sa')
        apply_operation(stack_a, stack_b, 'sb')
    elif operation == 'pa' and stack_b:
        stack_a.insert(0, stack_b.pop(0))
    elif operation == 'pb' and stack_a:
        stack_b.insert(0, stack_a.pop(0))
    elif operation == 'ra' and stack_a:
        stack_a.append(stack_a.pop(0))
    elif operation == 'rb' and stack_b:
        stack_b.append(stack_b.pop(0))
    elif operation == 'rr':
        apply_operation(stack_a, stack_b, 'ra')
        apply_operation(stack_a, stack_b, 'rb')
    elif operation == 'rra' and stack_a:
        stack_a.insert(0, stack_a.pop())
    elif operation == 'rrb' and stack_b:
        stack_b.insert(0, stack_b.pop())
    elif operation == 'rrr':
        apply_operation(stack_a, stack_b, 'rra')
        apply_operation(stack_a, stack_b, 'rrb')

if len(sys.argv) > 1:
    num_of_tests = int(sys.argv[1])
else:
    num_of_tests = 100

int_min = -2147483648
int_max = 2147483647

for _ in range(num_of_tests):
    permutation = random.sample(range(int_min, int_max + 1), 100)

    permutation_str = ' '.join(map(str, permutation))

    push_swap_process = subprocess.run(['./push_swap', permutation_str], capture_output=True, text=True)
    push_swap_output = push_swap_process.stdout.strip().replace('\n', ' ')

    operation_count = len(push_swap_output.split())

    stack_a = list(permutation)
    stack_b = []
    for operation in push_swap_output.split():
        apply_operation(stack_a, stack_b, operation)

    if len(permutation) == 100 and operation_count <= 700 or len(permutation) == 500 and operation_count <= 5500:
        operation_count_str = colored(str(operation_count), 'green')
    else:
        operation_count_str = colored(str(operation_count), 'red')

    if stack_a == sorted(stack_a) and not stack_b:
        print(f'({operation_count_str:>3}){colored("OK", "green")},', end='')
    else:
        print(f'({operation_count_str:>3}){colored("KO", "red")},', end='')
