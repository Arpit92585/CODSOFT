import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
password=" "
user=int(input("Enter the length of Password "))
n_letters=int(input("enter number of letters"))
n_symbols=int(input("enter number of symbols"))
n_numbers=int(input("enter number of numbers"))
password+="".join(random.sample(letters,n_letters))
password+="".join(random.sample(symbols,n_symbols))
password+="".join(random.sample(numbers,n_numbers))
  
password=''.join(random.sample(password,len(password)))

print(f"Your Password is : {password}")
