import sys
sys.path.append('../../')
sys.path.append('../../chemistrylab/reactions')
import gym
import chemistrylab
import numpy as np
from gym import envs

all_envs = envs.registry.all()
env_ids = [env_spec.id for env_spec in all_envs if 'React' in env_spec.id]
print(env_ids)
select_env = int(input(f"enter a number to chose which environment you want to run (0-{len(env_ids) - 1}): "))
env = gym.make(env_ids[select_env])
render_mode = "full"

action_set = ['Temperature', 'Volume', 'NaCl']

assert len(action_set) == env.action_space.shape[0]

done = False
state = env.reset()
total_reward = 0
round = 0
while not done:
    # print(state)
    env.render(mode=render_mode)
    # action = np.zeros(env.action_space.shape[0])
    print('--------------------')
    # for i, a in enumerate(action_set):
    #     action[i] = float(input(f'{a}: '))
    action = np.ones(env.action_space.shape[0])
    if round != 0:
        action[-1] = 0
    state, reward, done, _ = env.step(action)
    total_reward += reward
    print(f'reward: {reward}')
    print(f'total_reward: {total_reward}')
    round += 1
    if done:
        wait = input('PRESS ENTER TO QUIT')
