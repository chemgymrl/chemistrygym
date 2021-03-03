
# pylint: disable=invalid-name
# pylint: disable=unused-import
# pylint: disable=wrong-import-position

import os
import sys

import numpy as np

import gym
import gym.spaces

sys.path.append("../../")
from chemistrylab.reaction_bench.reaction_bench_v1_engine import ReactionBenchEnv
from chemistrylab.reactions.wurtz_new import Reaction
from chemistrylab.reactions.rate import *

class ReactionBenchEnv_0(ReactionBenchEnv):
    '''
    Class object to define an environment available in the reaction bench.
    '''

    def __init__(self):
        '''
        Constructor class for the ReactionBenchEnv_0 environment.
        '''
        rate_fn = WurtzRates()

        super(ReactionBenchEnv_0, self).__init__(
            reaction=Reaction,
            in_vessel_path=None, # do not include an input vessel
            out_vessel_path=os.getcwd(), # include an output vessel directory
            materials=[ # initialize the bench with the following materials
                {"Material": "1-chlorohexane", "Initial": 0.001},
                {"Material": "2-chlorohexane", "Initial": 0.001},
                {"Material": "3-chlorohexane", "Initial": 0.001},
                {"Material": "Na", "Initial": 0.001}
            ],
            solutes=[ # initialize the bench with the following solutes available
                {"Solute": "H2O", "Initial": 0.001}
            ],
            desired="dodecane",
            overlap=False,
            rate_fn=rate_fn
        )
