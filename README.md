# Deep Deterministic Policy Gradients for Continuous Control - Udacity DRLND Project 2

Deep Deterministic Policy Gradients reinforcement learning algorithm to solve a continuous control environment

## Project Details

This is the second assignment of Udacity's Deep Reinforcement Learning Nanodegree. In this project, the agent has to control a simulated robotic arm. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of the agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

The environment has two version, in the first, a single arm is controlled, in the second, 20 arms are training in parallel to speed up experience collection. I choose the first option, where in order to solve the environment, the agent must get an average score of +30 over 100 consecutive episodes.

![Trained agent navigates in the environment](trained_agent.gif)

## Getting Started

1. After cloning the repository, download the custom Unity enviroment matching your operating system, then copy it to the root folder of this project.

   Download links:

   - [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
   - [MacOS](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
   - [Windows 32-bit](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
   - [Windows 64-bit](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)

1. Create and activate a new virtual Python environment
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
1. Install dependencies by running the command below from the root of this repository:
   ```
   pip install -r requirements.txt
   ```
1. To train the agent and see how it performs, run `jupyter notebook` from the root of this repository, then open `Continuous_Control.ipynb`, and run the cells in the notebook.
