current_movies = {'The Grinch':'11:00am',
                    'Rudolph':'1:00pm',
                    'Frosty The Snowman':'3:00pm'}
print("We're currently showing the following movies: ")
for key in current_movies:
    print(key)
userchoice = input('What Movie Would you Like to see:\n')
showtime = current_movies.get(userchoice)   
if showtime == None:
    print("The requested showtime is not available!")
else:
    print(userchoice, 'is playing at', showtime)
    
""" if userchoice == "The Grinch":
    print('The movie starts at ', current_movies['The Grinch'])
elif userchoice == "Rudolph":
    print('The movie starts at ', current_movies['Rudolph'])
elif userchoice == "Frosty The Snowman":
   print('The movie starts at ', current_movies['Frosty The Snoman'])
elif userchoice != current_movies:
    print('This is not a valid choice') """