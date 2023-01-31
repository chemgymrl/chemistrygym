"""
This file is part of ChemGymRL.

ChemGymRL is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ChemGymRL is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ChemGymRL.  If not, see <https://www.gnu.org/licenses/>.
"""
import unittest
import sys
import os
sys.path.append('../../../')
sys.path.append('../../../chemistrylab/reactions')
import gym
import chemistrylab
from collections import Counter
import numpy as np

ENV_NAME = 'WurtzDistill-v1'

'''
The following unittests should be ran with the dq parameter set in `distillation_bench_v1.py` set to 1000
'''

class DistillationTestCase(unittest.TestCase):
    '''
    Unit test class for distill_v0.py
    '''

    def test_init(self):
        env = gym.make(ENV_NAME)
        boil_vessel = env.boil_vessel
        target_material= env.target_material
        dQ=env.dQ

        self.assertEqual(boil_vessel, env.distillation.boil_vessel)
        self.assertEqual(target_material, env.distillation.target_material)
        self.assertEqual(dQ, env.distillation.dQ)

    def test_get_action_space(self):
        env = gym.make(ENV_NAME)
        action_space = gym.spaces.MultiDiscrete([5,10])
        self.assertEqual(action_space, env.distillation.get_action_space())

    def test_reset(self):
        env = gym.make(ENV_NAME)
        env.reset()
        num_of_vessels = 3
        materials={}
        solutes={}

        self.assertEqual(num_of_vessels, len(env.distillation.reset(env.boil_vessel)))
        self.assertIn('boil_vessel', env.distillation.reset(env.boil_vessel)[0].label)
        self.assertEqual(materials, env.distillation.reset(env.boil_vessel)[1]._material_dict)
        self.assertEqual(solutes, env.distillation.reset(env.boil_vessel)[2]._solute_dict)

    def test_temperature_increase(self):
        env=gym.make(ENV_NAME)
        env.reset()

        initial_temp = env.boil_vessel.temperature

        # setting action to increase temperature
        action = np.array([0, 1000])
        env.step(action)

        final_temp = env.vessels[0].temperature

        self.assertLess(initial_temp, final_temp)

    def test_pour_bv_b1(self):
        env=gym.make(ENV_NAME)
        env.reset()

        # gets material dict of bv before the pour
        bv_material_dict_before = env.vessels[0].get_material_dict()

        # material list of bv before the pour
        # conversion to list is needed to compare with b1
        bv_material_list_before = []
        for key in bv_material_dict_before:
            bv_material_list_before.append(bv_material_dict_before[key][0].get_name())
            bv_material_list_before.append(bv_material_dict_before[key][1])

        # setting action to pour bv into b1
        action = np.array([1, 10])
        env.step(action)

        b1_material_list = []
        # converting into a list of material class and mol, no units
        for key in env.vessels[1]._material_dict:
            b1_material_list.append(env.vessels[1]._material_dict[key][0].get_name())
            b1_material_list.append(env.vessels[1]._material_dict[key][1])

        # env.boil_vessel._material_dict should be empty
        self.assertFalse(env.vessels[0]._material_dict)

        # beaker 1 should have the same material dict as boiling vessel before the pour
        self.assertEqual(bv_material_list_before, b1_material_list)

    def test_pour_b1_b2(self):
        env = gym.make(ENV_NAME)
        env.reset()

        # boil off some materials into b1
        action = np.array([0, 500])
        env.step(action)

        # gets material dict of b1 before the pour
        b1_material_dict_before = env.vessels[1].get_material_dict()

        # material list of b1 before the pour
        # conversion to list is needed to compare with b2
        b1_material_list_before = []
        for key in b1_material_dict_before:
            b1_material_list_before.append(b1_material_dict_before[key][0].get_name())
            b1_material_list_before.append(b1_material_dict_before[key][1])

        # setting action to pour b1 into b2
        action = np.array([2, 10])
        env.step(action)

        b2_material_list = []
        # converting into a list of material class and mol, no units
        for key in env.vessels[2]._material_dict:
            b2_material_list.append(env.vessels[2]._material_dict[key][0].get_name())
            b2_material_list.append(env.vessels[2]._material_dict[key][1])

        # env.vessels[1]._material_dict should be empty
        self.assertFalse(env.vessels[1]._material_dict)

        # beaker 2 should have the same material dict as beaker 1 before the pour
        self.assertEqual(b1_material_list_before, b2_material_list)

    def test_render(self):
        env=gym.make(ENV_NAME)
        env.reset()
        env.render("human")

        # setting action to pour bv into b1
        action = np.array([1, 10])
        env.step(action)

        env.render("human")

        env.reset()
        env.render("full")

        # setting action to pour bv into b1
        action = np.array([1, 10])
        env.step(action)

        env.render("full")


    def test_done(self):
        env = gym.make(ENV_NAME)
        env.reset()

        done = False

        action = np.array([4,0])
        __, __ , done, __ = env.step(action)

        self.assertTrue(done)

