# List
Names = ['Vishnu', 'Vyshu', 'Ram', 'Sahishna', 'Arjun']
# print(Names)
print(Names[0])  #Op: Vishnu
print(Names[1])  #Op: Vyshu
print(Names[2])  #Op: Ram
print(Names[3])  #Op: Sahishna
print(Names[4])  #Op: Arjun

Names[1] = 'torture'
print (Names)

# tuple
City = ('Bengaluru', 'Chennai', 'Hyderabad')  # Immutable
print(City[0])  # Op: Bengaluru
print(City[1])  # Op: Chennai
print(City[2])  # Op: Hyderabad


# convert tuple to list and modify it

City_list = list(City)

City_list[1] = 'Mumbai'
City_list.append('Pune')

City = tuple(City_list)

print(City)


#tuple - devices
Devices = ('Laptop', 'Mobile', 'Monitor', 'Keyboard', 'Mouse')
print(Devices[0])  # Op: Laptop
print(Devices[1])  # Op: Mobile
print(Devices[2])  # Op: Monitor
print(Devices[3])  # Op: Keyboard
print(Devices[4])  # Op: Mouse

#convert tuple - devices to list and modify it
Devices_list = list(Devices)
Devices_list[4] = 'Wireless Mouse'
Devices_list[3] = 'Wireless Keyboard'
Devices = tuple(Devices_list)
print(Devices)