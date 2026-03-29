from env.env import MyEnv
from agents.policies import RandomPolicy
from agents.policies import SmartPolicy
import matplotlib.pyplot as plt
env = MyEnv()
wins = 0
total = 5
results = {}
policies={
    "Random":RandomPolicy(),
    "Smart":SmartPolicy()
}
for name,policy in policies.items():
    print(f"\nRunning {name} policy:")
    wins = 0
    for episode in range(5):
        obs = env.reset()
        done = False
       # print("New Episode: ")
        while not done:
           action=policy.select_action(obs)
           print("Guess:", action, "Range:", obs)
           obs,reward,done = env.step(action)
        if obs["last_result"] == "correct":
            wins += 1
        print("Result:", obs["last_result"], "Reward:", reward)
        #print(f"Action:{action},Obs:{obs},Reward:{reward},Done:{done}")
        print("--------------------------------")
    win_rate = wins / total
    results[name] = win_rate
    print(f"{name} Win Rate: {win_rate:.2f}")