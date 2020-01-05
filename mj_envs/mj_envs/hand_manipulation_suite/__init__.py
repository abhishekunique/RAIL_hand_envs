from gym.envs.registration import register
from mjrl.envs.mujoco_env import MujocoEnv

# Swing the door open
register(
    id='door-v0',
    entry_point='mj_envs.hand_manipulation_suite:DoorEnvV0',
    max_episode_steps=200,
)
from mj_envs.hand_manipulation_suite.door_v0 import DoorEnvV0

# Hammer a nail into the board
register(
    id='hammer-v0',
    entry_point='mj_envs.hand_manipulation_suite:HammerEnvV0',
    max_episode_steps=200,
)
from mj_envs.hand_manipulation_suite.hammer_v0 import HammerEnvV0

# Reposition a pen in hand
register(
    id='remote-v0',
    entry_point='mj_envs.hand_manipulation_suite:RemoteEnvV0',
    max_episode_steps=100,
)
from mj_envs.hand_manipulation_suite.remote_v0 import RemoteEnvV0

# Relcoate an object to the target
register(
    id='relocate-v0',
    entry_point='mj_envs.hand_manipulation_suite:RelocateEnvV0',
    max_episode_steps=200,
)
from mj_envs.hand_manipulation_suite.relocate_v0 import RelocateEnvV0

# Reposition a pen in hand
register(
    id='jar-v0',
    entry_point='mj_envs.hand_manipulation_suite:JarEnvV0',
    max_episode_steps=100,
)
from mj_envs.hand_manipulation_suite.jar_v0 import JarEnvV0
