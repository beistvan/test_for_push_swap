import itertools
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
    num_of_tests = 5

print(f'Running tests for permutation of {num_of_tests} numbers...')
print('Usage : python3 chk35.py [<num_of_numers_in_permutation>]')
print('If not specified, the default number of numbers in permutation is 5.')

for n in range(num_of_tests, num_of_tests + 1):
    for permutation in itertools.permutations(range(1, n + 1)):

        if permutation == tuple(range(1, n + 1)):
            continue

        permutation_str = ' '.join(map(str, permutation))

        push_swap_process = subprocess.run(['./push_swap', permutation_str], capture_output=True, text=True)
        push_swap_output = push_swap_process.stdout.strip().replace('\n', ' ')

        operation_count = len(push_swap_output.split())
      
        stack_a = list(permutation)
        stack_b = []
        for operation in push_swap_output.split():
            apply_operation(stack_a, stack_b, operation)

        operation_count_str = colored(str(operation_count), 'red') if n == 5 and operation_count > 12 else colored(str(operation_count), 'green')
        if stack_a == sorted(stack_a) and not stack_b:
            print(f'{permutation_str:<10} - {push_swap_output:<40} ({operation_count_str:>3}) {colored("OK", "green")}')
        else:
            print(f'{permutation_str:<10} - {push_swap_output:<40} ({operation_count_str:>3}) {colored("KO", "red")}')
