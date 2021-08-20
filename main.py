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

# rankings of women preferred by each man
women_rankings = {
    'ryan': ['lizzy', 'sarah', 'zoey', 'daniella'],
    'josh': ['sarah', 'lizzy', 'daniella', 'zoey'],
    'blake': ['sarah', 'daniella', 'zoey', 'lizzy'],
    'connor': ['lizzy', 'sarah', 'zoey', 'daniella']
}

# rankings of men preferred by each woman
men_rankings = {
    'lizzy': ['ryan', 'blake', 'josh', 'connor'],
    'sarah': ['ryan', 'blake', 'connor', 'josh'],
    'zoey': ['connor', 'josh', 'ryan', 'blake'],
    'daniella': ['ryan', 'josh', 'connor', 'blake']
}

# keep track of matches that have been temporarily set up
tentative_matches = []

# men that need to still be matched successfully
available_men = []


def available_men_setup():
    for man, women in women_rankings.items():
        available_men.append(man)


def start_matching(man):
    print("Currently checking for : ", man)
    for woman in women_rankings[man]:
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
            matched_man_index = men_rankings[woman].index(matched_man)
            potential_man_index = men_rankings[woman].index(man)

            if matched_man_index > potential_man_index:
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
    print("The matching has been succesfully completed")


def main():
    available_men_setup()
    print("The available men currently are ", available_men)
    stable_matching()
    print("The matches are: ")
    print(tentative_matches)


main()
