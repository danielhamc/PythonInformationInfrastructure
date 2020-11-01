# Instructions:
# COPY YOUR MOVIE CLASS HERE, OR OURS FROM ONSCREEN
# You don't need the child classes, just Movie



# Once you've done that, add methods to override
# The > and == operators.



# WHY DO WE CARE? Adding these override methods
# will allow you to use .sort() and sorted() on a
# list of movies (given below), without writing any other code!

# No changes to the code below here!
movies = [Movie("The Extremely Disreputable Budapest Hotel", 2),
          Movie("Inside Out 2: Total Rage", 4),
          Movie("Star Wars: episode VIII - Luke Sulks For Two Hours", 1),
          Movie("The Martian 2 - Revenge of the Potato", 6),
          Movie("Zootopia Vs The Jungle Book", 5),
          Movie("Losing Dory", 3),
          Movie("Guardians of the Galaxy 2: Endless Dance-off", 7),
          Movie("Captain America: Tony Stark Takes His Medication", 8),
          Movie("The Lego my Eggo Movie", 5),
          Movie("Three Days, Two Nights, Business Economy Class", 2),
          Movie("Mad Max: Really Peaceful Road", 6),
          Movie("Dawn of the Revenge of the Sequel of the Movie About Apes", 3)]

print("The movies, sorted by rating:")
print("-" * 70)
for movie in sorted(movies):
    print(movie)
