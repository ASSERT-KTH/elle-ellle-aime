from elleelleaime.evaluate.strategies.text.instruct import InstructEvaluationStrategy
from elleelleaime.core.benchmarks.bug import Bug

from typing import Optional, List


class GoogleEvaluationStrategy(InstructEvaluationStrategy):

    def __init__(self, **kwargs):
        super().__init__(kwargs=kwargs)

    def _evaluate_impl(self, bug: Bug, sample: dict) -> Optional[List[dict]]:
        """
        Returns the evaluation for the given bug and sample.

        :param bug: The bug to generate the prompt for.
        :param sample: The sample to evaluate.
        """
        evaluation = []

        if sample["generation"] is None:
            return evaluation

        for generation in sample["generation"]:
            for candidate in generation["candidates"]:
                candidate_patch = candidate["content"]["parts"][0]["text"]
                evaluation.append(
                    self.evaluate_generation(bug, sample, candidate_patch)
                )

        return evaluation
