# Yeh sahi rahega
import sys
sys.path.append('server')  # server folder ko path mein add karo

from my_env_environment import MyEnvironment

env = MyEnvironment()
env.reset()

action = {"message": "I need leave for 2 days"}
result = env.step(action)

print("RESULT:", result)