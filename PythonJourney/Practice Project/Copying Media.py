from os import rename, remove

inputFile = open("/home/mwirigi/Downloads/Whitney Houston - I Have Nothing (Official HD Video).mp4", 'rb')  # Open file in binary read mode
outputFile = open("/home/mwirigi/Desktop/Whitney Houston - I Have Nothing (Official HD Video).mp4", 'wb')  #Open file in binary write mode

msg = inputFile.read(10)  # Restrict reading at 10 bit intervals to save computing resource
                          # Save read data in a varialbe

while len(msg):  # Loop to write the data until all the data in the file is read.
    outputFile.write(msg)
    msg = inputFile.read(10)  # Write the next 

inputFile.close()  # Close file after reading is complete
outputFile.close()  # Close file after writing is complete

#rename("/home/mwirigi/Desktop/Whitney Houston - I Have Nothing (Official HD Video).mp4","/home/mwirigi/Desktop/Whitney Houston - I Have Nothing.mp4")
                                                                       # Renames the file in this location
#remove("/home/mwirigi/Desktop/Whitney Houston - I Have Nothing.mp4")  # Deletes the file in this location

