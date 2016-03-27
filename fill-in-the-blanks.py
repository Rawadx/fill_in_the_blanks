# IPND Stage 2 Final Project



# The Quizes

sample1 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses.'''


sample2 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return.'''


sample3 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answers 
answers1 = ['function', 'arguments']
answers2 = ['function', 'arguments', 'None']
answers3 = ['function', 'arguments', 'None', 'list']

#The blanks
blanks1 = ['___1___', '___2___']
blanks2 = ['___1___', '___2___','___3___' ]
blanks3 = ['___1___', '___2___','___3___', '___4___' ]

#The levels
levels = ['easy', 'Easy', 'medium', 'Medium', 'hard', 'Hard']

#The trial options
trial_options = ['1','2','3','4','5']

#Prompts the user to choose the difficulty level of the quiz
def prompt_user_level():
    diff= raw_input("Select Difficulty: ")
    for e in levels:
        if diff ==e:
            return diff
    print "Enter valid level"
    return prompt_user_level()        
    
#Prompts the user to choose how many attempts/question they need
     
def prompt_user_trials():
    attempts= raw_input("How many guesses do you need? ")
    for e in trial_options:
        if attempts ==e:
            return attempts
    print "Enter valid level from 1 to 5"
    return prompt_user_trials()
    
    
# returns the quiz text as per difficulty level 
def quiz_text(level):
    if level.lower() == 'easy': 
        dataset=sample1
        return dataset
    if level.lower() == 'medium':
        dataset=sample2
        return dataset
    if level.lower() == 'hard':
        dataset=sample3
        return dataset
   

# returns the answers of the quiz chosen
def answers(level):

    if level.lower() == 'easy': 
        ans=answers1
        return ans
    if level.lower() == 'medium':
        ans=answers2
        return ans
    if level.lower() == 'hard':
        ans=answers3
        return ans   

# returns the list of blanks for the quiz chosen
def blanks_list(level):
    if level.lower() == 'easy': 
        dataset=blanks1
        return dataset
    if level.lower() == 'medium':
        dataset=blanks2
        return dataset
    if level.lower() == 'hard':
        dataset=blanks3
        return dataset


# checks if the response is correct and allows the user to make
# the number of trials/attempts specified
def attempts(trials, response, ans, index):
    i=1
    while i < trials:
        if response == ans[index]:
            print "Correct"
            return response
            break
        else:
            print "Wrong, Try again"
            print "You have " +str(trials-i)+ "trials remaining."
            response = raw_input("Answer " + str(index+1) + " is: ")            
        i+=1                
    
# returns the quiz with the blanks filled with the correct answers
def replace_blanks(quiz, response, blanks, index):
    replaced =[]
    quiz = quiz.split()  
    for e in quiz:
        if response !=None:
            e=e.replace(blanks[index], response)
            replaced.append(e)
        else:
            replaced.append(e)
    replaced = " ".join(replaced)
    return replaced

# choosing level and retrieving relevant data     
level = prompt_user_level()    
trials = int(prompt_user_trials())
quiz = quiz_text(level)
ans = answers(level)
#Main function 
def start_quiz(level, quiz, trials, ans):    
    index=0
    
    while index < len(ans):
        
        blanks=blanks_list(level)                  
        response = raw_input("Answer " + str(index+1) + " is: ")
        response =attempts(trials,response, ans, index)
        if response == None:
            break
        print replace_blanks(quiz, response, blanks, index)  # need to replace print statement
        index+=1
                

    return "That is the End of the Quiz"                    
print start_quiz(level, quiz, trials, ans)



# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
