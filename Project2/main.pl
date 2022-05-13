/* Author: Mihriban Guneydas
 * Course:CMPS-5113-180 Adv Programming Lang Concepts
 * Date: Fall 2021*/

happy(md). %fact
happy(jordan). %fact
happy(Y):- smile(Y),laugh(Y). %If a person is smiling and laughing, they are happy  
smile(deangelo). %fact
smile(sabin). %fact
smile(kyle). %fact
smile(X):-laugh(X). %If a person is laughing, they are smiling
smile(A):- see(A,B),smile(B),not(A=B). %A person will begin smiling if they see another person smiling
laugh(mia). %fact
laugh(parker). %fact
laugh(dylan). %fact
laugh(Z):-energetic(Z). %A person will begin laughing if they are energetic
energetic(leila). %fact
energetic(buddy). %fact
energetic(caleb). %fact
see(md,leila). %fact
see(sabin,kyle). %fact
see(parker,jordan). %fact
see(buddy,deangelo). %fact
see(caleb,mia). %fact
see(caleb,dylan). %fact
