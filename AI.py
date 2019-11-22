class Node:
    def __init__(self, name, ParentRight, ParentLeft, CostRight, CostLeft):
        self.name = name
        self.ParentRight = ParentRight
        self.ParentLeft = ParentLeft
        self.CostRight = CostRight
        self.CostLeft = CostLeft


    

# This is are Arrays for Every U-Bahn Line and it's corresponding Stations
# Stations name are in English so there is a bit differece in names of some stations

# U Warschauer Str. ◄ ► U Uhlandstr.
U1 = ["Warsaw street", "Silesian Gate", "Goerlitzer station", "Kottbusser Tor", "Prince street", "Hallesches Tor", "Moeckernbruecke", "Gleisdreieck", "Kurfuerstenstrasse", "Nollendorfplatz", "Wittenbergplatz", "Kurfuerstendamm", "Uhlandstrasse"]
TU1 = [2,2,1,2,2,2,1,2,2,2,1,1]
# U Ruhleben ◄ ► U Pankow
U2 = ["Pankow", "Vinetastrasse", "Schoenhauser Allee", "Eberswalder Strasse", "Senefelderplatz", "Rosa-Luxembourg-Platz", "Alexanderplatz", "Klosterstrasse", "Maerkisches Museum", "spittelmarkt", "Hausvogteiplatz", "town center", "Mohrenstrasse", "Potsdamer Platz", "Mendelssohn-Bartholdy-Park", "Gleisdreieck", "Buelowstrasse", "Nollendorfplatz", "Wittenbergplatz", "Zoological Garden", "Ernst-Reuter-Platz", "German opera", "Bismarckstrasse", "Sophie-Charlotte-Platz", "Kaiserdamm", "Theodor-Heuss-Platz", "Neu-Westend", "Olympic Stadium", "ruhleben"]
TU2 = [1,2,2,2,2,2,2,1,2,2,2,1,1,2,1,2,2,1,3,1,2,1,2,1,2,2,1,2]
# U Krumme Lanke ◄ ► U Warschauer Str.
U3 = ["Warsaw street", "Silesian Gate", "Goerlitzer station", "Kottbusser Tor", "Prince street", "Hallesches Tor", "Moeckernbrücke", "Gleisdreieck", "Kurfuersten street", "Nollendorfplatz", "Wittenbergplatz", "Augsburger street", "Spichern street", "Hohenzollernplatz", "Fehrbelliner Platz", "Heidelberg Square", "Ruedesheimer Platz", "Breitenbachplatz", "Podbielskiallee", "Dahlem-Dorf", "Thielplatz", "Oskar-Helene-Heim", "Uncle Tom's hut", "Crooked Lanke"]
TU3 = [2,2,1,2,2,2,1,2,2,2,2,1,2,1,2,2,1,2,1,2,2,2,2]
# U Innsbrucker Platz ◄ ► U Nollendorfplatz
U4 = ["Nollendorfplatz", "Viktoria-Luise-Platz", "Bavarian place", "Rathaus Schoeneberg", "Innsbrucker Platz"]
TU4 = [2,1,2,1]
# U Alexanderplatz ◄ ► U Hönow
U5 = ["Huenow", "Louis-Lewin-street", "Hellersdorf", "Cottbusser Platz", "Kienberg", "Kaulsdorf-Nord", "Wuhletal", "Elsterwerdaer Platz", "Biesdorf-Sued", "Tierpark", "Friedrichsfelde", "Lichtenberg", "Magdalenen street", "Frankfurter Allee", "Samariter street", "Frankfurter Tor", "Weberwiese", "Strausberger Platz", "Schillingstrasse", "Alexanderplatz"]
TU5 = [2,1,2,1,2,2,2,2,3,2,2,1,2,1,2,1,1,2,1]
# U Alt-Tegel ◄ ► U Alt-Mariendorf
U6 = ["Alt-Tegel", "Borsigwerke", "Holzhauser street", "Otis street", "Scharnweber street", "Kurt-Schumacher-Platz", "Afrikanische street", "Rehberge", "Seestrasse", "Leopoldplatz", "Wedding", "Reinickendorfer street", "Schwartzkopff street", "Naturkundemuseum", "Oranienburger Tor", "Friedrich street Bhf", "Franzoesische  street", "Stadtmitte", "Koch street/Checkpoint Charlie", "Hallesches Tor", "Mehringdamm", "Platz Der Luftbrücke", "Parade street", "Tempelhof", "Alt-Tempelhof", "Kaiserin-Augusta- street", "Ullstein street", "Westphalweg", "Alt-Mariendorf"]
TU6 = [1,2,1,1,2,1,1,2,2,1,1,1,1,2,1,1,2,1,1,2,2,1,2,1,1,1,2,1]
# U Grenzallee ◄ ► U Rudow
U7 = ["Rathaus Spandau", "Altstadt Spandau", "Zitadelle", "Haselhorst", "Paulstern street", "Rohrdamm", "Siemensdamm", "Halemweg", "Jakob-Kaiser-Platz", "Jungfernheide Bhf", "Mierendorffplatz", "Richard-Wagner-Platz", "Bismarck street", "Wilmersdorfer  street", "Adenauerplatz", "Konstanzer street", "Fehrbelliner Platz", "Blisse street", "Berliner street", "Bayerischer Platz", "Eisenacher street", "Kleistpark", "Yorckstrasse", "Moeckernbrücke", "Mehringdamm", "Gneisenau street", "Suedstern", "Hermannplatz", "Rathaus Neukoelln", "Karl-Marx- street", "Neukoelln", "Grenzallee", "Blaschkoallee", "Parchimer Allee", "Britz-Sued"]
TU7 = [1,1,2,2,1,2,1,1,2,1,2,1,1,2,1,1,2,1,1,1,2,1,2,2,1,2,2,1,2,1,2,1,2,1,2,1,2,1,1]
# U Hermannstr. ◄ ► U Wittenau
U8 = ["Hermann street", "Leine street", "Boddin street", "Hermannplatz", "Schoenlein street", "Kottbusser Tor", "Moritzplatz", "Heinrich-Heine- street", "Jannowitzbruecke", "Alexanderplatz", "Weinmeister street", "Rosenthaler Platz", "Bernauer street", "Volta street", "Gesundbrunnen Bhf"]               
TU8 = [1,2,2,1,1,2,2,1,2,1,2,1,2,2,1,2,1,2,2,2,1,2,1]
# U Rathaus Steglitz ◄ ► U Osloer Str.
U9 = ["Rathaus Steglitz", "Schloss street", "Walther-Schreiber-Platz", "Friedrich-Wilhelm-Platz", "Bundesplatz", "Berliner street", "Guentzel street", "Spichern street", "Kurfuerstendamm", "Zoologischer Garten Bhf", "Hansaplatz", "Turmstrasse", "Birken street", "Westhafen", "Amrumer street", "Leopoldplatz", "Nauener Platz", "Osloer street"]                  
TU9 = [1,1,2,1,1,2,1,2,2,1,1,1,2,1,1,2,1]
# U Brandenburger Tor ◄ ► U Berlin Hauptbahnhof
U55 = ["Brandenburger Tor", "Bundestag", "Berlin Hauptbahnhof"]	
TU55 = [1,1]

