def convert_array_of_strings_to_dictionary(expresion_strings):
    expression_dictionary = {}
    for exp in expresion_strings:
        chopped = exp.split("=")
        expression_dictionary[chopped[0].strip()] = chopped[1].strip()
    return expression_dictionary


def find_answer(exp_to_find, expressions, previous_vars=[]):
    # This assuming that the expressions is a dictionary like above. We'll use this
    # to follow through
    current_expression = exp_to_find
    if current_expression.isnumeric():
        return current_expression
    previous_variables = previous_vars
    while not expressions[current_expression].isnumeric():
        operation = expressions[current_expression].split(' ')
        if len(operation) == 1:
            if expressions[current_expression] in previous_variables:
                return "IMPOSSIBLE"
            previous_variables.append(current_expression)
            current_expression = expressions[current_expression]
        else:
            op1 = operation[0]
            op2 = operation[2]
            if op1 in previous_variables or op2 in previous_variables:
                return "IMPOSSIBLE"
            previous_variables.append(op1)
            previous_variables.append(op2)
            operand1 = find_answer(op1, expressions, previous_variables)
            op = operation[1]
            operand2 = find_answer(op2, expressions, previous_variables)
            if op == '+':
                if operand1 == "IMPOSSIBLE" or operand2 == "IMPOSSIBLE":
                    return "IMPOSSIBLE"
                return str(int(operand1) + int(operand2))
            if op == '-':
                if operand1 == "IMPOSSIBLE" or operand2 == "IMPOSSIBLE":
                    return "IMPOSSIBLE"
                return str(int(operand1) - int(operand2))
            if op == '*':
                if operand1 == "IMPOSSIBLE" or operand2 == "IMPOSSIBLE":
                    return "IMPOSSIBLE"
                return str(int(operand1) * int(operand2))
            else:
                return None
    return expressions[current_expression]


def expressionsFirst(computeExp, expressions):
    expression_dictionary = convert_array_of_strings_to_dictionary(expressions)
    answer = find_answer(computeExp, expression_dictionary)
    return answer


def expressionsSecond(computeExp, expressions):
    expression_dictionary = convert_array_of_strings_to_dictionary(expressions)
    answer = find_answer(computeExp, expression_dictionary)
    return answer


def expressionsThird(computeExp, expressions):
    expression_dictionary = convert_array_of_strings_to_dictionary(expressions)
    answer = find_answer(computeExp, expression_dictionary)
    return answer


def expressionsFourth(computeExp, expressions):
    expression_dictionary = convert_array_of_strings_to_dictionary(expressions)
    answer = find_answer(computeExp, expression_dictionary)
    return answer