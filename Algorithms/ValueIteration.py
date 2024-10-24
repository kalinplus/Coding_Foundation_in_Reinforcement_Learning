# Created by SupermanCao
# model-based algorithm

# Question: why the state value of the target state is 100 when gamma equals to 0.9

import numpy as np
from examples.arguments import args


def value_iteration(env, gamma=0.9, theta=1e-10):
    '''
    value iteration for solving the Bellman Optimality Equation(BOE)
    :param env: instance of the environment
    :param gamma: discounted factor
    :param theta: threshold level for convergence
    :return:
    '''
    # initialize the state values
    V = np.random.uniform(args.reward_forbidden, args.reward_target, env.num_states)
    policy = np.zeros((env.num_states, len(env.action_space)))
    iter_count = 0
    while True:
        iter_count += 1
        delta = 0
        # policy update
        # s is an integer, so in the grid world we do % and // to get x and y
        for s in range(env.num_states):
            state = (s % env.env_size[0], s // env.env_size[0])
            v = V[s]
            q_values = []
            for a, action in enumerate(env.action_space):
                next_state, reward = env.get_next_state_reward(state, action)
                # TODO: calculate the action values
                q_values.append(reward + gamma * V[next_state])
            # TODO: finish the policy update
            max_idx = np.argmax(q_values)
            max_action_value = q_values[max_idx]
            policy[s, :] = 0
            policy[s, max_idx] = 1
            # value update
            # TODO: finish the value update
            V[s] = max_action_value  # v_{k+1}
            delta = max(delta, abs(v - V[s]))
        print(f"Iteration {iter_count}, delta: {delta}")
        if delta < theta:
            break
    return V, policy
