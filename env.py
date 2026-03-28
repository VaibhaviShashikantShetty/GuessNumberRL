import random
class MyEnv:
    def __init__(self): 
        self.secret_number = None
        self.attempts = 0
        self.max_attempts = 5
        self.done = False
        self.low = 1
        self.high = 10
    def reset(self):
        self.secret_number = random.randint(1,10)
        self.attempts = 0  
        self.done = False
        self.high = 10
        self.low = 1
        return{
            "low" : self.low
            "high" : self.high
            "last_result" : "start"
        }      
    def step(self,action):
        if self.done:
             return None,0,True
        self.attempts += 1
        if action > self.secret_number:
            result = "too high"
            high = action-1
        elif action < self.secret_number:
            result = "too low"
            low = action+1
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
        observation ={
            "low":self.low,
            "high":self.high,
            "last_result":result
        }
        return observation, reward,self.done
    