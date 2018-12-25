#add solution for the transition metals and the lanthanids and Actinides

import random

class periodic_table:
	def __init__(self,initial,name,atomic_number,atomic_mass,valence_e,metal_or_not,nonmetal_or_not,noble_gas,row,column,electronegativity):
		self.initial = initial
		self.name = name
		#print(name)
		self.atomic_mass = atomic_mass
		#print(atomic_mass)
		self.atomic_number = atomic_number
		#print(atomic_number)
		self.valence_e = valence_e
		#print(valence_e)
		self.metal_or_not = metal_or_not
		self.nonmetal_or_not = nonmetal_or_not
		self.noble_gas = noble_gas
		self.row = row
		self.column = column
		self.electronegativity = electronegativity
	def ionic_bonding(atom1,atom2):
		if (atom1.metal_or_not == 'yes' and atom2.metal_or_not == 'no' and atom2.nonmetal_or_not == 'yes') or (atom1.initial == 'H' and atom2.metal_or_not == 'no' and atom2.nonmetal_or_not == 'yes'):
			if (atom1.valence_e+atom2.valence_e == 2 or atom1.valence_e+atom2.valence_e == 8):
				print(atom1.initial,atom2.initial)
			elif atom2.valence_e%2!=0 and (atom1.valence_e%2 != 0 or atom1.valence_e == 1):
				atom1number = (8-atom2.valence_e)/atom1.valence_e
				atom2number = 1
				print(str(atom1number),atom1.initial,str(atom2number),atom2.initial)
			else:
				atom1number = atom2.valence_e
				atom2number = atom1.valence_e
				while atom1number%2 == 0 and atom2number%2 == 0:
					atom1number=atom1number/2
					atom2number = atom2number/2
				print(str(atom1number),atom1.initial,str(atom2number),atom2.initial)
		
		elif atom1.metal_or_not == 'no' and atom1.nonmetal_or_not == 'yes' and atom2.metal_or_not == 'yes':
			if (atom1.valence_e+atom2.valence_e == 2 or atom1.valence_e+atom2.valence_e == 8):
				print(atom2.initial,atom1.initial)
				print('order of the two elements changed due to the fact that it was nonmetal metal not metal nonmetal')
			elif atom1.valence_e%2!=0 and (atom2.valence_e%2 != 0 or atom2.valence_e == 1):
				atom2number = (8-atom1.valence_e)/atom2.valence_e
				atom1number = 1
				print(str(atom2number),atom2.initial,str(atom1number),atom1.initial)
				print('order of the two elements changed due to the fact that it was nonmetal metal not metal nonmetal')
			else:
				atom2number = atom1.valence_e
				atom1number = atom2.valence_e
				while atom2number%2 == 0 and atom1number%2 == 0:
					atom2number=atom2number/2
					atom1number = atom1number/2
				print(str(atom2number),atom2.initial,str(atom1number),atom1.initial)
				print('order of the two elements changed due to the fact that it was nonmetal metal not metal nonmetal')
		else:
			if (atom1.initial == 'H' and atom2.initial == 'H'):
				print('Hydrogen and Hydrogen is a covalent bond so the program will restart this is a covalent bond')
				periodic_table.covalent_bonding(atom1,atom2)
			elif (atom1.nonmetal_or_not == 'yes' and atom2.nonmetal_or_not == 'yes'):
				print('error due to the fact that two nonmetals are being input this is a covalent bond')
				periodic_table.covalent_bonding(atom1,atom2)
	def ionic_bonding_and_number_identifier_and_covalent_identifier(atom1,charge1,atom2,charge2):
		metal = ''
		nonmetal = ''
		'''if atom1.metal_or_not == 'yes' and atom2.nonmetal_or_not == 'yes':
			metal = atom1
			nonmetal = atom2
		elif atom2.metal_or_not == 'yes' and atom1.nonmetal_or_not == 'yes':
			metal = atom2
			nonmetal = atom1
		if (metal == atom2) or (nonmetal == atom1):
			print('ionic bond detected outright')
			if (metal.valence_e+nonmetal.valence_e == 2 or metal.valence_e+nonmetal.valence_e == 8):
				print(metal.initial,nonmetal.initial)
			elif nonmetal.valence_e%2 != 0 and (metal.valence_e%2 != 0 or atom1.valence_e == 1):
				metalnumber = (8-nonmetal.valence_e)/metal.valence_e
				nonmetalnumber = 1
				print(str(metalnumber),metal.initial,str(nonmetalnumber),nonmetal.initial)
			else:
				atom1number = nonmetal.valence_e
				atom2number = metal.valence_e
				while atom1number%2 == 0 and atom2number%2 == 0:
					atom1number=atom1number/2
					atom2number = atom2number/2
				print(str(atom1number),metal.initial,str(atom2number),nonmetal.initial)'''

