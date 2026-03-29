import random
class RandomPolicy:
    def select_action(self, obs):
        return random.randint(obs["low"],obs["high"])
class SmartPolicy:
    def select_action(self, obs):
        return (obs["low"]+obs["high"])//2
