# Author: GinWook Lee
# GitHub username: git-ginwook
# Date: 3/9/2022
# Description:
#   This program runs ShipGame emulating the game Battleship.
#   There are two players playing against each other.
#   Each player has their own battlefield, 10x10 grid with rows: A~J and columns: 1~10.
#   Before the battle, each player prepare for the battle by building their battleships.
#   Placement of each battleship is kept hidden.
#   Once two battlefields are set, the first player fires the first torpedo.
#   Each player takes turn firing at each other until one player's battleships are all destroyed.

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
        # 10x10 battle board {key:value}
        self._board = {"Row": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
                       "Col": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]}

        # initialize battleship list
        self._battleships = {"first": [], "second": []}
        self._num_ships = {"first": 0, "second": 0}

        # initialize game setup
        self._current_state = "UNFINISHED"
        self._current_turn = "first"

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
        self._num_ships[player_str] = len(self._battleships[player_str])
        return True

    def get_current_state(self):
        """
        fetch and return current_state
        """
        return self._current_state

    def set_current_state(self, player_str):
        """
        this function is called only if there is a winner (and a loser).

        Two output options: 1) 'FIRST_WON' or 2) 'SECOND_WON'.
        The passed parameter, player_str, indicates the loser.
        """
        # player_str is the loser, so the other player is the winner
        if player_str == "first":
            self._current_state = "SECOND_WON"
        else:
            self._current_state = "FIRST_WON"

    def get_current_turn(self):
        """
        fetch and return current_turn
        """
        return self._current_turn

    def set_current_turn(self, player_str):
        """
        switch current_turn to the other player after each valid fire_torpedo()
        """
        if player_str == "first":
            self._current_turn = "second"

        else:
            self._current_turn = "first"

    def fire_torpedo(self, player_str, coord_str):
        """
        attack the specified coordinate on the opponent's grid.

        Before firing a torpedo, two checks need to be in place:
        1) check whether the current_state is 'UNFINISHED'.
        2) check whether the current_turn matches with player_str.

        If either one of checks is FALSE, then nothing happens and return False.
        If 1 and 2 are both TRUE, check impact of the fire on the opponent's grid.
        1) 'out of grid'
        2) 'miss'
        3) 'hit'

        regardless of 'hit' or 'miss', switch current_turn.

        If it's 'out of grid', just return True (turn wasted).
        If it's a 'hit', update remaining ships and current state, then return True.
        If it's a 'miss', just return True.
        """
        # [validation]
        # if game is already won by a player, return False
        if self._current_state != "UNFINISHED":
            return False
        # if player_str is neither "first" nor "second", return False
        if player_str != "first" and player_str != "second":
            return False
        # if it's not player_str's turn, return False
        if self._current_turn != player_str:
            return False

        # [switch turn]
        self.set_current_turn(player_str)

        # [torpedo impact]
        # parse coord_str into row and col
        row = coord_str[0]
        col = coord_str[1:]

        # check whether the torpedo is out of grid
        if row not in self._board["Row"] or col not in self._board["Col"]:
            # wasted shot - no further check is needed
            return True

        # check for hit
        for ship in self._battleships[self._current_turn]:
            # if there is a hit, call set_num_ships_remaining()
            if coord_str in ship:
                ship_num = self._battleships[self._current_turn].index(ship)
                part_num = self._battleships[self._current_turn][ship_num].index(coord_str)
                self.set_num_ships_remaining(self._current_turn, ship_num, part_num)

        # return True for both 'hit' and 'miss'
        return True

    def get_num_ships_remaining(self, player_str):
        """
        Return number of ships remaining for 'player_str'(either 'first' or 'second').
        """
        return self._num_ships[player_str]

    def set_num_ships_remaining(self, player_str, ship_num, part_num):
        """
        update number of ships remaining if there is a torpedo 'hit'.

        Function is called only if fire_torpedo() returns a 'hit'.

        Ship coordinates of the player under attack are revised - delete the hit part.
        Then, check other part(s) of the ship that has been striken.

        If there is at least one part of the ship not 'hit', then return nothing.
        If all parts of the ship have been 'hit', then deduct the number of ships remaining.

        If the number of remaining ships is not zero, then return nothing.
        If the number is zero, call set_current_state() to end the game with a winner.
        """
        # identify the player_str's hit ship
        hit_ship = self._battleships[player_str][ship_num]

        # delete part of hit ship from battleships list
        del hit_ship[part_num]

        # if the hit ship has just sunk, remove the ship
        if len(hit_ship) == 0:
            del self._battleships[player_str][ship_num]
            # update number of ships
            self._num_ships[player_str] = len(self._battleships[player_str])

            # if self._num_ships of player_str == 0:
            if self._num_ships[player_str] == 0:
                # self.set_current_state(player_str) <- loser
                self.set_current_state(player_str)

        # Otherwise, no change to num_ships_remaining


def main():
    """ test cases that run only within this ShipGame.py module """
    # create ShipGame object
    sg = ShipGame()

    sg.place_ship('first', 5, 'B2', 'C')
    sg.place_ship('first', 2, 'I8', 'R')
    sg.place_ship('first', 8, 'H2', 'R')

    sg.place_ship('second', 3, 'H2', 'C')
    sg.place_ship('second', 2, 'A1', 'C')

    # play ShipGame
    sg.fire_torpedo('second', 'A10')            # False
    sg.fire_torpedo('first', 'D2')              # miss
    sg.fire_torpedo('first', 'A2')              # False
    sg.fire_torpedo('second', 'I9')             # hit
    sg.fire_torpedo('first', 'X10')             # out and wasted
    sg.fire_torpedo('second', 'G15')            # out and wasted
    sg.fire_torpedo('first', 'B1')              # hit
    sg.fire_torpedo('second', 'I8')             # hit and sink 2:2
    sg.fire_torpedo('first', 'A1')              # hit and sink 2:1
    print(sg.get_current_turn())
    print(sg.get_current_state())
    sg.fire_torpedo('second', 'I8')             # repeat and wasted
    sg.fire_torpedo('first', 'H2')              # hit
    sg.fire_torpedo('second', 'B7')             # miss
    sg.fire_torpedo('first', 'I2')              # hit
    sg.fire_torpedo('second', 'H4')             # hit
    print(sg.get_current_turn())
    sg.fire_torpedo('first', 'J2')              # hit and sink 2:0
    print(sg.get_current_state())
    sg.fire_torpedo('second', 'E2')             # game over, FIRST_WON


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
