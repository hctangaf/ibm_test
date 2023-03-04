input_file = []
with open("some_file.txt", 'r') as f:
    allValid = True
    errorCodes = []
    for record in f:
        allValid = record.isValid
        if record.isValid is not True:
            raise Exception('error')

    if allValid is True:
        print("Yes")
    else:
        print("No")
        print('errorCodes sepearated by space character')