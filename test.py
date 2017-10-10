spy_age = 0

spy_age = int(raw_input("What is your age?"))
if spy_age > 12 and spy_age < 50:
           spy_rating = input("What is your spy rating?")
           if spy_rating > 4.5:
               print 'Great ace!'
           elif spy_rating > 3.5 and spy_rating <= 4.5:
               print 'You are one of the good ones.'
           elif spy_rating >= 2.5 and spy_rating <= 3.5:
               print 'You can always do better'
           else:
               print 'We can always use somebody to help in the office.'
else:
    print 'Sorry you are not of the correct age to be a spy'