#this portion of the code use is stupid I was not thinking right there is no case inwhich this'll work i'll work on it later
		'''if (atom1.noble_gas == 'yes' and atom2.nonmetal_or_not == 'yes') or (atom2.noble_gas == 'yes' and atom1.nonmetal_or_not == 'yes'):
			print('there is a lot of building in this stage left to do')
			print('')
			print('that is a covalent bond')
			print('two of the nonmetals needed you cannot just have an electon by itself')
			if (atom2.noble_gas == 'yes' and atom1.nonmetal_or_not == 'yes'):
				if atom1.electon%2 == 0:
					print(str(1),atom1.initial,str(1),atom2.initial)
					print('we put an answer of one for the metal but just remember that you can have any number of that metal that does not use up more than the 8 noble gas electrons')
				else:
					print(str(2),atom1.initial,str(1),atom2.initial)
					print('we put an answer of two for the metal but just remember that you can have any even number of that metal that does not use up more than the 8 noble gas electrons')
			else:
				terminateduetomistake()'''
#this first part may not het be finished but it's for the noble gases
		if atom1.noble_gas == 'yes' and atom2.noble_gas == 'yes':
			print('there clearly is an error here mate')
			print('there is no reason why two noble gases would bond together')
		elif (atom1.noble_gas == 'yes' and atom2.noble_gas == 'no') or (atom2.noble_gas == 'yes' and atom1.noble_gas == 'no'):
			if atom1.noble_gas == 'yes':
				if atom2.name == 'Helium' or atom2.name == 'Neon':
					print('neither Helium no Neon will form covalent bonds because they do not have an expanded octet')
				elif atom2.nonmetal_or_not == 'no' and atom2.metal_or_not == 'yes':
					metal = atom2
					nonmetal = atom1
					print('boy something is wrong noble gases do not do ionic bonds. THEY DO NOT WANT ANY MORE ELECTRONS DUMMY!')
				elif atom2.nonmetal_or_not == 'yes' and atom2.metal_or_not == 'no':
					periodic_table.covalent_bonding(atom1,atom2)
			elif atom2.noble_gas == 'yes':
				if atom2.name == 'Helium' or atom2.name == 'Neon':
					print('neither Helium no Neon will form covalent bonds because they do not have an expanded octet')
				elif atom1.nonmetal_or_not == 'no' and atom1.metal_or_not == 'yes':
					metal = atom1
					nonmetal = atom2
					periodic_table.ionic(metal,nonmetal)
					print('boy something is wrong noble gases do not do ionic bonds. THEY DO NOT WANT ANY MORE ELECTRONS DUMMY!')
				elif atom1.nonmetal_or_not == 'yes' and atom1.metal_or_not == 'no':
					periodic_table.covalent_bonding(atom2,atom1)
			else:
				terminateduetomistake()



		elif (abs(atom1.electronegativity-atom2.electronegativity)>2) or (atom1.nonmetal_or_not == 'yes' and atom1.metal_or_not == 'no' and atom2.nonmetal_or_not == 'no' and atom2.metal_or_not == 'yes') or (atom2.nonmetal_or_not == 'yes' and atom2.metal_or_not == 'no' and atom1.nonmetal_or_not == 'no' and atom1.metal_or_not == 'yes'):
			print('this is an ionic bond')
			if atom1.nonmetal_or_not == 'yes' and atom1.metal_or_not == 'no' and atom2.nonmetal_or_not == 'no' and atom2.metal_or_not == 'yes':
				metal = atom2
				metalcharge = charge2
				nonmetal = atom1
				nonmetalcharge = charge1
				periodic_table.ionic(metal,metalcharge,nonmetal,nonmetalcharge)
			elif atom2.nonmetal_or_not == 'yes' and atom2.metal_or_not == 'no' and atom1.nonmetal_or_not == 'no' and atom1.metal_or_not == 'yes':
				metal = atom1
				metalcharge = charge1
				nonmetal = atom2
				nonmetalcharge = charge2
				periodic_table.ionic(metal,metalcharge,nonmetal,nonmetalcharge)
			elif atom1.electronegativity<atom2.electronegativity:
				metal = atom1
				metalcharge = charge1
				nonmetal = atom2
				nonmetalcharge = charge2
				periodic_table.ionic(metal,metalcharge,nonmetal,nonmetalcharge)
			elif atom1.electronegativity>atom2.electronegativity:
				metal = atom2
				metalcharge = charge2
				nonmetal = atom1
				nonmetal_or_not = charge1
				periodic_table.ionic(metal,metalcharge,nonmetal,nonmetalcharge)
			else:
				terminateduetomistake()
		elif abs(atom1.electronegativity-atom2.electronegativity)<=.4:
			print('this is a pure covalent bond')
			periodic_table.covalent_bonding(atom1,atom2)
		elif abs(atom1.electronegativity-atom2.electronegativity)<=2:
			print('this is a polar covalent pond')
			periodic_table.covalent_bonding(atom1,charge1,atom2,charge2)
	def ionic(metal,metalcharge,nonmetal,nonmetalcharge):
		if (metal.valence_e[metalcharge]+nonmetal.valence_e[nonmetalcharge] == 2) or (metal.valence_e[metalcharge]+nonmetal.valence_e[nonmetalcharge] == 8):
			print('1' + metal.initial + ' 1' + nonmetal.initial)
		elif(metal.valence_e[metalcharge] == 1):
			metalnumber = (8-nonmetal.valence_e[nonmetalcharge])/metal.valence_e[metalcharge]
			nonmetalnumber = 1
			print(str(metalnumber),metal.initial,str(nonmetalnumber),nonmetal.initial)
		else:
			metalnumber = (8 - nonmetal.valence_e[nonmetalcharge])
