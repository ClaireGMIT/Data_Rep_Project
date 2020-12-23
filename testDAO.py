from Tablets2DAO import tabletsDAO

tabprdn = {
    'Batch_No': 45, 
    'API_Lot_No': "AB",
    'API_Particle_Size': 'Large',
    'Screen_Size': '3',
    'Blend_Time': 15,
    'Compressor': 'Compress1',
    'Inlet_Temp': 123,
    'Spray_Rate': 123,
    'Dissolution': 75
}

tabprdn2 = {
    'Batch_No': 45, 
    'API_Lot_No': "AA",
    'API_Particle_Size': 'Small',
    'Screen_Size': '3',
    'Blend_Time': 15,
    'Compressor': 'Compress1',
    'Inlet_Temp': 999,
    'Spray_Rate': 999,
    'Dissolution': 100
}


#returnvalue = tabletsDAO.create(tabprdn)
returnvalue = tabletsDAO.getAll()
print(returnvalue)

returnvalue = tabletsDAO.findByID(tabprdn2['Batch_No'])
print(returnvalue)

returnvalue = tabletsDAO.update(tabprdn2)
print(returnvalue)

returnvalue = tabletsDAO.findByID(tabprdn2['Batch_No'])
print(returnvalue)

returnvalue = tabletsDAO.delete(tabprdn2['Batch_No'])
print(returnvalue)

returnvalue = tabletsDAO.getAll()
print(returnvalue)
