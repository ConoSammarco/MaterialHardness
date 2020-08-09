
#This program is designed to calculate variable C ( the ionic Contribution to Eg) per bond,  based on bond length,
#valence elctrons, and other factors.
#The mathematics behind this can be view in Dr.Chee-Keong Tans research.
#This program utilizes the vickters scale as a hardness comparison.
#This Program was created by: Cono Sammarco (Clarkson University)
#This program will need to be ran once for every bond length used

import math

BondLength = 0.00 # UNITS: Angstroms
AtomsBondedtoAtomA = 0 #Integer of how many atoms are attached to the first atom
AtomsBondedtoAtomB = 0 #Integer of how many atoms are attached to the second atom
PseudobinaryCrystalRatio = 0
ValanceWithDA = 0 #Valance electrons in Atom A with the D orbital
ValanceWoutDA = 0 #Valance electrons in Atom A without the D orbital
ValanceWithDB = 0 #Valance electrons in Atom B with the D orbital
ValanceWoutDB = 0 #Valance electrons in Atom B without the D orbital
VolumePerBond = 0.00 #Volume of the single bond
TotalVolOfBonds = 0.00 #Volume of all bonds
BPUV = 0.00 #Bonds per unit volume
CorrectionFactor = 0.00 # Correction Factor for d-electron effect



########### CALCULATIONS ##########

radius = 0.5 * BondLength

NC = (AtomsBondedtoAtomA / (1+PseudobinaryCrystalRatio)) + ((PseudobinaryCrystalRatio * AtomsBondedtoAtomB)/(1+PseudobinaryCrystalRatio))
b = 0.089 * NC
ne = (ValanceWoutDA/ AtomsBondedtoAtomA) + (ValanceWoutDB / AtomsBondedtoAtomB)
Vb = VolumePerBond / (TotalVolOfBonds*BPUV)
Ne = ne / Vb
N = 3 * math.pi * math.pi * Ne
N1 = pow(N, 1/3 )
N2 = (4 * N1)/ (0.529 * math.pi) # 0.529 is the BOHR radius
Ks = pow(N2, 1/2)
C = (14.4 * b * abs( ValanceWoutDA + ValanceWithDA - (PseudobinaryCrystalRatio * ValanceWoutDB)) * exp(-Ks*r))/r
Eh = 39.74 / ( pow(BondLength, 2.5))
fi = (C * C)/ ((Eh *Eh) + (C * C))

print('The ionic contribution to Eg in this bond is ' + str(C) + '[eV]')
print('The ionocity of the bond is' + str(fi))

