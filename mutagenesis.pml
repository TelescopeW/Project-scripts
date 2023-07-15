import os
import pymol

# Set the output directory for saving the PDB files
output_dir = "/Users/H/Desktop/ensemble_dock/"

# Load the input PDB file
pymol.cmd.load("/Users/H/Desktop/ensemble_dock/spike_chain_seg_modified.pdb", "protein")

# Select residue 477 in chain B
pymol.cmd.select("residue_477", "chain B and resi 477")
pymol.cmd.wizard("mutagenesis")
pymol.cmd.get_wizard().do_select("residue_477")
pymol.cmd.get_wizard().set_mode("ASN")
pymol.cmd.frame(1)
pymol.cmd.get_wizard().apply()
pymol.cmd.save("conformation1")

# Get the list of mutant conformations
conformations = pymol.cmd.get_object_list("mutant*")

for i, conformation in enumerate(conformations): pdb_file = os.path.join(output_dir, f"conformation{i+1}.pdb"), pymol.cmd.save(pdb_file, conformation)


# Delete the original and mutant objects
pymol.cmd.delete("protein")
pymol.cmd.delete("mutant*")
