def book_appointment(patient_name, practitioner_name, appointment_time):
2
"""
3
Store appointment details in a dictionary.
4
5
Note:
6
- No database is used.
7
- No GUI is used.
8
"""
9
 
10
appointment = {
11
"patient_name": patient_name,
12
"practitioner_name": practitioner_name,
13
"appointment_time": appointment_time
14
}
15
 
16
return appointment
17
 
18
 
19
# Example usage
20
appointment = book_appointment(
21
"Alice Brown",
22
"Dr Smith",
23
"10:30 AM"
24
)
25
 
26
print(appointment)