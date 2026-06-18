def calculate(expression):

    try:

        answer = eval(expression)

        return answer

    except:

        return "Invalid Expression"