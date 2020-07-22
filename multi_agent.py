import numpy as np

from ddpg_agent import Agent
from buffer import ReplayBuffer
from config import *


class MultiAgent:
    """Interacts with and learns from the environment."""

    def __init__(self, agent_count, state_size, action_size, random_seed):
        """Initialize a MultiAgent object.

        Params
        ======
            agent_count (int): Number of agents
        """

        self.memory = ReplayBuffer(action_size, BUFFER_SIZE, BATCH_SIZE, random_seed)

        self.agents = [
            Agent(
                memory=self.memory,
                state_size=state_size,
                action_size=action_size,
                random_seed=random_seed,
            )
            for _ in range(agent_count)
        ]

    def step(self, states, actions, rewards, next_states, dones, timestep):
        # Save experience in replay memory
        for state, action, reward, next_state, done in zip(
            states, actions, rewards, next_states, dones
        ):
            self.memory.add(state, action, reward, next_state, done)

        # Learn, if enough samples are available in memory
        if len(self.memory) > BATCH_SIZE and timestep % UPDATE_EVERY == 0:
            for agent in self.agents:
                agent.learn(self.memory.sample(), GAMMA)

    def act(self, all_states):
        """Get actions from all agents"""
        actions = [
            agent.act(np.expand_dims(states, axis=0))
            for agent, states in zip(self.agents, all_states)
        ]
        return actions

    def reset(self):
        for agent in self.agents:
            agent.reset()
