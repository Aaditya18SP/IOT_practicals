def dec_to_bin(num):
    binary_num=""
    while(num>1):
        print("num %2 :" ,num%2)
        binary_num +=str(num%2)
        num=num//2
        print(num)

    if(num==1):
        binary_num += str(num)

    return binary_num

choice =2
while(choice>0):
    choice=int(input("Choose 1 to continue, 0 to exit:"))
    if(choice == 1):
        dec_num=int(input("Enter a decimal number:"))
        print("the binary number is:",dec_to_bin(dec_num))
    if( choice==0 ):
        break
    


        