#			print(str(nonmetal.valence_e[nonmetalcharge]))
			nonmetalnumber = metal.valence_e[metalcharge]
#			print(str(metal.valence_e[metalcharge]))
#			print('line 175')
			num = [2,3,4,5,6,7,8]
			for i in num:
				while nonmetalnumber%i == 0 and metalnumber%i == 0:
					nonmetalnumber = nonmetalnumber/i
					metalnumber=metalnumber/i
			print(str(metalnumber),metal.initial,str(nonmetalnumber),nonmetal.initial)
	def covalent_bonding(atom1,charge1,atom2,charge2):
		print('for the time being only put one of one element and however you need of the other')
		print('')
		numberofatom1 = int(input('what number of atoms for atom1 do you want? '))
		numberofatom2 = int(input('what number of atoms for atom2 do you want? '))
		if numberofatom1 > 1 and numberofatom2 > 1:
			terminate()
		if (numberofatom1*atom1.valence_e[charge1]+numberofatom2*atom2.valence_e[charge2])%2 != 0:
			charge = int(input('what is the charge on the compound if it is negative say the number (like 1 not -1) if it is positivie say - what ever number'))
			if charge != 0:
				periodic_table.covalent1(atom1,charge1,numberofatom1,atom2,charge2,numberofatom2,charge)
				#deal with number of electrons due to charge
			else:
				print('there is no way this would work uneven electron numbers do not work')
				terminate()
		elif (numberofatom1*atom1.valence_e[charge1]+numberofatom2*atom2.valence_e[charge2])%2 == 0:
			periodic_table.covalent1(atom1,charge1,numberofatom1,atom2,charge2,numberofatom2,0)
		else:
			terminateduetomistake()
	def covalent1(atom1,charge1,numberofatom1,atom2,charge2,numberofatom2,charge):
		if numberofatom2 == 1:
			electrons = atom2.valence_e[charge2]+charge
