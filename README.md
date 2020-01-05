# Install mujoco

- Download MuJoCo v2.0 binaries from the official [website](http://www.mujoco.org/) and also obtain the license key.
- Unzip the downloaded `mujoco200` directory into `~/.mujoco/mujoco200`, and place your license key (mjkey.txt) at `~/.mujoco/mjkey.txt`. Note that unzip of the MuJoCo binaries will generate `mujoco200_linux`. You need to rename the directory and place it at `~/.mujoco/mujoco200`.
- Install osmesa related dependencies:
```
$ sudo apt-get install libgl1-mesa-dev libgl1-mesa-glx libglew-dev libosmesa6-dev build-essential libglfw3
```
- Update `bashrc` by adding the following lines and source it
```
export LD_LIBRARY_PATH="<path/to/.mujoco>/mujoco200/bin:$LD_LIBRARY_PATH"
export MUJOCO_PY_FORCE_CPU=True
alias MJPL='LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so:/usr/lib/nvidia-384/libGL.so'

# Install conda package

conda env create -f environment.yml

# Install the mjrl package

cd mjrl
pip install --user -e .

# Install the mj_envs package

cd ../mj_envs
pip install --user -e .

# Set up pythonpath
add the following to bashrc
export PYTHONPATH=<location of mjrl>:<location of mj_envs>:$PYTHONPATH

# Run the examples
cd ../hand_dapg/dapg/examples
# For remote
python job_script.py --output remote_exp --config rl_scratch_remote.txt
# For jar
python job_script.py --output jar_exp --config rl_scratch_jar.txt

# To visualize the learned policies
cd ../
python utils/visualize_policy.py --env_name jar-v0 --policy examples/jar_exp/iterations/best_policy.pickle
python utils/visualize_policy.py --env_name remote-v0 --policy examples/remote_exp/iterations/best_policy.pickle

