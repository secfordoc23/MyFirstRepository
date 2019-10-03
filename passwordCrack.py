import hashlib

counter = 1

pass_input = input("Please Enter the raw MD5 hash: ")
pwFile = input("Enter in the password file name: ")
try:
    pwFile = open(pwFile, "r")
except:
    print ("\nFile Not Found!")
    quit()

for password in pwFile:
    filemd5 = hashlib.md5((password.strip()).encode()).hexdigest() #md5.new(password.strip()).hexdigest()
    print ("Trying password number %d: %s " % (counter, password.strip()))
    counter +=1

    if pass_input == filemd5:
        print ("\nMatch Found. \n Password is: %s " % password)
        break
else:
        print ("\nPassword not Found!")
    
