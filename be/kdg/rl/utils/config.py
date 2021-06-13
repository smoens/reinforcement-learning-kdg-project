import os

############# PARAMETERS #############
current_experiment = "experiment6"
n_episodes = 10000
output_freq = 100      # define at what frequency of episodes we want to create output

def init(environment):
    init_folders(environment, experiment=current_experiment)


params = {
    # directories for storing output graphs and results
    "dirs": {
        "output": os.path.join("./", "output"),
        "qval": os.path.join("images", "qval"),
        "reward": os.path.join("images", "reward")
    },
    "experiment": {
        "default": {
            'description': 'Experiment QLearning with default settings',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'Qlearning',
            'nstep': None,
            'α': 0.7,
            'λ': 0.0005,
            'γ': 0.9,
            't_max': 99
        },
        "experiment1": {
            'description': 'Experiment QLearning with completely random agent',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'Qlearning',
            'nstep': None,
            'α': 0.7,
            'λ': 0.0005,
            'γ': 0.9,
            't_max': 99
        },
        "experiment2": {
            'description': 'Experiment QLearning',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'Qlearning',
            'nstep': None,
            'α': 0.7,
            'λ': 0.0005,
            'γ': 0.9,
            't_max': 99
        },
        "experiment3": {
            'description': 'Experiment QLearning with lower discount rate',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'Qlearning',
            'nstep': None,
            'α': 0.7,
            'λ': 0.0005,
            'γ': 0.5,
            't_max': 99
        },
        "experiment4": {
            'description': 'Experiment QLearning with decreased learning rate',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'Qlearning',
            'nstep': None,
            'α': 0.5,
            'λ': 0.0005,
            'γ': 0.5,
            't_max': 99
        },
        "experiment5": {
            'description': 'Experiment QLearning with very small learning rate',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'Qlearning',
            'nstep': None,
            'α': 0.2,
            'λ': 0.0005,
            'γ': 0.5,
            't_max': 99
        },
        "experiment6": {
            'description': 'Experiment QLearning with large learning rate',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'Qlearning',
            'nstep': None,
            'α': 0.9,
            'λ': 0.0005,
            'γ': 0.5,
            't_max': 99
        },
        "experiment7": {
            'description': 'Experiment QLearning with very small discount rate',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'Qlearning',
            'nstep': None,
            'α': 0.7,
            'λ': 0.0005,
            'γ': 0.1,
            't_max': 99
        },
        "experiment8": {
            'description': 'Experiment NStepQLearning',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'NStepQlearning',
            'nstep': '3',
            'α': 0.7,
            'λ': 0.0005,
            'γ': 0.9,
            't_max': 99
        },
        "experiment6": {
            'description': 'Experiment NStepQLearning with lower discount',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'NStepQlearning',
            'nstep': '3',
            'α': 0.7,
            'λ': 0.0005,
            'γ': 0.5,
            't_max': 99
        },
        "experiment7": {
            'description': 'Experiment NStepQLearning with larger step-size',
            'environment': 'FrozenLakeEnvironment',
            'learning': 'NStepQlearning',
            'nstep': '7',
            'α': 0.7,
            'λ': 0.0005,
            'γ': 0.5,
            't_max': 99
        }
    },
    "models": {
        "model1": {
            "model_filename": "model1.h5",
            "lr": 0.001,
            "num_epochs": 10,
            "validation_steps": 10,
            "metrics": ["acc"],
            "seed": 1354874613,
        }
    },
    "environments": {
        "FrozenLake": "FrozenLakeEnvironment",
        "CartPole": "CartPoleEnvironment"
    },
    "methods": [
        "Qlearning",
        "NStepQLearning",
        "MonteCarloLearning",
        "DeepQLearning",
        "DoubleDeepQLearning"
    ]
}


def init_folders(env, experiment):
    path_experiment = os.path.join(
        params.get("dirs").get("output"),
        params.get("experiment").get(current_experiment).get("environment"),
        experiment)
    path_qval = params.get("dirs").get("qval")
    path_reward = params.get("dirs").get("reward")
    if not os.path.exists(path_experiment):
        os.makedirs(path_experiment)
        os.makedirs(os.path.join(path_experiment, path_qval))
        os.makedirs(os.path.join(path_experiment, path_reward))
    return
