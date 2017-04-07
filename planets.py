planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
print(planet_list)

planet_list.append("Pluto")
print(planet_list)

rocky_planets = planet_list[0:4]
print(rocky_planets)

# Create another list containing tuples. Each tuple will hold the name of a spacecraft that 
# we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. 
# ('Cassini', 'Saturn')). Iterate over your list of planets, and inside that loop, iterate 
# over the list of tuples. Print, for each planet, which sattelites have visited.

missions = [("Cassini", "Saturn"), ("Viking 1", "Mars"), ("Curiosity", "Mars"), 
("Galileo", "Jupiter"), ("Messenger", "Mercury"), ("Pioneer", "Venus")]

for planet in planet_list:
	print(("------ {} ------").format(planet))
	for mission in missions:
		spacecraft = mission[0]
		destination = mission[1]
		if planet is destination:
			print(spacecraft)
