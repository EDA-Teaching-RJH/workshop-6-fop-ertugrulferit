
sample_bay = ("Basalt", "Silica", "Iron", "Dust")
sample_bay = list(sample_bay)
if "Dust" in sample_bay:
    sample_bay.remove("Dust")
    
first_element = sample_bay[0]
print(first_element)
print(sample_bay[-1])
print("Cleaned sample_bay:", sample_bay)

number_of_bays = len(sample_bay)
print(number_of_bays)

for element in sample_bay: 
    print("transmitting data for " + element)
    
new_findings = input("Enter 3 new elements found in the bay, seperated by commas:")
new_elements = new_findings.split(",")
print(new_elements)
