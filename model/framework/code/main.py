# imports
import sys

import numpy as np
from ersilia_pack_utils.core import read_smiles, write_out

from synomega_runner import COLUMNS, score_smiles

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# read SMILES from .csv file, assuming one column with header
_, smiles_list = read_smiles(input_file)

# run model
outputs = score_smiles(smiles_list)

# check input and output have the same length
assert len(smiles_list) == len(outputs)

# write output in a .csv file
write_out(np.array(outputs, dtype=np.float32), COLUMNS, output_file, np.float32)
