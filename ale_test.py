import ale_py
# import pathlib
import importlib
from ale_py.roms import Breakout

# from AutoROM.roms import Breakout
env_name = "Breakout"
# ale = atari_py.ALEInterface()
ale = ale_py.ALEInterface()
ale.setInt("random_seed", 10)
ale.setInt("max_num_frames_per_episode", 200)
ale.setFloat("repeat_action_probability", 0)  # Disable sticky actions
ale.setInt("frame_skip", 0)
ale.setBool("color_averaging", False)

# game_rom = importlib.import_module('ale_py.roms.{}'.format(env_name))

import ale_py.roms as roms

print(roms.__all__)

print(roms.resolve_roms())

ale.loadROM(
    roms.resolve_roms()[env_name]
)

print(ale)

# import gym
#
# env = gym.make('Breakout-v0')
# print(env)
#
# obs = env.reset()
#
# print(obs)
#
# # from ale_py.roms.utils import rom_id_to_name
#
# # from gym.envs.atari.environment import ALEInterface
# #
# # ale = ALEInterface()
# # print(ale)
#
# import ale_py.roms as roms
#
# print(roms.__all__)