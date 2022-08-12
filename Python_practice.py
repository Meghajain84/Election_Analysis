# print("Hello World")
# print("Apple")
# voting_in_file = []
# voting_in_file.append({"county":"Kansas","registered":525})
# print (voting_in_file)

# How many votes did you get?
#my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")


counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if counties[2] != 'Jefferson':
   print(counties[2])
counties = ["Arapahoe","Denver","Jefferson"]

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

counties_tuples = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuples)):
      print(counties_tuples[i])
for county in counties_tuples:
      print(county)
for county in counties_tuples:
      print(counties)
apple_box_dict = {"Apple": 1, "Banana": 2}
for fruit, count in apple_box_dict.items():
    print(f"{fruit} has {count}")
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")


