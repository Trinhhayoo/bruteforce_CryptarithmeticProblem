from itertools import chain, permutations
from string import digits
def multiply_elements(lst):
    result = 1
    for element in lst:
        result *= element
    return result
def solve_cryptarithm(addends, result,calculation, parenthese):
    
    letters = ''.join(set(chain(result, *addends))) #những chữ cái tồn tại
    print(letters)
    initial_letters = ''.join(set(chain(result[0], (a[0] for a in addends)))) #chữ cái đầu
    print(initial_letters)
    
    for perm in permutations(digits, len(letters)): #perm: những khả năng
        
        
        decipher_table = str.maketrans(letters, ''.join(perm))
        
        def decipher(s):
            return s.translate(decipher_table)
        if '0' in decipher(initial_letters):
            
            continue # leading zeros not allowed
        leng = 0
        resultArr = []
        countRow = 0
        countCol = 0
        if len(parenthese) > 0:
            for i in range(len(parenthese)): 
                for j in range(parenthese[countRow][countCol],parenthese[countRow][countCol + 1],1):
                
                    resultArr.append(int(decipher(operands_list[j])))
                    print(resultArr[i])
                    if calculation[j] == "+":
                        resultArr[i] += int(decipher(operands_list[j+1])) 
                        print(resultArr[i])
                    elif calculation[j] == "*":
                        resultArr[i] *= int(decipher(operands_list[j+1]))
                print(resultArr[i])
           
        
        operator = 0
        countRow = 0
        countCol = 0
        countLoop = 0
        if parenthese[0][0] == 0:
            results = resultArr[0]
            countLoop += 1
        else:
            results = int(int(decipher(addends[0])))
            print(results)
            
        while operator  < len(calculation):
            if operator == parenthese[countRow][countCol] - 1:
                print("co ngoặc")
                if calculation[operator] == "+":
                    results += resultArr[countLoop]
                    countLoop += 1
                elif calculation[operator] == "*":
                    results *= resultArr[countLoop]
                    countLoop += 1
                operator += (parenthese[countRow][countCol+1] - parenthese[countRow][countCol] + 1 ) 
            elif calculation[operator] == "+":
                print("không ngoặc")
                
                results += int(decipher(addends[operator+1]))
                operator += 1
            elif calculation[operator] == "*":
                results *= int(decipher(addends[operator+1]))
                operator += 1
                
        if results == int(decipher(result)):
            def fmt(s):
                return f"{s}({decipher(s)})"
            print(" + ".join(map(fmt, addends)), "=", fmt(result))
            break
        
    else:
        print(" + ".join(addends), "=", result, " : no solution")
def parse_math_equation(equation):
    equation = equation.replace(" ", "")  # Remove spaces from the equation
    parts = equation.split("=")

    left_side = parts[0]
    right_side = parts[1]

    operands = []  # List to store the operands
    operators = []  # List to store the operators
    current_operand = ""  # Temporary variable to build the current operand
    parenthese_position = []
    countCol = 0
    countRow = 0

    for char in left_side:
        if char in ('+', '*'):  # If the character is an operator
            if current_operand:
                operands.append(current_operand)
                current_operand = ""
            operators.append(char)
        elif char in ('('):
            temp = len(operators)  # dấu ngoặc mở bằng lấy phần tử thứ đó
            countCol += 1
        elif char in (')'):
            parenthese_position.append([temp,len(operators)  ])#dấu ngoặc đóng lấy phần tử tới đó
            
        else:  # If the character is a digit or a variable
            current_operand += char

    if current_operand:  # Process the last operand (if any)
        operands.append(current_operand)

    return operands, operators, [right_side], parenthese_position
#stringCalculate = "SO + MANY + MORE + MEN + SEEM + TO + SAY + THAT + THEY + MAY + SOON + TRY + TO + STAY + AT + HOME + SO + AS + TO + SEE + OR + HEAR + THE + SAME + ONE + MAN + TRY + TO + MEET + THE + TEAM + ON + THE + MOON + AS + HE + HAS + AT + THE + OTHER + TEN =TESTS"
stringCalculate = "a + ( b + c ) + (a + b)= h "
operands_list, operators_list, result_operand, parentthese = parse_math_equation(stringCalculate)
result = result_operand[0]
print(operators_list)
solve_cryptarithm(operands_list, result,operators_list,parentthese)