#			print(electrons)
#			if (8-atom1.valence_e[charge1]) == 1:
#				print('all bonds are single bonds')
#				electrons2 = electrons - numberofatom1*(8-atom1.valence_e[charge1])
#				group_e_pairs = electrons2/2
#				group_bonds = electrons - electrons2
#				group_total = group_e_pairs+group_bonds
#				print(group_total)
#				periodic_table.electron(group_total,group_bonds,group_e_pairs)	
#			else:
#				terminateduetomistake()
			electron = atom1.valence_e[charge1]*numberofatom1+atom2.valence_e[charge2]*numberofatom2+charge
			if atom1.name == 'Hydrogen':
				remainder = electron - 2*numberofatom1
			else:
				remainder = electron - 8*numberofatom1
			group_e_pairs = remainder/2
			group_bonds = numberofatom1
			group_total = group_e_pairs + group_bonds
			while group_total < 4:
				group_bonds = group_bonds + 1
				group_total = group_e_pairs+group_bonds
			while group_bonds != numberofatom1:
				group_bonds = group_bonds - 1
			group_total = group_bonds+group_e_pairs
			periodic_table.electron(group_total,group_bonds,group_e_pairs)
		elif numberofatom1 == 1:
			electrons = atom1.valence_e[charge1]+charge
#			print(electrons)
#			if (8-atom2.valence_e[charge2]) == 1:
#				print('all bonds are single bonds')
#				electrons2 = electrons - numberofatom2*(8-atom2.valence_e[charge2])
#				group_e_pairs = electrons2/2
#				group_bonds = electrons - electrons2
#				group_total = group_e_pairs+group_bonds
#				print(group_total)
#				periodic_table.electron(group_total,group_bonds,group_e_pairs)
#			else:
#				terminateduetomistake()
			electron = atom2.valence_e[charge2]*numberofatom2+atom1.valence_e[charge1]*numberofatom1+charge
			if atom2.name == 'Hydrogen':
				remainder = electron - 2*numberofatom2
			else:
				remainder = electron - 8*numberofatom2
			group_e_pairs = remainder/2
#			if numberofatom2 < 4:
#				group_bonds = 4 - group_e_pairs
#			elif numberofatom2 > 4:
#				group_bonds = numberofatom2
			group_bonds = numberofatom2
			group_total = group_e_pairs + group_bonds
#			print(group_bonds)
			while group_total < 4:
				group_bonds = group_bonds + 1
				group_total = group_e_pairs+group_bonds
#			print(group_bonds)
#			print(group_e_pairs)
			while group_bonds != numberofatom2:
				group_bonds = group_bonds - 1
