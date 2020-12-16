def main():
    def welcome(): # welcome function
        print("==================================================================================")
        print("Hi this is a Cryptograph encoder which u can use to Encrypt or Decrypt messages")
        print("==================================================================================")
    welcome()

    def get_msg_and_choice():
        global decis #making the variable global
        decis=str(input("Please enter 'E' if you want to Encrypt a message or 'D' if you want to Decode the message: ")).upper()
        print("==================================================================================")
        msg=str(input("Please Enter the message you want to encrypt or Decrypt: "))
        print("==================================================================================")
        global y
        y=[]
        y= list(msg) # converting the input message into a list of characters
        global list_length
        list_length=len(y) #getting the length of the list

        #return y

    get_msg_and_choice() #calling the function

    def code_it():#for coding the message
        for i in range(len(y)):
            a=ord(y[i])# getting the ascii value
            m=(a+85)%128# using numbers to add to ascii
            print(chr(m),end="") #converting ASCII value to character


    def decode_it():# for decoding the message
        for i in range(len(y)):
            a=ord(y[i])#getting the Ascii Value
            m=(a-85)%128 #using mathematical operation to convert it to its original Form
            print(chr(m),end="") #converting ascii to char and printing it in same line

    def output():
        if (decis == 'D'):
            print("This is the Decrypted Message Copy this")
            print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
            decode_it()
        if (decis == 'E'):  # checking if the user wants to encode it
            print("This is the Encrypted Message Copy this")
            print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
            code_it()
    output()
main() # calling the main function

