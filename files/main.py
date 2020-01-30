# TODO
# Creating a file
# Reading from file
# Writing to file

# Opening a file
  
file1 = open("myfile.txt") 
# Reading from file 
print(file1.read()) 
# Closing a file
file1.close() 

# Creating a File
# Open function to open the file "myfile.txt" 
# (same directory) in append mode and store 
# it's reference in the variable file1 
file1 = open("myfile.txt", "a") 
# Writing to file 
file1.write("\nWriting to file :)") 
# Closing file 
file1.close() 

# Open function to open the file "MyFile1.txt"   
# (same directory) in append mode  and store 
# it's reference in the variable file1 
file1 = open("myfile.txt","w+")  

# Reading from File
    
# Creating a file  
file1 = open("myfile.txt", "w")  
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]  
    
# Writing data to a file  
file1.write("Hello \n")   
file1.writelines(L)  
file1.close()  # to change file access modes  
    
file1 = open("myfile.txt", "r+")  
    
print("Output of Read function is ")  
print(file1.read())  
print()  

# Append vs write mode 
file1 = open("myfile.txt","w") 
L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
file1.close() 
  
# Append-adds at last 
file1 = open("myfile.txt","a")#append mode 
file1.write("Today \n") 
file1.close() 
  
file1 = open("myfile.txt","r") 
print "Output of Readlines after appending"
print file1.readlines() 
print
file1.close() 
  
# Write-Overwrites 
file1 = open("myfile.txt","w")#write mode 
file1.write("Tomorrow \n") 
file1.close() 
  
file1 = open("myfile.txt","r") 
print "Output of Readlines after writing"
print file1.readlines() 
print
file1.close() 

# Program to show various ways to 
# write data to a file using with statement 
  
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"] 
  
# Writing to file 
with open("myfile.txt", "w") as file1: 
    # Writing data to a file 
    file1.write("Hello \n") 
    file1.writelines(L) 
  
# Reading from file 
with open("myfile.txt", "r+") as file1: 
    # Reading form a file 
    print(file1.read()) 


# Python append to a file

# With statement
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"] 
  
# Writing to file 
with open("myfile.txt", "w") as file1: 
    # Writing data to a file 
    file1.write("Hello \n") 
    file1.writelines(L) 
  
# Appending to file 
with open("myfile.txt", 'a') as file1: 
    file1.write("Today") 
  
# Reading from file 
with open("myfile.txt", "r+") as file1: 
    # Reading form a file 
    print(file1.read()) 
