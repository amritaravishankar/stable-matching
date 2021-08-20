# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
"""
    @Author: Amrita Ravishankar
    @Publication-Date: 20/8/21
    @Description:
    The stable matching algorithm seeks to solve the problem of finding a stable match between two sets of equal size
    given a list of preferences for each element.
    We can define "matching" and "stable" by the following definitions.
    Matching: Mapping from the elements of one set to the elements of another set
    Stable: No element A of the first set that prefers an element B of the second set over its current partner
            such that element B prefers element A over its current partner.


    NOTE: I learnt the algorithm with the men and women being considered as two different sets for matching. For simplicity of implementation,
    I have continued with the same.
    However, I support diversity of all kinds <3
"""

import collections


def print_description():
    print('''
    GALE-SHAPLEY ALGORITHM - STABLE MATCHING PROBLEM
    
    The stable matching algorithm seeks to solve the problem of finding a stable match 
    between two sets of equal size given a list of preferences for each element. 
    
    We can define "matching" and "stable" by the following definitions.
    Matching: Mapping from the elements of one set to the elements of another set
    Stable: No element A of the first set that prefers an element B of the second set over 
    its current partner such that element B prefers element A over its current partner.'''
    )
    print()



# keep track of matches that have been temporarily set up
tentative_matches = []

# men that need to still be matched successfully
available_men = []

men_preferences = collections.defaultdict(list)     # rankings of women preferred by each man
women_preferences = collections.defaultdict(list)   # rankings of men preferred by each woman


def take_user_input():
    n = int(input("Please input the desired number of members in each set: "))
    print()
    men = input(f"Please enter names of {n} men, separated by commas and no spaces eg. Mac,John: ")
    names_of_men = men.split(",")
    if len(names_of_men) != n:
        print("Exiting since number of men differ from initial input")
        exit()

    women = input(f"Please enter names of  {n} women, separated by commas and no spaces eg. Olivia,Tina: ")
    names_of_women = women.split(",")
    if len(names_of_women) != n:
        print("Exiting since number of women differ from initial input")
        exit()

    print()
    print("For each man, insert his ranking preference of the above women, separated by commas.")
    for man in names_of_men:
        print("Man: ", man)
        preferences = input("Preference ranking: ")
        men_preferences[man] = preferences.split(",")
        print()

    print()
    print("Great! We're done with men's preferences")
    print()

    print("For each woman, insert her ranking preference of the above men, separated by commas.")
    for woman in names_of_women:
        print("Woman: ", woman)
        preferences = input("Preference ranking: ")
        women_preferences[woman] = preferences.split(",")
        print()
    print()


def available_men_setup():
    for man, women in men_preferences.items():
        available_men.append(man)


def start_matching(man):
    print("Currently checking for : ", man)
    for woman in men_preferences[man]:
        existing_match = [match for match in tentative_matches if woman in match]

        # if the woman is not a part of any match yet - she is single
        if len(existing_match) == 0:
            # can be set up with the man
            tentative_matches.append([man, woman])
            available_men.remove(man)
            print(man, " is no longer available to be set up and is tentatively matched with ", woman)
            break

        # woman has a match - she is not single
        elif len(existing_match) > 0:
            matched_man = existing_match[0][0]
            print(woman, " is already matched with ", matched_man)

            # check rankings of matched man vs potential man
            matched_man_index = women_preferences[woman].index(matched_man)
            potential_man_index = women_preferences[woman].index(man)

            if matched_man_index < potential_man_index:
                print(woman, " is already happy with her match - ", matched_man, ", no rematching will take place...")

            else:
                print(woman, " would be happier with ", man, ", rematching will take place...")
                print(matched_man, " is available again...")

                available_men.append(matched_man)
                available_men.remove(man)

                # update the match
                existing_match[0][0] = man
                break


# perform the matching algorithm until all men have been successully matched up
def stable_matching():
    while len(available_men) > 0:
        for man in available_men:
            start_matching(man)
    print("The matching has been successfully completed!")


def main():
    print_description()
    take_user_input()
    available_men_setup()
    print("The available men currently are ", available_men)
    print()
    print("Calculation Logs")
    stable_matching()
    print()
    print("The matches are: ")
    print(tentative_matches)


main()
