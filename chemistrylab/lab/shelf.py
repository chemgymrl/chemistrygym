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
import sys
import numpy as np
sys.path.append("../../") # to access `chemistrylab`
from chemistrylab.chem_algorithms import material
from chemistrylab.chem_algorithms.vessel import Vessel


class Shelf:
    """
    The shelf class holds vessels from experiments.
    
    pop, __getitem__, __delitem__, and append are implemented so shelves can be used similar to a list of vessels
    """
    def __init__(self, *args,**kwargs):
        """
        TODO: Allow the starting vessels to be given as arguments.
        """
        self.vessels = []
        self.n_working = 0


    def get_working_vessels(self):
        """Returns a tuple of the 'working' vessels used for observations and rewards."""
        return tuple(self.vessels[:self.n_working])

    def pop(index=-1):
        return self.vessels.pop(index)
    def __getitem__(self, slice):
        return self.vessels[slice]
    def __delitem__(self, slice):
        del self.vessels[slice]
    def append(self,vessel: Vessel):
        self.vessels.append(vessel)

    def load_vessel(self, path: str):
        """
        TODO: Implement this
        Args:
        - path (str): the path to the vessel that is to be loaded
        """
        pass

    def reset(self):
        """
        TODO: Update this along with __init__
        Resets the shelf to it's initial state
        """
        self.vessels=[]
