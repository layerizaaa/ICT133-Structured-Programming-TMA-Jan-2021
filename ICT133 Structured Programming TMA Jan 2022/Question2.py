from random import randint
#Generate operands based on different levels 
def random_with_N_digits(level):
    range_start = 10**(level-1)
    range_end = (10**level)-1
    return randint(range_start, range_end)
    

#Generate operands based on different levels and operators
def getOperands(operator, level):
    if operator == '+':
        operand1 = random_with_N_digits(level)
        operand2 = random_with_N_digits(level)

    elif operator == '-':
        while True:
            operand1 = random_with_N_digits(level)
            operand2 = random_with_N_digits(level)
            if operand1 > operand2:
                break
            
    else: #operator == '*'
        operand2 = randint(2,9) 
        operand1 = random_with_N_digits(level) 
    return operand1, operand2


#Q2a Implement getExpression(level, operator) function
def getExpression(level, operator):
    operand1, operand2 = getOperands(operator, level)
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    question = input(f'{operand1} {operator} {operand2} = ')
    return question, result

#Q2b 

#User select highest level
def user_level():
    while True:
        level_select = int(input('Enter highest level to achieve (1-5): '))
        if level_select == 0 or level_select >5:
            print('Highest level must be between 1 and 5.')
        else:
            break
    return level_select


#Generate random operator
def random_operator():
    from random import sample
    operator = '+-*'
    shuffled_operator = sample(operator,len(operator)) #shuffle the order of operators using random.sample
    return shuffled_operator


#start of 3 questions per level  
def GenerateQuiz(current_level):   
    print(f'\n***Level {current_level}***\n') 
    countWrong = 0   #wrong answer counter
    shuffled_operator = random_operator() #Generate random operator               
    operator_len = -1                            
    for q in range(1,4):                               
        print(f'Q{q}.', end = ' ')
        operator_len += 1 
        question, result = getExpression(current_level,shuffled_operator[operator_len])
        #check if user entered correct answer
        if int(question) == result:
            print('Correct!\n')
        else: 
            print(f'Incorrect. The correct answer is {result}.\n')
            countWrong += 1
    return countWrong     


#Determine whether to move to next level 
def DetermineNxtLvl(correct, countWrong, current_level, level_select):
    if countWrong == 0 and current_level < level_select:
        correct = True
        input(f'Well Done! Press <Enter> to proceed to level {current_level+1}.')
        current_level +=1 #start new level when answers are all correct
    elif countWrong == 0 and current_level == level_select:
        correct = True
        print(f'Well done! You have completed the highest level {level_select}!')
        #end program when all levels are completed
    elif countWrong == 1:
        input('You have 1 error. Press <Enter> to repeat this level.')
    else:
        input(f'You have {countWrong} errors. Press <Enter> to repeat this level.')
    return correct, current_level


#Main Program
def main():
    #start of new level
    level_select = user_level() 
    current_level = 1 
    for levels in range(current_level, level_select+1):
        correct = False
        while not correct:
            countWrong = GenerateQuiz(current_level)
            correct, current_level = DetermineNxtLvl(correct, countWrong, current_level,level_select)
        

main()





        






