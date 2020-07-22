# Multi-Agent DDPG for Continuous Control - Udacity DRLND Project 3

Multi-Agent Deep Deterministic Policy Gradients reinforcement learning algorithm to solve a continuous control environment

## Project Details

This is the third and final assignment of Udacity's Deep Reinforcement Learning Nanodegree. In this environment, two agents control rackets to bounce a ball over a net. If an agent hits the ball over the net, it receives a reward of +0.1. If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of -0.01. Thus, the goal of each agent is to keep the ball in play.

The observation space consists of 8 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation. Two continuous actions are available, corresponding to movement toward (or away from) the net, and jumping.

The task is episodic, and in order to solve the environment, your agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents).

![Trained agent navigates in the environment](trained_agent.gif)

## Getting Started

1. After cloning the repository, download the custom Unity enviroment matching your operating system, then copy it to the root folder of this project.

   Download links:

   - [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)
   - [MacOS](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)
   - [Windows 32-bit](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)
   - [Windows 64-bit](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)

1. Create and activate a new virtual Python environment
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
1. Install dependencies by running the command below from the root of this repository:
   ```
   pip install -r requirements.txt
   ```
1. To train the agent and see how it performs, run `jupyter notebook` from the root of this repository, then open `Multi_Agent.ipynb`, and run the cells in the notebook.
