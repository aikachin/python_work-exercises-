# test 3-4
invite_people = ['jack', 'hellon', 'winter']
message = 'People I wanna to invite to have dinner with me are : ' + invite_people[0].title() + ', ' + invite_people[1].title() + ', ' + invite_people[2].title() + '.'
print(message)
print("However, " + invite_people[0].title() + " can't not make time to join me.")
invite_people[0] = "tommy"
#invite_people.append('tommy')
message2 = 'Finally, I invite them to have dinner with me: ' + invite_people[0].title() + ', ' + invite_people[1].title() + ', ' + invite_people[2].title() + '.'
print(message2)
message3 = ", would you like to have dinner with me?"
print(invite_people[0].title() + message3)
print(invite_people[1].title() + message3)
print(invite_people[2].title() + message3)
print("Oh, I've find a bigger table for dinner. I would like to invite more friends to join us.")
invite_people.insert(0, 'David')
invite_people.insert(2, 'Ketty')
invite_people.append('John')
print(invite_people[0].title() + message3)
print(invite_people[1].title() + message3)
print(invite_people[2].title() + message3)
print(invite_people[3].title() + message3)
print(invite_people[4].title() + message3)
print(invite_people[5].title() + message3)
message4 = "I'm so sorry to tell you that my table can reach tonight. So I can only use the old table which is not big enough for more than 3 persons to have dinner."
print(message4)
guest1 = invite_people.pop(-2)
guest2 = invite_people.pop(-1)
guest3 = invite_people.pop()
guest4 = invite_people.pop()
message5 = ", I'm afraid I have to tell you that the party of tonight is cancelled. Maybe the next time ~ "
print(guest1 + message5)
print(guest2 + message5)
print(guest3 + message5)
print(guest4 + message5)
message6 = ", don't worry. We still could have dinner together tonight."
print(invite_people[0] + message6)
print(invite_people[1] + message6)
del invite_people[1]
del invite_people[0]
print(invite_people)
