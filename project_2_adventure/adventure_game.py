import random
import time
from typing import Set

has_sword = False
MONSTERS = ["dragon", "gorgon", "wicked fairie"]
monster = None
HOUSE = "house"
FIELD = "field"
CAVE = "cave"
END_GAME = "end"


def field_with_house_and_cave() -> str:
    print_and_pause("")
    print_and_pause("Enter 1 to knock on the door of the house.")
    print_and_pause("Enter 2 to peer into the cave.")
    response = get_valid_input(
        "What would you like to do?", "1 or 2", {'1', '2'}
    )
    return HOUSE if response == "1" else CAVE


def print_victory_text() -> None:
    global monster
    if has_sword:
        print_and_pause(
            f"As the {monster} moves to attack, "
            f"you unsheath your new sword."
        )
        print_and_pause(
            "The Sword of Ogoroth shines brightly in your "
            "hand as you brace yourself for the attack."
        )
        print_and_pause(
            f"But the {monster} takes one look at "
            f"your shiny new toy and runs away!"
        )
    else:
        print_and_pause(
            f"The {monster} takes one look at your "
            f"dagger and starts laughing hysterically."
        )
        print_and_pause(
            f"So hysterically, in fact, "
            f"that the {monster}'s poor heart can't take it."
        )
        print_and_pause(f"The {monster} drops dead.")
    print_and_pause(
        f"You have rid the town of the {monster}. You are victorious!"
    )


def fight_monster() -> None:
    global monster
    if has_sword:
        is_victorious = random.randint(1, 10) > 1
    else:
        is_victorious = random.randint(1, 10) > 9

    if is_victorious:
        print_victory_text(monster)
    else:
        print_and_pause("That did not go well...")
        print_and_pause("You have been defeated!")


def horror_house() -> str:
    global monster
    print_and_pause("You approach the door of the house.")
    print_and_pause(
        f"You are about to knock when the door "
        f"opens and out steps a {monster}."
    )
    print_and_pause(f"Eep! This is the {monster}'s hoouse!")
    print_and_pause(f"The {monster} attacks you!")
    if not has_sword:
        print_and_pause(
            "You feel a bit under-prepared for this, "
            "what with only having a tiny dagger."
        )

    response = get_valid_input(
        "What would you like to do?",
        "(1) to fight or (2) to run away.",
        {'1', '2'}
    )
    action = "fight" if response == "1" else "run"
    if action == "fight":
        fight_monster(monster)
        return END_GAME
    else:
        print_and_pause(
            f"You run back into the field. "
            f"Luckily, you don't seem to have been followed."
        )
        return FIELD


def cave_with_sword() -> str:
    global has_sword
    print_and_pause("You peer cautiously into the cave.")
    if not has_sword:
        print_and_pause("It turns out to be only a very small cave.")
        print_and_pause("Your eye catches a glint of metal behind a rock.")
        print_and_pause("You have found the magical Sword of Ogoroth!")
        print_and_pause(
            "You discard your silly old dagger and take the sword with you."
        )
        has_sword = True
    else:
        print_and_pause(
            "You've been here before, and gotten all the good stuff. "
            "It's just an empty cave now."
        )
    print_and_pause("You walk back out to the field.")
    return FIELD


def print_and_pause(message: str) -> None:
    print(message)
    time.sleep(1)


def intro() -> None:
    print_and_pause(
        "You find yourself standing in an open field, "
        "filled with grass and yellow wildflowers."
    )
    print_and_pause(
        "Rumor has it that a dragon is somewhere around here, "
        "and has been terrifying the nearby village."
    )
    print_and_pause("In front of you is a house.")
    print_and_pause("To your right is a dark cave.")
    print_and_pause(
        "In your hand you hold your trusty (but not very effective) dagger."
    )


def get_valid_input(
        intro_message: str,
        options_str: str,
        valid_inputs: Set[str]
) -> str:
    print_and_pause(intro_message)
    entire_options_request_str = f"(Please enter {options_str}.)\n"
    response = input(entire_options_request_str)
    while response not in valid_inputs:
        response = input(entire_options_request_str)

    return response


def ask_if_play_again() -> bool:
    play_again = get_valid_input(
        "Would you like to play again?",
        "'y' for yes or 'n' for no",
        {"y", "n"}
    )
    if play_again == 'y':
        print_and_pause("Excellent! Restarting the game ...")
        return True
    else:
        print_and_pause("Good bye....")
        return False


FUN_DICT = {
    FIELD: field_with_house_and_cave,
    HOUSE: horror_house,
    CAVE: cave_with_sword
}


def play_round() -> None:
    global monster
    monster = random.choice(MONSTERS)
    intro()
    response = field_with_house_and_cave()
    while response != "end":
        response = FUN_DICT[response]()


def play_game() -> None:
    global has_sword
    play_again = True
    while play_again:
        has_sword = False
        play_round()
        play_again = ask_if_play_again()


play_game()