#			print(group_bonds)
			group_total = group_bonds+group_e_pairs
			periodic_table.electron(group_total,group_bonds,group_e_pairs)
		pass
	def electron(group_total,group_bonds,group_e_pairs):
		if group_total == 2:
			if group_bonds == 2:
				print('molecular geometry is linear')
				print('angle bonds is 180 degrees')
				print('and')
				print('electron geometry is linear')
				print('angle bonds is 180 degrees')
		elif group_total == 3:
			if group_bonds == 3:
				print('molecular geometry is trigonal planar')
				print('bond angles are 120 degrees')
				print('and')
				print('electron geometry is trigonal planar')
				print('bond angles are 120 degrees')
			elif group_bonds == 2:
				print('molecular geometry is bent')
				print('bond angles are < 120 degrees')
				print('and')
				print('electron geometry is trigonal planar')
				print('bond angles are 120 degrees')
			else:
				terminateduetomistake()
		elif group_total == 4:
			if group_bonds == 4:
				print('molecular geometry is tetrahedral')
				print('bond angles are 109.5 degrees')
				print('and')
				print('electron geometry is tetrahedral')
				print('bond angles are 109.5 degrees')
			elif group_bonds == 3:
				print('molecular geoemetry is trigonal pyramidal')
				print('bond andles are < 109.5 degrees')
				print('and')
				print('molecular geometry is tetrahedral')
				print('bond angles are 109.5 degrees')
			elif group_bonds == 2:
				print('molecular geometry is bent')
				print('bond angles are < 109.5 degrees')
				print('for reference the bond angle in this case is smaller than that of the trigonal pyramidal which is also < 109.5 degrees')
				print('and')
				print('molecular geometry is tetrahedral')
				print('bond angles are 109.5 degrees')
			else:
				terminateduetomistake()
		elif group_total == 5:
			if group_bonds == 5:
				print('molecular geometry is trigonal bipyramidal')
				print('bond angles are 120 degrees and 90 degrees')
				print('and')
				print('electron geometry is trigonal bipyramidal')
				print('bond angles are 120 degrees and 90 degrees')
			elif group_bonds == 4:
				print('molecular geometry is seesaw')
				print('bond angles are < 120 degrees and < 90 degrees')
				print('and')
				print('molecular geometry is trigonal bipyramidal')
				print('bond angles are 120 degrees and 90 degrees')
			elif group_bonds == 3:
				print('molecular geometry is T-Shape')
				print('bond angles are < 90 degrees ')
				print('and')
				print('molecular geometry is trigonal bipyramidal')
				print('bond angles are 120 degrees and 90 degrees')
			elif group_bonds == 2:
				print('molecular geometry is linear')
				print('bond angles are 180 degrees')
				print('and')
				print('molecular geometry is trigonal bipyramidal')
				print('bond angles are 120 degrees and 90 degrees')
			else:
				terminateduetomistake()
		elif group_total == 6:
			if group_bonds == 6:
				print('molecular geometry is octahedral')
				print('bond angles are 90 degrees')
				print('and')
				print('molecular geometry is octahedral')
				print('bond angles are 90 degrees')
			elif group_bonds == 5:
				print('molecular geometry is square pyramidal')
				print('bond angles are 90 degrees')
				print('and')
				print('molecular geometry is octahedral')
				print('bond angles are 90 degrees')
			elif group_bonds == 4:
				print('molecular geometry is square planar')
				print('bond angles are 90 degrees')
				print('and')
				print('molecular geometry is octahedral')
				print('bond angles are 90 degrees')
			elif group_bonds == 3:
				terminateduetomistake()
			elif group_bonds == 2:
				terminateduetomistake()
			else:
				terminateduetomistake()

def terminate():
	print('invalid inputs')

def terminateduetomistake():
	print('error error error')

