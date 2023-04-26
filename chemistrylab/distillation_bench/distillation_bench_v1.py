'''
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

Distillation Bench Environment
:title: distillation_bench_v1.py
:author: Mitchell Shahen, Mark Baula
:history: 2020-07-23
'''

# pylint: disable=invalid-name
# pylint: disable=wrong-import-position

# import external modules
import os
import pickle
import sys
from copy import deepcopy
from random import choice

# import local modules
sys.path.append("../../") # to access `chemistrylab`
from chemistrylab.chem_algorithms.reward import DistillationReward
from chemistrylab.chem_algorithms import material, util, vessel
from chemistrylab.reactions.reaction_base import _Reaction
from chemistrylab.general_bench.general_bench import *
import importlib


def wurtz_vessel(add_mat):
    """
    Function to generate an input vessel for the oil and water extraction experiment.

    Parameters
    ---------------
    None

    Returns
    ---------------
    `extract_vessel` : `vessel`
        A vessel object containing state variables, materials, solutes, and spectral data.

    Raises
    ---------------
    None
    """

    # initialize extraction vessel
    boil_vessel = vessel.Vessel(label='boil_vessel')

    # initialize C6H14
    C6H14 = material.C6H14()

    # initialize material
    products = {'dodecane': material.Dodecane,
        '5-methylundecane': material.FiveMethylundecane,
        '4-ethyldecane': material.FourEthyldecane,
        '5,6-dimethyldecane': material.FiveSixDimethyldecane,
        '4-ethyl-5-methylnonane': material.FourEthylFiveMethylnonane,
        '4,5-diethyloctane': material.FourFiveDiethyloctane,
        'NaCl': material.NaCl
    }

    try:
        if add_mat == "":
            add_mat = choice(list(products.keys()))
        
        add_material = products[add_mat]()
    
    except KeyError:
        add_mat = 'dodecane'
        add_material = products[add_mat]()
    
    add_material.set_solute_flag(True)
    add_material.set_color(0.0)
    add_material.set_phase('l')

    # material_dict
    material_dict = {
        C6H14.get_name(): [C6H14, 4.0, 'mol'],
        add_material.get_name(): [add_material, 1.0, 'mol']
    }

    # solute_dict
    solute_dict = {
        add_material.get_name(): {C6H14.get_name(): [C6H14, 1.0, 'mol']}
    }

    if choice([0, 1]) > 0.5:
        if add_mat == 'NaCl':
            add_material2 = material.Dodecane()
            material_dict[add_material2.get_name()] = [add_material2, 1.0, 'mol']
            solute_dict[add_material2.get_name()] = {C6H14.get_name(): [C6H14, 1.0, 'mol']}

        else:
            add_material2 = material.NaCl()
            material_dict[add_material2.get_name()] = [add_material2, 1.0, 'mol']
            solute_dict[add_material2.get_name()] = {C6H14.get_name(): [C6H14, 1.0, 'mol']}

    material_dict, solute_dict, _ = util.check_overflow(
        material_dict=material_dict,
        solute_dict=solute_dict,
        v_max=boil_vessel.get_max_volume()
    )

    # set events and push them to the queue
    boil_vessel.push_event_to_queue(
        events=None,
        feedback=[
            ['update material dict', material_dict],
            ['update solute dict', solute_dict]
        ],
        dt=0
    )
    boil_vessel.push_event_to_queue(
        events=None,
        feedback=None,
        dt=-100000
    )

    boil_vessel.default_dt=0.01
    
    return boil_vessel, add_mat


class GeneralWurtzDistill_v1(GenBench):
    """
    Class to define an environment which performs a Wurtz extraction on materials in a vessel.
    """

    def __init__(self):
        d_rew= lambda x,y:DistillationReward(vessels=x,desired_material=y).calc_reward()
        vessel_generators = [
            lambda x:wurtz_vessel(x)[0],
            lambda x:vessel.Vessel("Beaker 1"),
            lambda x:vessel.Vessel("Beaker 2"),
        ]
        dQ=20000.0
        amounts=np.linspace(0,1,10).reshape([10,1])
        temps=amounts*2-1
        T=297.0
        actions = [
            Action([0],    dQ * temps,           'change_heat',    [1],   0.01,   False),
            Action([0],    amounts,              'pour by volume', [1],   0.01,   False),
            Action([1],    amounts,              'pour by volume', [2],   0.01,   False),
            Action([0], [[T, False], [T, True]], 'wait',           [1],   0.01,   False),
            Action([0],  [[0]],                  'mix',            None,  0,      True)
        ]
        
        targets = [
            "dodecane",
            "5-methylundecane",
            "4-ethyldecane",
            "5,6-dimethyldecane",
            "4-ethyl-5-methylnonane",
            "4,5-diethyloctane",
            "NaCl"
        ]
        
        super(GeneralWurtzDistill_v1, self).__init__(
            vessel_generators,
            actions,
            importlib.import_module("chemistrylab.reactions.available_reactions.precipitation"),
            ["layers","PVT","targets"],
            reward_function=d_rew,
            react_list=[0],
            targets=targets
        )


