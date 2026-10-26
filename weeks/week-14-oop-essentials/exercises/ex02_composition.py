"""Exercise 02: compose Bot with a strategy."""

from collections.abc import Callable

Strategy = Callable[[dict[str, int]], str]


class Bot:
    """Choose actions using a replaceable strategy function."""

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        return self.strategy(state)


def move_toward_goal(state: dict[str, int]) -> str:
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state: dict[str, int]) -> str:
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: dict[str, int]) -> str:
    return move_toward_goal(state)


def aggressive(state: dict[str, int]) -> str:
    return move_toward_goal(state)


def main() -> None:
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    for name, strategy in (("defensive", defensive), ("balanced", balanced), ("aggressive", aggressive)):
        print(f"{name}: {Bot(strategy).choose_action(state)}")


if __name__ == "__main__":
    main()
