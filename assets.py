"""
Asset creation module
"""

import random
import itertools


def make_description() -> str:
    """
    Generate description randomly.

    This function generates a random description randomly from a tuple of descriptions.

    :postcondition: generate random integer to index through a tuple and obtain a room description
    :return: a random string from the collection of strings
    """

    room_descriptions = ("The dusty scrolls of the stacks howled with an eerie silence",
                         "It seems a family of jumping spiders are practicing parkour",
                         "The cozy room is filled with the warm glow of flickering candles, casting dancing shadows "
                         "across the endless shelves of books and tomes.",
                         "Quaint armchairs sit nestled amongst stacks of dusty books, inviting visitors to lose "
                         "themselves in their pages and the tales they contain.",
                         "The room is filled with the rich scent of old leather bindings and musty pages, mingling"
                         " with the faint aroma of brewing coffee and the sweet scent of sugary treats.",
                         "The air is thick with the scent of ancient ink and quills, as scholars pour over "
                         "yellowed manuscripts and forgotten tomes in search of hidden knowledge.",
                         "A winding staircase leads up to an old wooden loft, where ancient tomes and forgotten "
                         "scrolls wait patiently to be discovered.",
                         "Small creatures scurry amongst the stacks of tomes and scrolls, seeking out forgotten "
                         "knowledge hidden within the pages.",
                         "The warmth of the fireplace casts flickering shadows across the room, revealing the "
                         "presence of ancient artifacts and magical objects that have been hidden away for centuries.",
                         "The scent of old parchment fills the air, as endless shelves of books tower high around you, "
                         "inviting you to lose yourself in the secrets of arcane lore.",
                         "Quaint tapestries adorn the walls, depicting ancient legends and mystical beasts, "
                         "each with a tale to be told.",
                         "A large oak table, adorned with mystical runes and symbols, stands in the center of the room,"
                         " holding an open grimoire, beckoning those who would dare to study its pages.",
                         "The sound of turning pages and scratching quills fills the air, as ancient wisdom is "
                         "transcribed by scholars and sages in leather-bound tomes.",
                         "The room is filled with the faint glow of lamplight, illuminating the pages of ancient "
                         "grimoires and the secrets they contain.",
                         "The warmth of the fireplace casts flickering shadows across the room, revealing the presence "
                         "of ancient artifacts and magical objects that have been hidden away for centuries.",
                         "The scent of brewing tea and warm cookies mingles with the smell of old books, creating a "
                         "cozy atmosphere that beckons visitors to stay awhile to indulge in the pleasures of reading.",
                         "The soft rustling of pages can be heard as tomes open and close on their own, "
                         "revealing their secrets to those who possess the gift of magic.",
                         "A curious collection of objects is scattered throughout the room, from ancient artifacts to "
                         "curious trinkets, each with its own story to tell.",
                         "An old grandfather clock ticks softly in the corner, marking the passage of time as visitors "
                         "lose themselves in the pages of magical tomes and epic sagas.",
                         "The room is alive with the sound of rustling pages, as curious ants scurry across the pages "
                         "of dusty tomes, seeking out scraps of knowledge to take back to their colony.",
                         "Old books sit nestled amongst the clutter of everyday objects, with quills and inkpots,"
                         " bookmarks, and paperweights scattered haphazardly across the tables and chairs.",
                         "The room is filled with the soft patter of spider feet, as they spin their webs amongst the"
                         " dusty stacks of tomes and scrolls, creating intricate patterns that hint at hidden magic.",
                         "A thick layer of dust coats the forgotten corners of the room, gathering around the legs of "
                         "forgotten chairs and tables, and providing a haven for small creatures seeking shelter.",
                         "Amongst the stacks of tomes, curious beetles crawl across pages filled with arcane symbols "
                         "and mysterious runes, seeking out secrets hidden deep within their depths.")
    return room_descriptions[random.randint(0, len(room_descriptions) - 1)]


def make_enemy() -> str:
    """
    Make enemy description.

    This function generate random description for enemies from a selection of descriptions.

    :precondition: must have a tuple of descriptions
    :postcondition: generate random integer to index through a tuple and obtain an enemy description
    :return: a random string from the collection of strings
    """
    enemy_descriptions = ("Look out, it's a warrior ant with ill intentions!",
                          "The Snail of Orwell demands a duel!",
                          "An Orb Weaver has blocked the path with its sticky web.",
                          "The mini ant colony under the red table wants to steal your food!",
                          "A drunk flying moth is about to crash into us!",
                          "Careful now, we're being stalked by a praying mantis...sshhhh",
                          "That bundle of freshly sharpened pencils seems lethal, watch your head.",
                          "Watch your step these books seem wobbly",
                          "Bob's cat, Lucius, is waking up. We must hurry!",
                          "Watch out for that cat paw, it wants to squish us!",
                          "Another bookworm is eating through the origami bridge, hurry across!",
                          "We have trek around the puddle of ink. Can you think of anything?",
                          "Madam Lorene the Lady Bug wants you to play game with her.",
                          "Aunty Gemma wants us to come in for tea but only if you answer out her question",
                          "This shady looking ant wants to sell you grass. Ignore him!",
                          "Hold on that desk fan's gonna blow us awwaaaaaaaaaaaaaaaayyy",
                          "Seems like Karen left her rusty paper clips on the plains again, "
                          "must challenge the warrior ants to go through the other route",
                          "This chair's underside is riddled with gum, but we must persevere!")
    return enemy_descriptions[random.randint(0, len(enemy_descriptions) - 1)]


def make_board(rows: int, columns: int) -> dict:
    """
    Create the game space.

    :param rows: integer 10
    :param columns: integer 10
    :precondition rows: must be an integer = 10
    :precondition columns: must be an integer = 10
    :postcondition: creates a dictionary that defines the map of the game
    :raise ValueError: raises ValueError if either row or column input is not integer = 10
    :return: dictionary of the map for the game

    """
    if rows != 10 or columns != 10:
        raise ValueError("Rows and columns must both be 10")
    else:
        game_board_coords = {number for number in itertools.product(list(range(rows)), repeat=2)}
        game_board = {}
        for item in game_board_coords:
            game_board[item] = make_description()
        return game_board


def make_character() -> dict:
    """
    Create character attributes.

    :precondition: values for X-coordinate, Y-coordinate and Current HP must be integers
    :postcondition: creates dictionary with character attributes
    :return: dictionary with character attributes
    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 50, 'Current XP': 0, 'Knowledge': 'Novice'}
    """
    player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "Knowledge": "Novice"}
    return player


def main():
    """
    Drive the program
    """


if __name__ == "__main__":
    main()