# this is the code with no variability in the posible charges in the metals (it's kinda obselite now! I made it better!)
'''
#row one
H = periodic_table('H','Hydrogen',1,1.008,1,'no','yes','no',1,1,2.1)
He = periodic_table('He','Helium',2,4.0026,2,'no','yes','no',1,18,'no data')
#figure out fix for helium bonding


#row two
Li = periodic_table('Li','Lithium',3,6.94,1,'yes','no','no',2,1,1.0)
Be = periodic_table('Be','Beryllium',4,9.0122,2,'yes','no','no',2,2,1.5)
B = periodic_table('B','Boron',5,10.81,3,'no','no','no',2,13,2)
C = periodic_table('C','Carbon',6,12.011,4,'no','yes','no',2,14,2.5)
N = periodic_table('N','Nitrogen',7,14.007,5,'no','yes','no',2,15,3)
O = periodic_table('O','Oxygen',8,15.999,6,'no','yes','no',2,16,3.5)
F = periodic_table('F','Fluorine',9,18.998,7,'no','yes','no',2,17,4)
Ne = periodic_table('Ne','Neon',10,20.180,8,'no','yes','yes',2,18,'no data')
#row three
Na = periodic_table('Na','Sodium',11,22.990,1,'yes','no','no',3,1,.9)
Mg = periodic_table('Mg','Magnesium',12,24.305,2,'yes','no','no',3,2,1.2)
Al = periodic_table('Al','Aluminium',13,26.982,3,'yes','no','no',3,13,1.5)
Si = periodic_table('Si','Silicon',14,28.085,4,'no','no','no',3,14,1.8)
P = periodic_table('P','Phosphorus',15,30.974,5,'no','yes','no',3,15,2.1)
S = periodic_table('S','Sulfur',16,32.06,6,'no','yes','no',3,16,2.5)
Cl = periodic_table('Cl','Chlorine',17,35.45,7,'no','yes','no',3,17,3)
Ar = periodic_table('Ar','Argon',18,39.948,8,'no','yes','yes',3,18,'no data')

#row four
K = periodic_table('K','Potassium',19,39.098,1,'yes','no','no',4,1,.8)
Ca = periodic_table('Ca','Calcium',20,40.078,2,'yes','no','no',4,2,1)
Ga = periodic_table('Ga','Gallium',31,69.723,3,'yes','no','no',4,13,1.6)
Ge = periodic_table('Ge','Germanium',32,72.630,4,'no','no','no',4,14,1.8)
As = periodic_table('As','Arsenic',33,74.922,5,'no','no','no',4,15,2)
Se = periodic_table('Se','Selenium',34,78.972,6,'no','yes','no',4,16,2.4)
Br = periodic_table('Br','Bromine',35,79.904,7,'no','yes','no',4,17,2.8)
Kr = periodic_table('Kr','Kyrpton',36,83.798,8,'no','yes','yes',4,18,'no data')

#row five
Rb = periodic_table('Rb','Rubidium',37,85.468,1,'yes','no','no',5,1,.8)
Sr = periodic_table('Sr','Strontium',38,87.62,2,'yes','no','no',5,2,1)
In = periodic_table('In','Indium',49,114.82,3,'yes','no','no',5,13,1.7)
Sn = periodic_table('Sn','Tin',50,118.71,4,'yes','no','no',5,14,1.8)
Sb = periodic_table('Sb','Antimony',51,121.76,5,'no','no','no',5,15,1.9)
Te = periodic_table('Te','Tellurium',52,127.60,6,'no','no','no',5,16,2.1)
I = periodic_table('I','Iodine',53,126.90,7,'no','yes','no',5,17,2.5)
Xe = periodic_table('Xe','Xenon',54,131.29,8,'no','yes','yes',5,18,'no data')

#row six
Cs = periodic_table('Cs','Caesium',55,132.91,1,'yes','no','no',6,1,.7)
Ba = periodic_table('Ba','Barium',56,137.33,2,'yes','no','no',6,2,.9)
Tl = periodic_table('Tl','Thallium',38,204.38,3,'yes','no','no',6,13,1.8)
Pb = periodic_table('Pb','Lead',84,207.2,4,'yes','no','no',6,14,1.9)
Bi = periodic_table('Bi','Bismuth',85,208.98,5,'yes','no','no',6,15,1.9)
Po = periodic_table('Po','Polonium',86,209,6,'yes','no','no',6,16,2.0)
At = periodic_table('At','Astatine',87,210,7,'no','no','no',6,17,2.2)
Rn = periodic_table('Rn','Radon',86,222,8,'no','yes','yes',6,18,'no data')

#row seven
Fr = periodic_table('Fr','Francium',86,223,1,'yes','no','no',7,1,.7)
Ra = periodic_table('Ra','Radium',87,226,2,'yes','no','no',7,2,.9)
Nh = periodic_table('Nh','Nihonium',113,286,3,'not_defined','not_defined','no',7,13,'no data')
Fl = periodic_table('Fl','Flerovium',114,289,4,'yes','no','no',7,14,'no data')
Mc = periodic_table('Mc','Moscovium',115,290,5,'not_defined','not_defined','no',7,15,'no data')
Lv = periodic_table('Lv','Livermorium',116,293,6,'not_defined','not_defined','no',7,16,'no data')
Ts = periodic_table('Ts','Tennessine',117,294,7,'not_defined','not_defined','no',7,17,'no data')
Og = periodic_table('Og','Oganesson',118,294,8,'not_defined','not_defined','not_defined',7,18,'no data')
'''
#row one
H = periodic_table('H','Hydrogen',1,1.008,[1,1],'no','yes','no',1,1,2.1)
He = periodic_table('He','Helium',2,4.0026,[2,2],'no','yes','no',1,18,'no data')
#figure out fix for helium bonding


