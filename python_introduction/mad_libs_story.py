# Mad libs story

# define variables with prompting user for input

weather_adj = input("Enter an adjective to describe the day: ")
monkey_adj = input("Enter an adjective to describe the monkey: ")
lion_adj = input("Enter an adjective to describe the lion: ")
experience_adj = input("Enter an adjective to describe the experience: ")
favorite_animal = input("Enter your favorite animal: ").lower()

# build the story using the input variables
print("\n Here is your mad libs story:\n")

story = f"On a beautiful {weather_adj} day, I went to the zoo. "
story += f"I saw a {monkey_adj} monkey swinging from tree to tree. "
story += f"Next, I saw a {lion_adj} lion lounging in the sun. "

# add the conditons to the story based on the favorite animal
if favorite_animal == "elephant":
    story += "I saw an elephant spraying water with its trunk, which was quite a sight!"
elif favorite_animal == "giraffe":
    story += "I saw a giraffe reaching high into the trees to eat leaves, its long neck was fascinating!" 
elif favorite_animal == "panda":
    story += "I saw a panda munching on bamboo, it was adorable!"
else:
    story += f"{favorite_animal} made a surpising appreance and that was quite unique and interesting!"

story += f"\nWhat a wild and {experience_adj} experience."

# print the final story
print(story)


# End of the mad libs story