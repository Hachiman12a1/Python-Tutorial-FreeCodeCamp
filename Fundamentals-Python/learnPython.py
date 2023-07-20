from enum import Enum


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


print(State.INACTIVE.value)
print(State["INACTIVE"].value)
print(State.INACTIVE)
print(State["INACTIVE"])
print(list(State))
print(len(State))
