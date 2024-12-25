import sys
from enum import Enum

input_file = sys.argv[1]

class State(Enum):
    Between = 0
    Lock = 1
    Key = 2

state = State.Between
keys = []
locks = []

with open(input_file) as f:
    for line in f:
        line = line.rstrip()
        match state:
            case State.Between:
                if line == "#####":
                    state = State.Lock
                    new_lock = [0] * 5
                else:
                    state = State.Key
                    new_key = [-1] * 5
            case State.Lock:
                if line == "":
                    state = State.Between
                    locks.append(new_lock)
                    continue

                for i in range(5):
                    if line[i] == "#":
                        new_lock[i] += 1

            case State.Key:
                if line == "":
                    state = State.Between
                    keys.append(new_key)
                    continue

                for i in range(5):
                    if line[i] == "#":
                        new_key[i] += 1

    if state == State.Key:
        keys.append(new_key)
    else:
        locks.append(new_lock)


def find_keys_and_locks(keys: list[list[int]], locks: list[list[int]]) -> int:
    result = 0

    for key in keys:
        for lock in locks:
            if fit(key, lock):
                result += 1

    return result


def fit(key: list[int], lock: list[int]) -> int:
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False

    return True