def CheckName(Station):
    if Station not in U1 and Station not in U2 and Station not in U3 and Station not in U4 and Station not in U5 and Station not in U6 and Station not in U7 and Station not in U8 and Station not in U9 and Station not in U55 :
    	return "Enter Valid Station Name !";
    return;

def OperationRight(Station):
	Temp = OtherRoutes(Station)
	Tim = GetTime(Station)
	Result = []
	for i in range(len(Temp)):
		if Temp[i].index(Station) + 1 < len(Temp[i]):
			if Temp[i].index(Station) == (len(Temp[i]) - 1): 
				Result.append(Node(Temp[i][Temp[i].index(Station) + 1], None, Temp[i][Temp[i].index(Station)], None, None))
			elif Temp[i].index(Station) < (len(Temp[i]) - 1):
				Result.append(Node(Temp[i][Temp[i].index(Station) + 1], None, Temp[i][Temp[i].index(Station)], Tim[i][Temp[i].index(Station)], None))
	return Result	

def OperationLeft(Station):
	Temp = OtherRoutes(Station)
	Tim = GetTime(Station)
	Result = []
	for i in range(len(Temp)):
		if Temp[i].index(Station) - 1 >= 0:
			if Temp[i].index(Station) == 0:
				Result.append(Node(Temp[i][Temp[i].index(Station) - 1], Temp[i][Temp[i].index(Station)], None, None, None))
			elif Temp[i].index(Station) > 0 & Temp[i].index(Station) < len(Temp[i]):
				Result.append(Node(Temp[i][Temp[i].index(Station) - 1], Temp[i][Temp[i].index(Station)], None, None, Tim[i][Temp[i].index(Station) - 1]))
	return Result	

