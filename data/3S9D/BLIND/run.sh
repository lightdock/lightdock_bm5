#!/bin/bash

################
# You may change these variables according to your needs
COMPLEX="3S9D"
SWARMS=400
GLOWWORMS=200
STEPS=100
CORES=24
################

# Setup
cp ../${COMPLEX}_A_noh.pdb ../${COMPLEX}_B_noh.pdb .
lightdock_setup ${COMPLEX}_A_noh.pdb ${COMPLEX}_B_noh.pdb ${SWARMS} ${GLOWWORMS} --noxt --noh -anm

# Simulation
lightdock setup.json ${STEPS} -s fastdfire -c ${CORES}

# Generate predictions in PDB format
swarms=$((SWARMS-1))
for i in $(seq 0 $swarms)
  do
    cd swarm_${i}; lgd_generate_conformations.py ../${COMPLEX}_A_noh.pdb ../${COMPLEX}_B_noh.pdb  gso_${STEPS}.out ${GLOWWORMS}; cd ..;
  done

# Cluster per swarm
for i in $(seq 0 $swarms)
  do
    cd swarm_${i}; lgd_cluster_bsas.py gso_${STEPS}.out; cd ..;
  done

echo "Done."