#row two
Li = periodic_table('Li','Lithium',3,6.94,[1,1],'yes','no','no',2,1,1.0)
Be = periodic_table('Be','Beryllium',4,9.0122,[2,2],'yes','no','no',2,2,1.5)
B = periodic_table('B','Boron',5,10.81,[3,3],'no','no','no',2,13,2)
C = periodic_table('C','Carbon',6,12.011,[4,4],'no','yes','no',2,14,2.5)
N = periodic_table('N','Nitrogen',7,14.007,[5,5],'no','yes','no',2,15,3)
O = periodic_table('O','Oxygen',8,15.999,[6,6],'no','yes','no',2,16,3.5)
F = periodic_table('F','Fluorine',9,18.998,[7,7],'no','yes','no',2,17,4)
Ne = periodic_table('Ne','Neon',10,20.180,[8,8],'no','yes','yes',2,18,'no data')
#row three
Na = periodic_table('Na','Sodium',11,22.990,[1,1],'yes','no','no',3,1,.9)
Mg = periodic_table('Mg','Magnesium',12,24.305,[2,2],'yes','no','no',3,2,1.2)
Al = periodic_table('Al','Aluminium',13,26.982,[3,3],'yes','no','no',3,13,1.5)
Si = periodic_table('Si','Silicon',14,28.085,[4,4],'no','no','no',3,14,1.8)
P = periodic_table('P','Phosphorus',15,30.974,[5,5],'no','yes','no',3,15,2.1)
S = periodic_table('S','Sulfur',16,32.06,[6,6],'no','yes','no',3,16,2.5)
Cl = periodic_table('Cl','Chlorine',17,35.45,[7,7],'no','yes','no',3,17,3)
Ar = periodic_table('Ar','Argon',18,39.948,[8,8],'no','yes','yes',3,18,'no data')

#row four
K = periodic_table('K','Potassium',19,39.098,[1,1],'yes','no','no',4,1,.8)
Ca = periodic_table('Ca','Calcium',20,40.078,[2,2],'yes','no','no',4,2,1)
Ga = periodic_table('Ga','Gallium',31,69.723,[3,3],'yes','no','no',4,13,1.6)
Ge = periodic_table('Ge','Germanium',32,72.630,[4,4],'no','no','no',4,14,1.8)
As = periodic_table('As','Arsenic',33,74.922,[5,5],'no','no','no',4,15,2)
Se = periodic_table('Se','Selenium',34,78.972,[6,6],'no','yes','no',4,16,2.4)
Br = periodic_table('Br','Bromine',35,79.904,[7,7],'no','yes','no',4,17,2.8)
Kr = periodic_table('Kr','Kyrpton',36,83.798,[8,8],'no','yes','yes',4,18,'no data')

#row five
Rb = periodic_table('Rb','Rubidium',37,85.468,[1,1],'yes','no','no',5,1,.8)
Sr = periodic_table('Sr','Strontium',38,87.62,[2,2],'yes','no','no',5,2,1)
In = periodic_table('In','Indium',49,114.82,[3,3],'yes','no','no',5,13,1.7)
Sn = periodic_table('Sn','Tin',50,118.71,[2,4],'yes','no','no',5,14,1.8)
Sb = periodic_table('Sb','Antimony',51,121.76,[5,5],'no','no','no',5,15,1.9)
Te = periodic_table('Te','Tellurium',52,127.60,[6,6],'no','no','no',5,16,2.1)
I = periodic_table('I','Iodine',53,126.90,[7,7],'no','yes','no',5,17,2.5)
Xe = periodic_table('Xe','Xenon',54,131.29,[8,8],'no','yes','yes',5,18,'no data')

