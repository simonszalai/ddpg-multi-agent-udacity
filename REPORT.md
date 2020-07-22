## Environment

In this environment, two agents control rackets to bounce a ball over a net. If an agent hits the ball over the net, it receives a reward of +0.1. If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of -0.01. Thus, the goal of each agent is to keep the ball in play.

The observation space consists of 8 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation. Two continuous actions are available, corresponding to movement toward (or away from) the net, and jumping.

The task is episodic, and in order to solve the environment, your agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents).

## Learning Algorithm

The agent utilizes a modified algorithm called DDPG, which stands for Deep Deterministic Policy Gradient, introduced in [this](https://arxiv.org/abs/1509.02971) paper. This algorithm has been adapted to work with multiple agents. The agents use the same replay buffer, but the rest, like the neural networks are independent from each other. Since both agents are rewarded the same way, they are incentivized to collaborate and keep the ball in the air.

## Neural Networks

Both the actor and critic networks have a similar architecture, but since they are mapping to different things, their outputs are different. Both of them are 3 layers deep, the first layer consists of 512 nodes while the second consists of 256 nodes, and both of them utilize batch normalization. The activation function of the actor network is tanh, so it outputs a single number, which is the action in the continuous action space. The critic maps action-state pairs to Q values, so the activation function is a linear function.

## Agent Performance

When training the agent, the following hyperparameters were used:

```
BUFFER_SIZE = int(1e6)  # replay buffer size
BATCH_SIZE = 512  # minibatch size
GAMMA = 0.999  # discount factor
TAU = 1e-4  # for soft update of target parameters
LR_ACTOR = 1e-4  # learning rate of the actor
LR_CRITIC = 3e-4  # learning rate of the critic
WEIGHT_DECAY = 0  # L2 weight decay
UPDATE_EVERY = 4  # timesteps between updates
EPSILON = 1.0  # epsilon for the noise process added to the actions
EPSILON_DECAY = 1e-6  # decay rate for epsilon
```

With the above hyperparameters, the training finished in 403 episodes. You can see the scores as a function of episodes during the training below:

![Scores during the training](training.png)

## Future Work

A few ideas to improve the performance:

1. Utilize prioritized experience replay
1. Try shared neural network
1. Try separate replay buffer
