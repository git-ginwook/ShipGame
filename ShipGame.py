# Author: GinWook Lee
# GitHub username: git-ginwook
# Date: 3/2/2022
# Description:

# Game objective:
#   Two players take turn firing torpedo to sink all of the opponent's battleships.

# assumptions:
#   1) a positive integer will always be passed as the length of a ship.
#   2) player 'first' always fires the first torpedo.
#   3) there is no limit to the number of battleships each player starts with.
#   4) place_ship() method gets called before any other methods are called.
#   5) once the first fire_torpedo() gets called, place_ship() won't be called.

#  restrictions:
#   1) unittest and typing are the only approved modules.
#   2) each battleship should be at least 2 in its length.
#   3) battleships cannot overlap.
#   4) battleships cannot take any partial place beyond the grid.
#   5) battleships cannot be placed diagonally.
#   6) fire_torpedo() method doesn't return result, whether it's a hit or miss.
#   7) fire_torpedo() outside of the grid is a wasted turn.

class ShipGame:
    """
    A class to represent ShipGame.
    - First part: two players set battleship(s) inside the their own 10x10 grid.
    - Second part: two players alternate firing torpedo at each other.

    ShipGame class updates each move and announce the winner
    once one of players has no more ships left in their grid.
    """
    def __init__(self):
        """
        init method takes no parameter. All data members are private.
        Initialize for each player: (* means either 'first' or 'second')
        - board: a clean grid
        - ships_coord_*: battleship records
        - ships_remaining_*: number of live battleships
        Set default values:
        - grid_range = 10x10 (rows: A~J x column: 1~10)
        - current_turn = 'first'
        - current_state = 'UNFINISHED'
        """
        self._board = {
            "R": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
            "C": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        }
        # initialize battleship list
        self._board_first = []
        self._board_second = []

    def place_ship(self, player_str, ship_length, coord_str, orient_str):
        """
        add a ship with 'ship_length' for 'player_str' at 'coord_str' in 'orient_str'

        First, each passed parameter needs to be validated:
        - player_str: must be either 'first' or 'second'
        - ship_length: 2 <= length <= 10
        - orient_str: must be either 'R' or 'C'
        - coord_str: no part of the ship falls outside of the grid
        If any of these conditions are not met, then return FALSE.

        If all of these conditions are met, then build a battleship by:
        1) identify whose battleship it is based on 'player_str'
        2) set the head of the ship based on 'coord_str'
        3) check orientation of the ship based on 'orient_str' ('R'=right, 'C'=column)
        4) append remaining part(s) starting from 'coord_str' in 'orient_str' direction
        5) label all of covered coordinates as one battleship

        Then, return True after:
        incrementing the remaining number of ships ('ships_remaining_*') for 'player_str'
        and appending the new battleship to 'ships_coord_*' for 'player_str'.
        """
        # check ship_length
        if ship_length < 2:
            return False

        # parse coord_str into index[0] and index[1:]
        row = coord_str[0]
        col = coord_str[1:]

        # check whether the head of battleship (coord_str) is out of the board
        if row not in self._board["R"]:
            return False

        if col not in self._board["C"]:
            return False




        # tail:
        # if index position of index[0] in "R_li" plus ship_length > 9:
        # return False (out of grid)
        # else:
        # move on to the next line

        return True

        # [head and tail test] - column
        # head:
        # if index[0] is not in "C_li" of board:
        # return False (out of grid)

            # else: (if index[0] is in "C_li" of board)
            # move on to the next line

            # tail:
            # if index position of index[0] in "C_li" plus ship_length > 9:
            # return False (out of grid)
            # else:
            # move on to the next line



        # [overlap test]
        # generate a temp_ship list from head to tail
        # use ship_length as a count for a while loop
        # for part in temp_ship:
        # if part in ships_coord_*:
        # return False (overlap)

        # append temp_ship as a new battleship

        # use len to count remaining battleships



    def get_current_state(self):
        """
        fetch and return the current_state value
        """
        pass

    def set_current_state(self):
        """
        function as a gatekeeper whether to continue the game.

        Three return options: 1) 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'.
        Return options are based on get_num_ships_remaining() method.

        If all battleships got destroyed for either one of 'first' or 'second' player,
        then a winner is declared and ShipGame stops, ('FIRST_WON' or 'SECOND_WON').

        If neither has zero ships remaining, then the game proceeds as 'UNFINISHED'.
        """
        pass

    def get_current_turn(self):
        """
        fetch and return current_turn value
        """
        pass

    def set_current_turn(self):
        """
        switch current_turn to the other player after each fire_torpedo() gets called
        """
        pass

    def fire_torpedo(self, player_str, coord_str):
        """
        attack the specified coordinate on the opponent's grid.

        Before firing a torpedo, two checks need to be in place:
        1) check whether the current_turn matches with player_str.
        2) check whether the current_state is 'UNFINISHED'.

        If 1 or 2, or both is FALSE, then nothing happens.
        If 1 and 2 are both TRUE, check the attached coordinate on the opponent's grid.
        1) 'miss'
        2) 'hit'

        If it's a 'miss', just switch current_turn.
        If it's a 'hit', switch turn, check remaining ships, and update current state.
        """
        pass

    def get_num_ships_remaining(self, player_str):
        """
        Return number of ships remaining for 'player_str'(either 'first' or 'second').
        """
        # use len to count remaining battleships
        if player_str == "first":
            self._ships_remaining_first = len(self._board_first)
            return self._ships_remaining_first
        if player_str == "second":
            self._ships_remaining_second = len(self._board_second)
            return self._ships_remaining_second

    def set_num_ships_remaining(self, player_str, coord_str):
        """
        update number of ships remaining after reflecting the torpedo 'hit'.

        Function is called only if fire_torpedo() returns a 'hit'.

        The attacked player's ship coordinates are updated with the struck coordinate.
        Then, check other portion(s) of the struck ship.

        If there is at least one portion of the ship not 'hit', then return nothing.
        If all portions have been 'hit', then deduct the number of ships remaining.

        If the number of remaining ships is not zero, then return nothing.
        If the number is zero, call set_current_state() to end the game with a winner.
        """
        pass


