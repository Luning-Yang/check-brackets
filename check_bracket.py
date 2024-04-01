def check_brackets(line):
    output_lines = []
    left_stack = [] 
    right_stack = [] 
    markers = [' '] * len(line)

    for i, char in enumerate(line):
        if char == '(':
            left_stack.append(i)
        elif char == ')':
            if left_stack:
                left_stack.pop()
            else:
                right_stack.append(i)

    for index in left_stack:
        markers[index] = 'x'

    for index in right_stack:
        markers[index] = '?'

    return line + "\n" + ''.join(markers)
