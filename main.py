
def find_anagrams():
    # [assignment] Add your code here
    string1 = input("Type in a word of your choice: ")
    string2 = input("Type in a word of your choice: ")
    
    #convert both strings to similar case(uppercase)
    string1 = string1.upper()
    string2 = string2.upper()
    
    #check the length of both strings
    if len(string1) == len(string2):
        
        #sort both strings
        if sorted(string1) == sorted(string2):
            print("True")
        else:
            print("False")
        
    else: 
        print("False")
        

    
find_anagrams()    
    
    

