import os
import shutil

def main():
   
    main_folder = "Characters"
    os.makedirs(main_folder, exist_ok=True)

  
    characters = ["Mickey", "Donald", "Goofy"]
    for character in characters:
        file_path = os.path.join(main_folder, f"{character}.txt")
        with open(file_path, "w") as file:
            file.write(f"{character}!")

 
    disney_folder = os.path.join(main_folder, "Disney")
    os.makedirs(disney_folder, exist_ok=True)


    mickey_file_path = os.path.join(main_folder, "Mickey.txt")
    mickey_disney_path = os.path.join(disney_folder, "Mickey.txt")
    
    with open(mickey_file_path, "r") as mickey_file:
        content = mickey_file.read()

    with open(mickey_disney_path, "w") as mickey_disney_file:
        mickey_disney_file.write(content)

if __name__ == "__main__":
    main()







      

