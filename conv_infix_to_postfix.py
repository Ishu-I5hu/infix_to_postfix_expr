# <----- conv_infix_to_postfix.py ----->
"""
    Title: Conversion of infix into postfix expression.
    Author: Ishu
    Version: v1.0
"""
"""
    Aim: To convert given infix expression into postfix expression.
"""

OPERATORS = tuple('+-*/^')
PRECEDENCE = {'^':3, '*':2, '/':2, '+':1, '-':1,}

def get_str(string, space):
    """ Return provided string with appropriate no. of white spaces, so that it looks like a tabular column. """
    return string + (" " * (space - len(string)))

def main():
    """ Main function of the program. """
    stack = ''
    postfix_exp = ''
    exp_inp = input('\nEnter infix expr to convert to postfix expr: ').strip() # (A+B)*C/D
    exp = '(' + exp_inp.replace(" ", "") + ')'

    print('Infix expression:', exp, '\n')
    print(' '*2, get_str('S.No.', 6), get_str('Symbol', 8), get_str('Stack', 10), get_str('Postfix_exp', 20))
    # print('\n%5s'%'S.No.', '%8s'%'Symbol', '%10s'%'Stack', '%20s'%'Postfix_exp')
    print(' ', '----------------------------------------')

    for (i,sym) in enumerate(exp):
        if sym == '(':
            stack += sym

        elif sym in OPERATORS:
            if stack[-1] in OPERATORS:
                if PRECEDENCE[stack[-1]] >= PRECEDENCE[sym]:
                    postfix_exp += stack[-1]
                    stack = stack[:-1] + sym
                else: stack += sym
            else: stack += sym

        elif sym == ')':
            while stack[-1] != '(':
                postfix_exp += stack[-1]
                stack = stack[:-1]
            stack = stack[:-1]

        else:
            postfix_exp += sym      # Operand case

        print(' '*3, get_str(str(i+1), 7), get_str(sym, 6), get_str(stack or 'Empty', 10), get_str(postfix_exp or '~', 20))
    print('\nPostfix expression:', postfix_exp)

if __name__ == '__main__':
    while True:
        main()
        cnt = input('Want to continue? (Y/N): ').strip()
        if not cnt or cnt not in 'Yy1': break
