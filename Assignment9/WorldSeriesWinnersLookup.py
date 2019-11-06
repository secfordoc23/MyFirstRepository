"""
    Program: World Series Winners Lookup
    File: WorldSeriesWinnersLookup.py
    Author: Jason J Welch
    Date: 10/28/2019
    Purpose: A program to lookup how many times a team has won the World Series from 1903 to 2009, with data imported
        from a text file.
    
"""
from InputValidation import *

# ================== main ==================
def main():
    fileName = "WorldSeriesWinners.txt"

    while True:
        print("***************************************************************")
        print("\tWorld Series Winners Lookup")
        print("***************************************************************")
        userSelection = display_menu(["Find how many times a Team has won from 1902 to 2009", "Exit"])
        if userSelection == 1:
            teamName = input("Enter a team name to lookup: ")
            winnerList = load_list_from_file(fileName)
            find_team_in_list(teamName, winnerList)
        else:
            break

# END main


# ================== find_team_in_list ==================
def find_team_in_list(teamName, winnerList):
    counter = 0
    for team in winnerList:
        if teamName.lower() == team.lower():
            counter += 1
    if counter > 0:
        message = f"\nThe {teamName} have won {counter} World Series.\n"
    else:
        message = f"\nThe {teamName} have not won a World Series.\n"
    print(message)
# END find_team_in_list


main()
# *************************** NO CODE FOLLOWS ***************************