def OtherRoutes(Station):
	Routes = []
	Time = []
	if(Station in U1):
		Routes.append(U1)
	if(Station in U2):
		Routes.append(U2)
	if(Station in U3):
		Routes.append(U3)
	if(Station in U4):
		Routes.append(U4)
	if(Station in U5):
		Routes.append(U5)
	if(Station in U6):
		Routes.append(U6)
	if(Station in U7):
		Routes.append(U7)
	if(Station in U8):
		Routes.append(U8)
	if(Station in U9):
		Routes.append(U9)
	if(Station in U55):
		Routes.append(U55)
	return Routes

def GetTime(Station):
	Time = []
	if(Station in U1):
		Time.append(TU1)
	if(Station in U2):
		Time.append(TU2)
	if(Station in U3):
		Time.append(TU3)
	if(Station in U4):
		Time.append(TU4)
	if(Station in U5):
		Time.append(TU5)
	if(Station in U6):
		Time.append(TU6)
	if(Station in U7):
		Time.append(TU7)
	if(Station in U8):
		Time.append(TU8)
	if(Station in U9):
		Time.append(TU9)
	if(Station in U55):
		Time.append(TU55)
	return Time    


def BFS(Departure, Destination):
	if CheckName(Departure) == "Enter Valid Station Name !":
		return CheckName(Departure)
	elif CheckName(Destination) == "Enter Valid Station Name !":
		return CheckName(Destination)
	elif Departure == Destination:
		print("Departure is the Destination")
	else:
		Metros = OtherRoutes(Departure)

		Trees = [[]] * len(Metros)

		Result = []
		Found = True
		Queue = []
		for i in range(len(Trees)):
			Trees[i].append(Node(Departure,None,None,None,None))
			Visited = []
			Visited.append(Node(Departure,None,None,None,None))

			while Found:
				if len(Trees[i]) > 0:
					RightNodes = OperationRight(Trees[i][0].name)
					AddRight = []
					FlagRight = True
					FlagLeft = True
					for j in range(len(RightNodes)):
						for z in range(len(Visited)):
							if Visited[z].name == RightNodes[j].name:
								FlagRight = False
						if FlagRight:
							AddRight.append(RightNodes[j])

					for j in range(len(AddRight)):
						Trees[i].append(AddRight[j])
						Visited.append(AddRight[j])

					for j in range(len(RightNodes)):
						if RightNodes[j].name == Destination:
							Found = False
							Result = Visited
							for z in range(len(Trees[i])):
								Queue.append(Trees[i][z].name)

					LeftNodes = OperationLeft(Trees[i][0].name)
					AddLeft = []	

					for j in range(len(LeftNodes)):
						for z in range(len(Visited)):
							if Visited[z].name == LeftNodes[j].name:
								FlagLeft = False
						if FlagLeft:
							AddLeft.append(LeftNodes[j])

					for j in range(len(AddLeft)):
							Trees[i].append(AddLeft[j])
							Visited.append(AddLeft[j])

					for j in range(len(Visited)):
						if Visited[j].name == Destination:
							Found = False
							Result = Visited
							for z in range(len(Trees[i])):
								Queue.append(Trees[i][z].name)

					if len(Trees[i]) > 0 & Found:
						Trees[i].pop(0)
				else:
					Found = False
					Result = []

		if len(Result) == 0:
			print("No Route from Departure to Destination")
			return 1000
		else:
			Exe = []

			for i in range(len(Result)):
				Exe.append(Result[i].name)

			print ("Expaned Nodes : \n", Exe)

			TimeTaken = 0;
			Path = []
			End = True
			for i in range(len(Result)):
				if Result[i].name == Destination:
					Path.append(Result[i])
			print("Not expanded nodes in the queue: ",Queue)
			while End:
				if (Path[len(Path) - 1].ParentRight is not None) | (Path[len(Path) - 1].ParentLeft is not None):
					for i in range(len(Result)):
						if Result[i].name == Path[len(Path) - 1].ParentRight:
							Path.append(Result[i])
						elif Result[i].name == Path[len(Path) - 1].ParentLeft:
							Path.append(Result[i])
				else:
					End = False

			Path.reverse()

			print("Path to the Destination: ")
			for i in range(len(Path)):
				print(Path[i].name)
				if Path[i].CostLeft != None:
					TimeTaken += Path[i].CostLeft
				elif Path[i].CostRight != None:
					TimeTaken += Path[i].CostRight
			return TimeTaken
			# print("Time Take from Departure to Destination is ", TimeTaken, " minutes")

