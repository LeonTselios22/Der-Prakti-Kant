Name = input("Geben Sie ihren Namen ein: ")
print("Name is: " + Name)



Alter = input("Geben Sie ihr Alter ein: ")
print("Alter is: " + Alter)




username = input("Geben Sie ihren Usernamen ein: ")
print("Username is: " + username)


print("\nZusammenfassung:")
print("Name: " + Name)
print("Alter: " + Alter)
print("Username: " + username)



f = open("Kundendaten.txt", "w")



datei = open('Kundendaten.txt','a')

datei.write(" \nName " + Name)

datei.write(" \nAlter " + Alter)

datei.write(" \nUsername " + username)

# Sehr guter Code!


#     __.------~~~-.
#   ,'/             `\
#   " \  ,..__ | ,_   `\_,
#      >/|/   ~~\||`\(`~,~'
#      | `\     /'|   \_;
#        "   "   "


      

