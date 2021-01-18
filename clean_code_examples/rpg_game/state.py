from abc import ABC


class State(ABC):

    validators = []

    def get_validators(self):
        return self.validators

    def _run_validators(self):
        pass

    def steps(self):
        pass

    def run(self):
        pass

    def _run(self):
        pass

    def next_step(self):
        """
        Run step by step.
        """
        pass
