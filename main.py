from env import MyEnv
env = MyEnv()
obs=env.reset()
print("Initial observation",obs)

print(env.step(5))