class Employee:

    #Initializing (Constructor)
    def __init__(self):
        print("Employee created.")

    #Deleting (destructor)
    def __del__(self):
        print('Destructor called, employee deleted.')


obj = Employee()
del obj

