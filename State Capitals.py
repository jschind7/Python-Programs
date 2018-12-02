import random
def main():
    state_capitals = {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
                      'Arkansas':'Little Rock','California':'Sacramento','Colorado':
                      'Denver','Connecticut':'Hartford','Delaware':'Dover','Florida':
                      'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu','Idaho':
                      'Boise','Illinois':'Springfield','Indiana':'Indianapolis','Iowa':
                      'Des Moines','Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':
                      'Baton Rouge','Maine':'Augusta','Maryland':'Annapolis',
                      'Massachusetts':'Boston','Michigan':'Lansing','Minnesota':
                      'Saint Paul','Mississippi':'Jackson','Missouri':'Jefferson City',
                      'Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City',
                      'New Hampshire':'Concord','New Jersey':'Trenton','New Mexico':
                      'Santa Fe','New York':'Albany','North Carolina':'Raleigh',
                      'North Dakota':'Bismarck','Ohio':'Columbus','Oklahoma':
                      'Oklahoma City','Oregon':'Salem','Pennsylvania':'Harrisburg',
                      'Rhode Island':'Providence','South Carolina':'Columbia',
                      'South Dakota':'Pierre','Tennessee':'Nashville','Texas':'Austin',
                      'Utah':'Salt Lake City','Vermont':'Montpelier','Virginia':
                      'Richmond','Washington':'Olympia','West Virginia':'Charleston',
                      'Wisconsin':'Madison','Wyoming':'Cheyenne'}
    wrong_answers = []
    print("Let's see how well you know the state capitals.")
    while len(state_capitals)>0:
        state = random.choice(list(state_capitals))
        correct_answer = state_capitals.get(state)
        print("What is the capital of",state,"?")
        guess = input(" ")
        if guess == correct_answer:
            print("That's right!")
            del state_capitals[state]
        else:
            print("Sorry. That is not the right answer.")
            print("The capital is",correct_answer)
            wrong_answers.append(state)
    print("You know",50-len(wrong_answers),"out of 50 state capitals.")
    if wrong_answers:
        print("These are the states you don't know:")
        for states in wrong_answers:
            print(states)
    else:
        print("Great job! You got them all right.")
play_again=""
while play_again != "n":
    main()
    play_again = input("Do you want to play again? (y/n)")
    

