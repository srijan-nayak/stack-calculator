prompt_input = ''
operand_stack = []
operators = {'+', '-', '*', '/', '//', '%', '**'}


def operate_with(prompt_input):
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    result = 0
    if prompt_input == '+':
        result = operand1 + operand2
    elif prompt_input == '-':
        result = operand1 - operand2
    elif prompt_input == '*':
        result = operand1 * operand2
    elif prompt_input == '/':
        result = operand1 / operand2
    elif prompt_input == '//':
        result = operand1 // operand2
    elif prompt_input == '%':
        result = operand1 % operand2
    elif prompt_input == '**':
        result = operand1 ** operand2
    operand_stack.append(result)


print('Enter h for help')
while prompt_input != 'q':
    print('Stack:', operand_stack)
    prompt_input = input('> ')
    if prompt_input.isnumeric():
        operand_stack.append(int(prompt_input))
    elif prompt_input in operators:
        if len(operand_stack) < 2:
            print('Not enough operands to operate with!')
            continue
        operate_with(prompt_input)
    elif prompt_input.lower() == 'x':
        operand_stack.pop()
    elif prompt_input == 'h':
        print('q: Quit')
        print('x: Pops last element from stack')
        print('<number>: Pushes <number> to stack')
        print('<operator>: Pushes <2nd last element>'
              ' <operator> <last element> to stack')
