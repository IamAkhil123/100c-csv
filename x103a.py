#!python3

<<<<<<< HEAD
def getData(x):
  return str(x)
=======
def getData(): 
 f = open("data.csv", "r")
 return str((f.read()))

x = getData()
print(x)
>>>>>>> 44025dd4e921d4e157b0e503b3c3a8cf2d83d34e

"""
Create a function called getData()
getData takes no input parameters
return: file contents as a string

def getData():
    return data

def main():
    data = getData()
    assert "list" in str(type(db))
    assert "list" in str(type(db[0]))
    assert "Placed in Service" in data[0] == True
    assert "MAC 6c299551c1b5" in data[33] == True    
    assert data.find("No.,Equipment Item N") == 0
    assert data.find("Barry") == 27089

if __name__ == "__main__":
    main()
"""
<<<<<<< HEAD
=======

>>>>>>> 44025dd4e921d4e157b0e503b3c3a8cf2d83d34e
