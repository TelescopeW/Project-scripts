import pymol

# Load the first conformation as the ensemble
ensemble = pymol.cmd.load("conformation1_11.pdb")

# Load the remaining conformations into the ensemble
for i in range(2, 12): pymol.cmd.load(f"conformation{i}_11.pdb", "ensemble")

# Save the ensemble as a single PDB file
pymol.cmd.save("ensemble.pdb", "ensemble")