#row six
Cs = periodic_table('Cs','Caesium',55,132.91,[1,1],'yes','no','no',6,1,.7)
Ba = periodic_table('Ba','Barium',56,137.33,[2,2],'yes','no','no',6,2,.9)
Tl = periodic_table('Tl','Thallium',38,204.38,[3,3],'yes','no','no',6,13,1.8)
Pb = periodic_table('Pb','Lead',84,207.2,[2,4],'yes','no','no',6,14,1.9)
Bi = periodic_table('Bi','Bismuth',85,208.98,[5,5],'yes','no','no',6,15,1.9)
Po = periodic_table('Po','Polonium',86,209,[6,6],'yes','no','no',6,16,2.0)
At = periodic_table('At','Astatine',87,210,[7,7],'no','no','no',6,17,2.2)
Rn = periodic_table('Rn','Radon',86,222,[8,8],'no','yes','yes',6,18,'no data')

#row seven
Fr = periodic_table('Fr','Francium',86,223,[1,1],'yes','no','no',7,1,.7)
Ra = periodic_table('Ra','Radium',87,226,[2,2],'yes','no','no',7,2,.9)
Nh = periodic_table('Nh','Nihonium',113,286,[3,3],'not_defined','not_defined','no',7,13,'no data')
Fl = periodic_table('Fl','Flerovium',114,289,[4,4],'yes','no','no',7,14,'no data')
Mc = periodic_table('Mc','Moscovium',115,290,[5,5],'not_defined','not_defined','no',7,15,'no data')
Lv = periodic_table('Lv','Livermorium',116,293,[6,6],'not_defined','not_defined','no',7,16,'no data')
Ts = periodic_table('Ts','Tennessine',117,294,[7,7],'not_defined','not_defined','no',7,17,'no data')
Og = periodic_table('Og','Oganesson',118,294,[8,8],'not_defined','not_defined','not_defined',7,18,'no data')

#periodic_table.ionic_bonding(Na,F)
#periodic_table.ionic_bonding_and_number_identifier_and_covalent_identifier(C,O)
def startup():
	print('')
	print('')
	print('')
	print('')
	print('the code is now starting up')
	print('...')
	print('...')
	print('...')
	print('...')
def restart():
	answer = input('do you want to restart? yes/no ')
	if answer == 'yes':
		start()
	else:
		print('okay cool we are done now I hope you have appreciated this Edwin Meriaux Production!')
		print('')
		print('')
		print('')
		x = random.randint(1,5)
		if x == 1 or x == 3:
			print('Have a great day!')
		elif x == 2 or x == 4:
			print('I hope you enjoy chemistry!')
		elif x == 3:
			print('This is a special thank you to all the people who betatested this code with me!')
def start():
	startup()
	global charge1
	global charge2
	charge1 = 0
	charge2 = 0
	atom1 = input('please input the initial for atom1 ')
	atom2 = input('please input the initial for atom2 ')
	if len(atom1) <= 2 and len(atom2)<= 2:
		atom11 = eval(atom1)
		if int(atom11.valence_e[0]) != int(atom11.valence_e[1]):
			charge1 = int(input("input needed " + atom1 + " has two valence charges " + str(atom11.valence_e[0]) + " and " + str(atom11.valence_e[1]) + " if you want the first one input zero if you want the second one input 1 "))
		atom22 = eval(atom2)
		if int(atom22.valence_e[0]) != int(atom22.valence_e[1]):
			charge2 = int(input("input needed " + atom1 + " has two valence charges " + str(atom22.valence_e[0]) + " and " + str(atom22.valence_e[1]) + " if you want the first one input zero if you want the second one input 1 "))
		periodic_table.ionic_bonding_and_number_identifier_and_covalent_identifier(atom11,charge1,atom22,charge2)
		restart()
	elif len(atom1) > 2 or len(atom2) > 2:
		print('input is too big there is no atom who with an initial longer than two letters. The code is now restarting')
		start()
	else:
		print('invalid input restarting code')
		start()
start()