def main():
    """ test cases that run only within this ShipGame.py module """
    # create ShipGame object
    sg = ShipGame()

    # check initial setting
    print("initial battleship(first): ", sg.get_num_ships_remaining("first"))
    print("initial battleship(second): ", sg.get_num_ships_remaining("second"))

    # [place_ship() tests]
    # ship_length test
    print("length less than 2: ", sg.place_ship("first", 1, "X1", "R"))
    # head test
    print("index[0] not in 'R': ", sg.place_ship("first", 2, "a1", "R"))            # False
    print("index[0] not in 'R': ", sg.place_ship("first", 2, "X1", "R"))            # False
    print("index[1:] not in 'C': ", sg.place_ship("first", 2, "A0", "C"))           # False
    print("index[1:] not in 'C': ", sg.place_ship("first", 2, "A11", "C"))          # False

    print("coord_str in: ", sg.place_ship("first", 2, "A1", "R"))                   # True
    print("coord_str in: ", sg.place_ship("first", 2, "A10", "R"))                  # True
    print("coord_str in: ", sg.place_ship("first", 2, "J1", "R"))                   # True
    print("coord_str in: ", sg.place_ship("first", 2, "J10", "R"))                  # True


    print("index[1:] in 'C': ", sg.place_ship("first", 2, "A10", "C"))

    # tail test


    # sg.place_ship("second", 1, "A1", "C")
    # sg.place_ship("first", 2, "B1", "R")
    # sg.place_ship("second", 2, "A2", "C")





if __name__ == '__main__':
    main()


# Scenario descriptions
# “DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS”
# 1. Determining how to store the boards
#   - each player's board starts with an empty list.
#   - When place_ship() gets called right, new battleship gets appended as a nested list.

# 2. Initializing the boards
#   - once each player completes place_ship() method,
#     two players get board lists with battleship coordinates inside as nested lists.

# 3. Determining how to track which player's turn it is to play right now
#   - each fire_torpedo() method updates the turn through set_current_turn() method.

# 4. Determining how to validate piece placement
#   - 'hit' or 'miss' is determined through a search method.
#   - taking 'coord_str' from fire_torpedo(), search through the opponent's board list.
#   - if there is no match, it's a 'miss'.
#   - if there is a match, it's a 'hit'. Delete the matching element from the list.

# 5. Determining when ships have been sunk
#   - each time there is a 'hit', count the number of elements in that nested list.
#   - if the 'hit' nested list counts zero element, that ship has been sunk.
#   - delete that nested list from the board list.
#   - change the remaining ships by counting the number of elements in the board list.

# 6. Determining when the game has ended
#   - after each 'hit' and update on the nested list and, if any, change to board list,
#     if the count of elements in the board list is zero, the game has ended.
#     At that point, set_current_state() should be triggered and change to '*_WON'.
