from typing import Union, List
import numpy as np
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
import csv
import sys
from multiprocessing import Pool
from tqdm import tqdm

Molecule = Union[str, Chem.Mol]

from descriptastorus.descriptors import rdDescriptors, rdNormalizedDescriptors

def rdkit_2d_features_generator(mol: Molecule) -> np.ndarray:
    """
    Generates RDKit 2D normalized features for a molecule.

    :param mol: A molecule (i.e. either a SMILES string or an RDKit molecule).
    :return: A 1D numpy array containing the RDKit 2D normalized features.
    """
    smiles = Chem.MolToSmiles(mol, isomericSmiles=True) if type(mol) != str else mol
    generator = rdNormalizedDescriptors.RDKit2DNormalized()
    features = generator.process(smiles)[1:]

    return features


def get_features(infile, outfile, use_compound_names=False):
    with open(infile) as f:
        reader = csv.reader(f)
        next(reader)
        feat_list = []
        total_lines = sum(1 for _ in reader)  # Count total lines in the file
        f.seek(0)  # Reset file pointer to the beginning
        next(reader)  # Skip header line
        with tqdm(total=total_lines, desc='Processing') as pbar:
            for line in reader:
                if use_compound_names:
                    line = line[1:]
                smiles = line[0]
                feat = rdkit_2d_features_generator(smiles)
                feat_list.append(feat)
                pbar.update(1)
        feat_array = np.array(feat_list)
        np.save(outfile, feat_array)

infile = sys.argv[1]
outfile = sys.argv[2]
withname = int(sys.argv[3])
if withname == 1:
    use_compound_names = True
else:
    use_compound_names = False
get_features(infile, outfile, use_compound_names)
