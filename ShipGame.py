# Author: GinWook Lee
# GitHub username: git-ginwook
# Date: 3/9/2022
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

        Initialize private data members:
        - board: a clean 10x10 grid (rows: A~J x column: 1~10)
        - battleships: battleship records
        - num_ships: number of live battleships
        - current_state: 'UNFINISHED'
        - current_turn: 'first'
        """
        # 10x10 battle board
        self._board = {"Row": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
                       "Col": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]}

        # initialize battleship list
        self._battleships = {"first": [], "second": []}
        self._num_ships = {"first": 0, "second": 0}


    def place_ship(self, player_str, ship_length, coord_str, orient_str):
        """
        add a ship with 'ship_length' for 'player_str' at 'coord_str' in 'orient_str'

        First, each passed parameter needs to be validated:
        - player_str: must be either 'first' or 'second'
        - orient_str: must be either 'R' or 'C'
        - ship_length: 2 <= length <= 10
        - coord_str: no part of the ship falls outside of the grid
        If any of these conditions are not met, then return FALSE.

        If all of these conditions are met, then build a battleship by:
        1) identify whose battleship it is based on 'player_str'
        2) set the head of the ship based on 'coord_str'
        3) check orientation of the ship based on 'orient_str' ('R'=right, 'C'=down)
        4) append remaining part(s) starting from 'coord_str' in 'orient_str' direction
        5) label all of covered coordinates as one battleship

        Then, return True after:
        incrementing the remaining number of ships ('num_ships') for 'player_str'
        and appending the new battleship to 'battleships' for 'player_str'.
        """
        # parameter validation
        if player_str != "first" and player_str != "second":
            return False
        if orient_str != "R" and orient_str != "C":
            return False
        if ship_length < 2 or ship_length > 10:
            return False

        # parse coord_str into row and col
        row = coord_str[0]
        col = coord_str[1:]

        # check whether the head of battleship is out of bound
        if row not in self._board["Row"] or col not in self._board["Col"]:
            return False

        # check whether the tail of battleship is out of bound
        if orient_str == "C" and self._board["Row"].index(row) + ship_length > 10:
            return False
        if orient_str == "R" and self._board["Col"].index(col) + ship_length > 10:
            return False

        # build new ship one part at a time
        temp_ship = []
        candidate = None

        for part in range(ship_length):
            if orient_str == "C":
                row_index = self._board["Row"].index(row) + part
                candidate = self._board["Row"][row_index] + col

            if orient_str == "R":
                col_index = self._board["Col"].index(col) + part
                candidate = row + self._board["Col"][col_index]

            # check for overlap
            for num in range(self._num_ships[player_str]):
                if candidate in self._battleships[player_str][num]:
                    return False

            # lining up ship parts into a new ship
            temp_ship.append(candidate)

        # append new ship to battleship list
        self._battleships[player_str].append(temp_ship)
        # update number of ships
        self._num_ships[player_str] = self.get_num_ships_remaining(player_str)
        return True

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
        return len(self._battleships[player_str])

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


def main():
    """ test cases that run only within this ShipGame.py module """
    # create ShipGame object
    sg = ShipGame()


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
