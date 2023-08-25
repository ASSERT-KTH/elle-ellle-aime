from elleelleaime.evaluate.strategies.strategy import PatchEvaluationStrategy
from elleelleaime.evaluate.strategies.text.replace import ReplaceEvaluationStrategy


class PatchEvaluationStrategyRegistry:
    """
    Class for storing and retrieving models based on their name.
    """

    def __init__(self, **kwargs):
        self._strategies: dict[str, PatchEvaluationStrategy] = {
            "replace": ReplaceEvaluationStrategy(**kwargs),
        }

    def get_evaluation(self, name: str) -> PatchEvaluationStrategy:
        if name.lower().strip() not in self._strategies:
            raise ValueError(f"Unknown strategy {name}")
        return self._strategies[name.lower().strip()]
