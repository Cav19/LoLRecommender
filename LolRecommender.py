__author__ = 'Connor Valenti'

# This file contains the methods necessary for my League of Legends Champion Recommender software.
# Work in Progress

import csv


ROLES = ['Fighter', 'Tank', 'Mage', 'Juggernaut', 'Assassin', 'Marksman', 'Support']
CHAMPION_ROLES = {}

def read_file():
    tsv_file = open("ratings.tsv")
    champions = csv.reader(tsv_file, delimiter = '\t')
    while(True):
        champion = next(champions)
        name = champion[0]
        role = champion[1]
        damage_type = int(champion[2])
        skillshot = int(champion[3])
        range = int(champion[4])
        tankiness = int(champion[5])
        crowd_control = int(champion[6])
        mobility = int(champion[7])
        auto_attack = int(champion[8])
        damage = int(champion[9])
        wave_clear = int(champion[10])
        mechanics = int(champion[11])
        stacks = int(champion[12])
        invisibility = int(champion[13])
        global_spells = int(champion[14])
        yield(name, role, damage_type, skillshot, range, tankiness, crowd_control, mobility, auto_attack, damage, wave_clear, mechanics, stacks, invisibility, global_spells)


def get_scores():
    champion_scores = []
    for champion in read_file():
        CHAMPION_ROLES[champion[0]] = champion[1]
        champion_scores.append((champion[0], champion[2], champion[3], champion[4], champion[5], champion[6], champion[7], champion[8], champion[9], champion[10], champion[11], champion[12], champion[13], champion[14]))
    return champion_scores


def compare_champs():
    compared_scores = {}
    champ_scores = get_scores()
    for champion in champ_scores:
        compared_scores[champion[0]] = []
        for champion2 in champ_scores:
            if not champion[0] == champion2[0]:
                difference = 0
                for i in range(1, len(champion)):
                    difference += abs(champion[i] - champion2[i])
                compared_scores[champion[0]].append((difference, champion2[0]))
    return compared_scores


def get_matches(champion):
    all_scores = compare_champs()
    champ_scores = all_scores[champion]
    champ_scores.sort()
    matches = []
    for i in range(125):
        matches.append(champ_scores[i])
    return matches


def get_all_matches():
    all_scores = compare_champs()
    all_matches = []
    for score in all_scores:
        champ_scores = all_scores[score]
        champ_scores.sort()
        matches = []
        for i in range(5):
            matches.append(champ_scores[i])
        all_matches.append((score, matches))
        print score, matches
    return all_matches


def suggest_champ_by_role(champion):
    champion_matches = get_matches(champion)
    suggestions = []
    for role in ROLES:
        for match in champion_matches:
            if role == CHAMPION_ROLES[match[1]]:
                suggestions.append(match[1])
                break
    print suggestions
    return suggestions


suggest_champ_by_role('Shaco')