from env import MyEnv
env = MyEnv()
obs=env.reset()
print("Initial observation",obs)

print(env.step(5))
print(env.step(7))
print(env.step(18))