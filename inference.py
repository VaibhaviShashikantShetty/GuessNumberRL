from env import MyEnv
from policies import random_policy

def run_episode(env):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = random_policy(state)
        state, reward, done = env.step(action)
        total_reward += reward

    return total_reward


def main():
    env = MyEnv()
    episodes = 10
    scores = []

    for i in range(episodes):
        score = run_episode(env)
        print(f"Episode {i+1}: {score}")
        scores.append(score)

    avg_score = sum(scores) / len(scores)
    print("Average Score:", avg_score)


if __name__ == "__main__":
    main()