# BFS("Klosterstrasse", "Hermannplatz")
     					



def DFS(Departure, Destination):
	if CheckName(Departure) == "Enter Valid Station Name !":
		return CheckName(Departure)
	elif CheckName(Destination) == "Enter Valid Station Name !":
		return CheckName(Destination)
	elif Departure == Destination:
		print("Departure is the Destination")
	else:
		Metros = OtherRoutes(Departure)

		Trees = [[]] * len(Metros)

		Result = []
		Found = True
		loop = True
		Queue = []
		for i in range(len(Trees)):
			Trees[i].insert(0, Node(Departure,None,None,None,None))
			Visited = []
			Visited.insert(0, Node(Departure,None,None,None,None))
			while Found:
				if len(Trees[i]) > 0:
					RightNodes = OperationRight(Trees[i][0].name)
					AddRight = []
					FlagRight = True
					FlagLeft = True
					for j in range(len(RightNodes)):
						for z in range(len(Visited)):
							if Visited[z].name == RightNodes[j].name:
								FlagRight = False
						if FlagRight:
							AddRight.insert(0,RightNodes[j])

					for j in range(len(AddRight)):
						Trees[i].insert(0, AddRight[j])
						Visited.insert(0, AddRight[j])

					for j in range(len(RightNodes)):
						if RightNodes[j].name == Destination:
							Found = False
							Result = Visited
							for z in range(len(Trees[i])):
								Queue.append(Trees[i][z].name)

					LeftNodes = OperationLeft(Trees[i][0].name)
					AddLeft = []	
					Trees[i].pop(0)
					for j in range(len(LeftNodes)):
						for z in range(len(Visited)):
							if Visited[z].name == LeftNodes[j].name:
								FlagLeft = False
						if FlagLeft:
							AddLeft.insert(0, LeftNodes[j])

					for j in range(len(AddLeft)):
						Trees[i].insert(0, AddLeft[j])
						Visited.insert(0, AddLeft[j])

					if len(AddLeft) == 0 & loop:
						loop = False


					for j in range(len(Visited)):
						if Visited[j].name == Destination:
							Found = False
							Result = Visited
							for z in range(len(Trees[i])):
								Queue.append(Trees[i][z].name)
				else:
					Found = False
					Result = []

		if len(Result) == 0:
			print("No Route from Departure to Destination")
		else:
			Exe = []

			for i in range(len(Result)):
				Exe.append(Result[i].name)

			print ("Expaned Nodes : \n", Exe)

			TimeTaken = 0
			Path = []
			End = True
			for i in range(len(Result)):
				if Result[i].name == Destination:
					Path.append(Result[i])
			print("Not expanded nodes in the queue: ",Queue)
			while End:
				if (Path[len(Path) - 1].ParentRight is not None) | (Path[len(Path) - 1].ParentLeft is not None):
					for i in range(len(Result)):
						if Result[i].name == Path[len(Path) - 1].ParentRight:
							Path.append(Result[i])
						elif Result[i].name == Path[len(Path) - 1].ParentLeft:
							Path.append(Result[i])
				else:
					End = False

			Path.reverse()

			print("Path to the Destination: ")
			for i in range(len(Path)):
				print(Path[i].name)
				if Path[i].CostLeft != None:
					TimeTaken += Path[i].CostLeft
				elif Path[i].CostRight != None:
					TimeTaken += Path[i].CostRight

			print("Time Take from Departure to Destination is ", TimeTaken, " minutes")



