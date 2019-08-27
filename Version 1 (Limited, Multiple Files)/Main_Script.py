from Authenticate_User import get_usernames_and_passwords, authenticate_user
from Music_Game import get_artists_and_songs, start_music_game


# ======================================================================================================================
# ======================================================================================================================

def main_menu():
    print("Main Menu\n\n")

    print("Play\n\nSign Out\n\nExit\n\n")

    picked_option = input()

    print("\n\n")

    if picked_option.lower().strip().replace(" ", "") == "play":
        start_music_game()

        main_menu()  # Returns to main menu

    elif picked_option.lower().strip().replace(" ", "") == "signout":
        authenticate_user()  # Goes back to the sign in menu

        main_menu()  # Returns to main menu

    elif picked_option.lower().strip().replace(" ", "") == "exit":
        print("Goodbye!\n\n")

        quit()

    else:
        print("That is invalid. Check your spelling.\n\n")

        main_menu()


# ====================================================initialisation====================================================
# ======================================================================================================================

get_usernames_and_passwords()

get_artists_and_songs()


# ====================================================Program Starts====================================================
# ======================================================================================================================

authenticate_user()

main_menu()
