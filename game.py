from copy import deepcopy
from typing import Tuple, List
BottlesArray = List[List[str]]

from typing import List, Tuple
from copy import deepcopy
import json

# Constant for empty bottle
EMPTY = "EMPTY"

# Type alias for bottles array
BottlesArray = List[List[str]]

# Class for Game
class Game:
    def __init__(self, bottles: BottlesArray):
        self.bottles = bottles

    def solve(self) -> 'Flow':
        queue_state = [Flow(bottles=self.bottles)]
        visited = {}
        solved_state = None

        while queue_state:
            current_state = queue_state.pop()
            if visited.get(hash_bottles(current_state.bottles)):
                continue
            visited[hash_bottles(current_state.bottles)] = True
            if is_done(current_state.bottles):
                solved_state = current_state
                break

            for i in range(len(current_state.bottles)):
                bottle1 = current_state.bottles[i]
                if is_bottle_done(bottle1) or bottle1[0] == EMPTY:
                    continue

                for j in range(len(current_state.bottles)):
                    if i == j or current_state.bottles[j][-1] != EMPTY:
                        continue

                    bottle2 = current_state.bottles[j]
                    if is_move_possible(bottle1, bottle2):
                        cs = get_copy_of_situation(current_state.bottles)
                        make_move(cs, i, j)
                        flow = Flow(bottles=get_copy_of_situation(cs), moves=current_state.moves.copy())
                        flow.moves.append(f"{i} -> {j}")

                        if not is_already_solved(queue_state, cs):
                            queue_state.append(flow)

        return solved_state

# Class for Flow
class Flow:
    def __init__(self, bottles: BottlesArray, moves: List[str] = None):
        self.bottles = bottles
        self.moves = moves or []

# Function to create a new Game from a file
def NewGame(filename: str) -> Game:
    with open(filename, 'r') as file:
        data = json.load(file)
    return Game(bottles=data["bottles"])


# Function to check if a bottle is done
def is_bottle_done(bottle: List[str]) -> bool:
    color = bottle[0]

    if color == 'EMPTY':
        return False

    for b_color in bottle[1:]:
        if b_color != color:
            return False

    return True

# Function to get a copy of the situation
def get_copy_of_situation(situation: BottlesArray) -> BottlesArray:
    return deepcopy(situation)

# Function to hash the bottles (using string representation)
def hash_bottles(bottles: BottlesArray) -> str:
    return str(bottles)

# Function to make a move
def make_move(current_situation: BottlesArray, i: int, j: int) -> None:
    color, index = get_top_color_of_bottle(current_situation[i])
    empty_index = get_bottom_empty_place(current_situation[j])
    current_situation[i][index] = 'EMPTY'
    current_situation[j][empty_index] = color
    if is_move_possible(current_situation[i], current_situation[j]):
        make_move(current_situation, i, j)

# Function to check if a move is possible
def is_move_possible(bottle1: List[str], bottle2: List[str]) -> bool:
    top_color_bottle1, _ = get_top_color_of_bottle(bottle1)
    top_color_bottle2, _ = get_top_color_of_bottle(bottle2)

    empty_spaces_bottle2 = sum(1 for x in bottle2 if x == "EMPTY")
    liquid_bottle1 = sum(1 for x in bottle1 if x == top_color_bottle1)

    if liquid_bottle1 > empty_spaces_bottle2:
        return False

    if bottle2[-1] != "EMPTY":
        return False

    if top_color_bottle1 == bottle1[0] and bottle2[0] == "EMPTY":
        return False

    if top_color_bottle1 != top_color_bottle2 and top_color_bottle2 != "EMPTY":
        return False

    return True

# Function to get the bottom empty place of a bottle
def get_bottom_empty_place(bottle: List[str]) -> int:
    return next((i for i, color in enumerate(bottle) if color == 'EMPTY'), -1)

# Function to get the top color of a bottle
def get_top_color_of_bottle(bottle: List[str]) -> Tuple[str, int]:
    for i in reversed(range(len(bottle))):
        if bottle[i] != 'EMPTY':
            return bottle[i], i
    return 'EMPTY', -1

# Function to check if the game is done
def is_done(bottles: List[List[str]]) -> bool:
    is_done = True
    for bottle in bottles:
        previous_color = ""
        for color in bottle:
            if previous_color == "":
                previous_color = color
                continue
            if color != previous_color:
                is_done = False
                break
            previous_color = color

        if not is_done:
            break

    return is_done


# Function to create a new Game from a file
def NewGame(filename: str) -> Game:
    with open(filename, 'r') as file:
        data = json.load(file)
    return Game(bottles=data["bottles"])

# Function to check if already solved (to be used in the above method)
def is_already_solved(solutions: List[Flow], bottles: BottlesArray) -> bool:
    return any(hash_bottles(val.bottles) == hash_bottles(bottles) for val in solutions)
