current_movies = {'The Grinch':'11:00am',
                  'Rudolph':'1:00pm',
                  'Frosty the Snowman':'3:00pm',
                  'Christmas Vacation':'5:00pm'
                  }

print('Now showing')
for key in current_movies:
    print(key)

movie = input('pick a movie...')
if current_movies.get(movie) == None:
    print(f'{movie} not playing at this time')
else:
    print(f'{movie} shows at {current_movies.get(movie)}')