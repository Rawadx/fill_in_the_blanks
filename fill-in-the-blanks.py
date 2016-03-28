# IPND Stage 2 Final Project

# The Quizes

easy_quiz = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''


medium_quiz = '''Python is an interpreted, ___1___, high-level programming language with dynamic ___2___.
Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive
for ___3___ Development, as well as for use as a __4___ or glue language to connect existing components
together.'''

hard_quiz = '''Python was created in the early 1990s by ___1___ at Stichting Mathematisch Centrum
in the ___2___ as a successor of a language called ___3___. Guido remains Python’s principal author,
although it includes many contributions from others. All Python releases are ___4___. Historically, most,
but not all, Python releases have also been ___5___ compatible.'''



# answers 
answers_easy = ['function', 'arguments','None', 'list']
answers_medium= ['object-oriented', 'semantics', 'Rapid Application', 'scripting']
answers_hard = ['Guido van Rossum', 'Netherlands', 'ABC', 'Open Source', 'GPL' ]

# blanks
blanks_easy = ['___1___', '___2___','___3___', '___4___' ]
blanks_medium = ['___1___', '___2___','___3___', '___4___' ]
blanks_hard = ['___1___', '___2___','___3___', '___4___' ,'___5___']

# levels
levels = ['easy', 'Easy', 'medium', 'Medium', 'hard', 'Hard']

# Attempts choices
trial_options = ['1','2','3','4','5']

#Prompts the user to choose the difficulty level of the quiz
def prompt_user_level():
    diff= raw_input("Select Difficulty (easy, medium or hard): ")
    for e in levels:
        if diff ==e:
            return diff
    print "Enter valid level: easy, medium or hard"
    return prompt_user_level()        
    
#Prompts the user to choose how many attempts/question they need
     
def prompt_user_trials():
    attempts= raw_input("How many guesses do you need? ")
    for e in trial_options:
        if attempts ==e:
            return attempts
    print "Please Enter a numbber from 1 to 5"
    print "_ _ _ _ _"
    return prompt_user_trials()
    
    
# returns the quiz text as per difficulty level

def quiz_text(level):
    if level.lower() == 'easy': 
        dataset=easy_quiz
        return dataset
    if level.lower() == 'medium':
        dataset=medium_quiz
        return dataset
    if level.lower() == 'hard':
        dataset=hard_quiz
        return dataset
   

# returns the answers related to the quiz chosen
def answers(level):

    if level.lower() == 'easy': 
        ans=answers_easy
        return ans
    if level.lower() == 'medium':
        ans=answers_medium
        return ans
    if level.lower() == 'hard':
        ans=answers_hard
        return ans   

# returns the list of blanks related to the quiz chosen
def blanks_list(level):
    if level.lower() == 'easy': 
        dataset=blanks_easy
        return dataset
    if level.lower() == 'medium':
        dataset=blanks_medium
        return dataset
    if level.lower() == 'hard':
        dataset=blanks_hard
        return dataset


# checks if the response is correct and allows the user to make
# the number of trials/attempts specified
def attempts(trials, response, ans, index):
    i=1
    while i < trials:
        if response == ans[index]:
            print "Correct"
            print "_ _ _ _ _"
            return response
            break
        else:
            print "Wrong, Try again"
            print "You have " +str(trials-i)+ " trial(s) remaining."
            response = raw_input("Answer " + str(index+1) + " is: ")            
        i+=1                
    
# returns the quiz with the blanks replaced by the correct answers
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

# assigning levels, trials, qiuz and answers     
level = prompt_user_level()    
trials = int(prompt_user_trials())
quiz = quiz_text(level)
ans = answers(level)

# Main function 
def start_quiz(level, quiz, trials, ans):

    print quiz
    print "_ _ _ _ _"
    index=0   
    while index < len(ans):
        
        blanks=blanks_list(level)
        response = raw_input("Answer " + str(index+1) + " is: ")
        response =attempts(trials,response, ans, index)
        if response == None:
            break
        print replace_blanks(quiz, response, blanks, index)
        print "_ _ _ _ _"
        quiz = str(replace_blanks(quiz, response, blanks, index))
        index+=1
                

    return "You've reached the End of the Quiz"                    
print start_quiz(level, quiz, trials, ans)



# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/
