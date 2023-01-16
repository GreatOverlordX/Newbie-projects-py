# Kaleidoscope episode-bot-picker

# This is a fun project I decided to make for the Kaleidoscope serie on Netflix. Since you can watch the show in any order you please, I decided to create a sort of bot to pick for me everytime I would run it.  

import random

kalbot = ['Blue', 'Yellow', 'Green', 'Red', 'Orange', 'Violet', 'Pink', 'White'] #Black is not listed since it is the series' introductory episode
kcope = random.sample(kalbot, 1)[0] # Randomize the array of colours
print(kcope) # Pick it, Watch it!