#!python3

"""
Create a function called getData()
getData takes no input parameters
return: file contents as a string

"""
def getData():
    return data

def main():
    data = getData()
    assert "list" in str(type(db))
    assert "list" in str(type(db[0]))
    assert data.find("No.,Equipment Item N") == 0
    assert data.find("Barry") == 27089

if __name__ == "__main__":
    main()

