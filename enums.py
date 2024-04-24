from enum import Enum

class State(Enum):
    PLAYING =0
    PAUSED = 1
    GAME_OVER = 3

state=State.PLAYING
print(state.value)