# OCR-GCSE-Programming-Project-Task-1-for-practise-
https://www.ocr.org.uk/Images/503195-programming-project-tasks-june-2019-and-june-2020.pdf

##Task

Noel is creating a music quiz game.

The game stores a list of song names and their artist
(e.g. the band or solo artist name). The player needs to
try and guess the song name.

The game is played as follows:

•   A random song name and artist are chosen.
•   The artist and the first letter of each word in the song title are displayed.
•   The user has two chances to guess the name of the song.
•   If the user guesses the answer correctly the first time, they score 3 points. If the user guesses
the answer correctly the second time they score 1 point. The game repeats.
•   The game ends when a player guesses the song name incorrectly the second time.

Only authorised players are allowed to play the game.
Where appropriate, input from the user should be validated.

Design, develop, test and evaluate a system (using python) that:

1. Allows a player to enter their details, which are then authenticated to ensure that they are an
authorised player.
2. Stores a list of song names and artists in an external file.
3. Selects a song from the file, displaying the artist and the first letter of each word of the song title.
4. Allows the user up to two chances to guess the name of the song, stopping the game if they guess
a song incorrectly on the second chance.
5. If the guess is correct, add the points to the player’s score depending on the number of guesses.
6. Displays the number of points the player has when the game ends.
7. Stores the name of the player and their score in an external file.
8. Displays the score and player name of the top 5 winning scores from the external file.

##Comments about code

Sections of code are splitted with double closers:

===============================================================================
===============================================================================

Sections within sections are splitted with one closer:

===============================================================================

This is in order to make reading the code easier and make the sections of sections of code easier to find, modify, read, and understand

One of the things I did with the code is that instead of putting "else:" statements where I could I only put them where they where necessary making "elif:" statements instead to make the code easier to read.
