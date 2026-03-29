import random
class MyEnv:
    def __init__(self): 
        self.secret_number = None
        self.attempts = 0
        self.max_attempts = 5
        self.done = False
        self.low = 1
        self.high = 10
        self.last_result = None
    def reset(self):
        self.secret_number = random.randint(1, 10)
        self.attempts = 0  
        self.done = False
        self.high = 10
        self.low = 1
        self.last_result = "start"
        return self.state() 
    def step(self,action):
        if self.done:
             return None,0,True
        self.attempts += 1
        if action > self.secret_number:
            result = "too high"
            self.high = action - 1
        elif action < self.secret_number:
            result = "too low"
            self.low = action + 1
        else:
            result = "correct"
        if result == "correct":
            reward = 10
        elif abs(action - self.secret_number)==1:
            reward = 2
        else:
            reward = -1
        if result == "correct" or self.attempts >= self.max_attempts:
            self.done = True
        self.last_result = result
        return self.state(), reward,self.done
    
    def state(self):
        return {
        "low": self.low,
        "high": self.high,
        "last_result": self.last_result
    }
    