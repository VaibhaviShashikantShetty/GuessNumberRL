from env.env import MyEnv
from agents.policies import RandomPolicy

def run_episode(env, policy):
    obs = env.reset()
    done = False
    total_reward = 0

    while not done:
        action = policy.select_action(obs)
        obs, reward, done = env.step(action)
        total_reward += reward

    return total_reward


def main():
    env = MyEnv()
    policy = RandomPolicy()

    episodes = 10
    scores = []

    for i in range(episodes):
        score = run_episode(env, policy)
        print(f"Episode {i+1}: {score}")
        scores.append(score)

    avg = sum(scores) / len(scores)
    print("Average Score:", avg)


if __name__ == "__main__":
    main()