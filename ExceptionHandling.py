try:
    import sys
    print("Imported successfully")
    list=[2,3,4,5,6,7]
    print(list[6])
except (ImportError):
    print("This library does not exist")
except (IndexError):
    print("Index out of bounds")
