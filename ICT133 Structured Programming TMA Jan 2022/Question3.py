#Q3a Implement getPlayers() function
def getPlayers():
    #Up to 26 players
    Name_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #Up to 26 players 
    while True:
        NoOfPlayers = int(input('Enter number of players: '))
        if NoOfPlayers < 2:
            print('Please enter at least 2 players.')
        else:
            break

    Player_names = Name_list[:NoOfPlayers]
    print(f'{NoOfPlayers} players {Player_names}')
    return NoOfPlayers, Player_names


#Q3b

from random import randint
#Generate operands based on different levels 
def random_with_N_digits(level):
    from random import randint
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


#Implement getExpression(level, operator) function
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


#Generate random operator
def random_operator():
    from random import choice
    operator = ['+', '-', '*']
    #choose random operator
    return choice(operator)


#Generate questions based on level and players
def GenerateQuiz(NoOfPlayers, Player_names, current_level):    
    print(f'\n***Level {current_level}***\n') 
    operator = random_operator() #Generate random operator   
    n = 0                                    
    for q in range(1,NoOfPlayers+1):   
        current_player = Player_names[n]                       
        print(f'Player {current_player},', end = ' ')
        question, result = getExpression(current_level, operator)
        #check if user entered correct answer
        if int(question) == result:
            print('Correct!\n')
            n += 1
        else: 
            print(f'Incorrect! Player {current_player} is eliminated.\n')
            Player_names.remove(current_player)
        current_NoofPlayers = len(Player_names)
    return Player_names, current_NoofPlayers


#Determine who moves to next level/who wins 
def DetermineNxtLvl(correct, NoOfPlayers, current_NoofPlayers, current_level, Player_names):
    #lone player wins
    if current_NoofPlayers == 1: 
        print(f'Player {Player_names} is the winner!')
        correct = True
    #winners progress to next level
    elif current_NoofPlayers < NoOfPlayers:
        print(f'Players {Player_names} progress to the next level {current_level+1}.')
        current_level += 1
        NoOfPlayers = current_NoofPlayers
    #no winners, repeat level
    else:
        print(f'Players {Player_names} will challenge same level {current_level} again.')
    return NoOfPlayers, current_level, correct


#Main Program
def main():
    NoOfPlayers, Player_names = getPlayers() 
    #start of new level
    current_level = 1
    correct = False
    while not correct:
        Player_names, current_NoofPlayers = GenerateQuiz(NoOfPlayers, Player_names, current_level)
        NoOfPlayers, current_level, correct = DetermineNxtLvl(correct, NoOfPlayers, current_NoofPlayers, current_level, Player_names)

   
main()