# DFS("Klosterstrasse", "Hermannplatz")


def BFSS(Departure, Destination):
	Metros = OtherRoutes(Departure)

	Trees = [[]] * len(Metros)

	Result = []
	Found = True

	for i in range(len(Trees)):
		Trees[i].append(Node(Departure,None,None,None,None))
		Visited = []
		Visited.append(Node(Departure,None,None,None,None))

		while Found:
			if len(Trees[i]) > 0:
				RightNodes = OperationRight(Trees[i][0].name)
				AddRight = []
				FlagRight = True
				FlagLeft = True
				for j in range(len(RightNodes)):
					for z in range(len(Visited)):
						if Visited[z].name == RightNodes[j].name:
							FlagRight = False
					if FlagRight:
						AddRight.append(RightNodes[j])

				for j in range(len(AddRight)):
					Trees[i].append(AddRight[j])
					Visited.append(AddRight[j])

				for j in range(len(RightNodes)):
					if RightNodes[j].name == Destination:
						Found = False
						Result = Visited

				LeftNodes = OperationLeft(Trees[i][0].name)
				AddLeft = []	

				for j in range(len(LeftNodes)):
					for z in range(len(Visited)):
						if Visited[z].name == LeftNodes[j].name:
							FlagLeft = False
					if FlagLeft:
						AddLeft.append(LeftNodes[j])

				for j in range(len(AddLeft)):
						Trees[i].append(AddLeft[j])
						Visited.append(AddLeft[j])

				for j in range(len(Visited)):
					if Visited[j].name == Destination:
						Found = False
						Result = Visited

				if len(Trees[i]) > 0 & Found:
					Trees[i].pop(0)
			else:
				Found = False
				Result = []

	if len(Result) == 0:
		return 1000
	else:
		Exe = []

		for i in range(len(Result)):
			Exe.append(Result[i].name)


		TimeTaken = 0;
		Path = []
		End = True
		for i in range(len(Result)):
			if Result[i].name == Destination:
				Path.append(Result[i])

		while End:
			if (Path[len(Path) - 1].ParentRight is not None) | (Path[len(Path) - 1].ParentLeft is not None):
				for i in range(len(Result)):
					if Result[i].name == Path[len(Path) - 1].ParentRight:
						Path.append(Result[i])
					elif Result[i].name == Path[len(Path) - 1].ParentLeft:
						Path.append(Result[i])
			else:
				End = False

		Path.reverse()

		for i in range(len(Path)):
			if Path[i].CostLeft != None:
				TimeTaken += Path[i].CostLeft
			elif Path[i].CostRight != None:
				TimeTaken += Path[i].CostRight
		return TimeTaken

