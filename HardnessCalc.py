import math



#This Program needs all the  bond infromation inputted and will output the theoretical hardness of the material
#The mathematics behind this can be view in Dr.Chee-Keong Tans research.
#This program utilizes the vickters scale as a hardness comparison.
#This Program was created by: Cono Sammarco (Clarkson University)
#This program will need to be ran once for every bond length used


#Dependent Variables
ValPerVolume = 0.00 #Valence Electrons per Cubic Angstrom of Bond
NumberOfBonds = 2 #Number of Bonds (minimum of one)




############# CALCULATIONS ###############
Hardness = 1.00 #DONOT CHANGE THIS VARIABLE
H = 1.00 #DONOT CHANGE THIS VARIABLE
ni = 0.00#DONOT CHANGE THIS VARIABLE

for i in range(0,NumberOfBonds):
    print('Bond number: '+ str(i+1))
    Bondlength = input('Length of the bond [Angstroms]: ')
    N = input('Valence electrons per cubic angstrom of the bond: ')
    Fi = input('Ionocity of the Bond: ')
    ntot = input('The number of bonds comprising this multicomponent crystal: ')
    ntot = float(ntot)
    Fi = float(Fi)
    N = float(N)
    Bondlength = float(Bondlength)
    I = 1.191 * Fi

    ni = ni + ntot
    H = (350 * pow(N, (2/3))/ (pow(2.71828, I) * pow(Bondlength,2.5)))
    Hardness = Hardness * pow(H, ntot)



Hardness = pow(Hardness, (1/ni))

print('Total Hardness: '+ str(Hardness) + '[Gpa]')

