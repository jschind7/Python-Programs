import random
morse_code = {'._':'a','_...':'b','_._.':'c','_..':'d','.':'e','.._.':'f',
              '__.':'g','....':'h','..':'i','.___':'j','_._':'k','._..':'l',
              '__':'m','_.':'n','___':'o','.__.':'p','__._':'q','._.':'r',
              '...':'s','_':'t','.._':'u','..._':'v','.__':'w','_.._':'x',
              '_.__':'y','__..':'z'}
i = 0
wrong_answers = 0
while i<10:
    random_letter = random.choice(list(morse_code))
    answer = morse_code.get(random_letter)
    print("What letter is this?",random_letter)
    guess = input("# ")
    if guess==answer:
        print("Correct!")
    else:
        print("Sorry, that's not right.")
        print("The answer is",answer)
        wrong_answers += 1
    i+=1
print("You got",10-wrong_answers,"out of 10 questions correct")
print("Good Job!")
