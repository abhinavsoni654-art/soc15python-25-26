student = {"name":"abhinav",
       "age":15,
       "college":"MIT ADT University",
       "course": "B.Tech CSE"}
print("Dictionery",student)

#Update dictionery 
student["age"] = 15
student["Year"] = "First Year"
print("Updated Dictionery:", student )

#Removing elements 
student.pop("course")
print("After removing element:",student)

#Merging dictionaries
marks={"MFC": 84, "PL":96 } 
merged_dict= student | marks 
print("Merged dictionary:", merged_dict)
