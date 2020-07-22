UPDATE_EVERY = 1  # timesteps between updates
BATCH_SIZE = 512  # minibatch size
GAMMA = 0.99  # discount factor
BUFFER_SIZE = int(1e6)  # replay buffer size
TAU = 1e-3  # for soft update of target parameters
LR_ACTOR = 1e-3  # learning rate of the actor
LR_CRITIC = 1e-3  # learning rate of the critic
WEIGHT_DECAY = 0  # L2 weight decay
EPSILON = 1.0  # epsilon for the noise process added to the actions
EPSILON_DECAY = 1e-6  # decay rate for epsilon
