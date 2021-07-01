import random
when = ['Yesterday', 'Last weekend', 'Two weeks ago', 'This afternoon', 'This evening']
name = ['Priya', 'Sarah', 'Ishmael', 'Emily', 'Tyler']
location = ['Denver', 'Seattle', 'Portland', 'Houston', 'New York City']
went = ['laundromat', 'shower', 'sleep', 'cinema', 'college']
happened = ['made friends', 'was late to work', 'listened to music', 'studied for exams', 'met a new employee']

print( random.choice(when) + ", " + random.choice(name) + " who lives in " + random.choice(location) + " went to " + random.choice(went) + " and " + random.choice(happened))