def Greedy(Departure, Destination):
	if CheckName(Departure) == "Enter Valid Station Name !":
		return CheckName(Departure)
	elif CheckName(Destination) == "Enter Valid Station Name !":
		return CheckName(Destination)
	elif Departure == Destination:
		print("Departure is the Destination")
	else:
		Metros = OtherRoutes(Departure)

		Trees = [[]] * len(Metros)
		Queue = []
		Result = []
		Found = True
		MiniRight = 1000;
		MiniLeft = 1000;
		TimeRight = []
		TimeLeft = []
		NextRight = Node(None,None,None,None,None)
		NextLeft = Node(None,None,None,None,None)
		for i in range(len(Trees)):
			Trees[i].append(Node(Departure,None,None,None,None))
			Visited = []
			Visited.append(Node(Departure,None,None,None,None))
			while Found:
				if len(Trees[i]) > 0:
					RightNodes = OperationRight(Trees[i][0].name)
					LeftNodes = OperationLeft(Trees[i][0].name)
					Right = []
					Left = []
					for j in range(len(RightNodes)):
						if RightNodes[j] != None:
							Right.append(RightNodes[j])
					for j in range(len(LeftNodes)):
						if LeftNodes[j] != None:
							Left.append(LeftNodes[j])
					for j in range(len(Right)):
						TimeRight.append(BFSS(Right[j].name, Destination))
						MiniRight = min(TimeRight)
					for j in range(len(Left)):
						TimeLeft.append(BFSS(Left[j].name, Destination))
						MiniLeft = min(TimeLeft)
					if MiniRight < MiniLeft:
						First = True
						for j in range(len(Right)):
							Temp = BFSS(Right[j].name, Destination)
							if Temp == MiniRight & First:
								NextRight = Right[j]
								First = False
						if NextRight not in Visited:
							Trees[i].append(NextRight)
							Visited.append(NextRight)
						if NextRight.name == Destination:
							Found = False
							Result = Visited
							for z in range(len(Trees[i])):
								Queue.append(Trees[i][z].name)
					elif MiniLeft < MiniRight:
						First = True
						for j in range(len(Left)):
							Temp = BFSS(Left[j].name, Destination)
							if (Temp == MiniLeft) and First:
								NextLeft = Left[j]
								First = False
						if NextLeft not in Visited:
							Trees[i].append(NextLeft)
							Visited.append(NextLeft)
						if NextLeft.name == Destination:
							Found = False
							Result = Visited
					Trees[i].pop(0)
				else:
					Found = False
					Result = []
			Exe = []

			for i in range(len(Result)):
				Exe.append(Result[i].name)

			print ("Expaned Nodes : \n", Exe)

			TimeTaken = 0
			Path = []
			End = True
			for i in range(len(Result)):
				if Result[i].name == Destination:
					Path.append(Result[i])
			print("Not expanded nodes in the queue: ",Queue)
			while End:
				if (Path[len(Path) - 1].ParentRight is not None) | (Path[len(Path) - 1].ParentLeft is not None):
					for i in range(len(Result)):
						if Result[i].name == Path[len(Path) - 1].ParentRight:
							Path.append(Result[i])
						elif Result[i].name == Path[len(Path) - 1].ParentLeft:
							Path.append(Result[i])
				else:
					End = False

			Path.reverse()

			print("Path to the Destination: ")
			for i in range(len(Path)):
				print(Path[i].name)
				if Path[i].CostLeft != None:
					TimeTaken += Path[i].CostLeft
				elif Path[i].CostRight != None:
					TimeTaken += Path[i].CostRight

			print("Time Take from Departure to Destination is ", TimeTaken, " minutes")

#To run Breadth First Search
BFS("Klosterstrasse", "Hermannplatz")
#To run Deapth First Search
DFS("Klosterstrasse", "Hermannplatz")
#To run Greedy Search
Greedy("Klosterstrasse", "Hermannplatz")









