import os # get our operative system 

def main():
    i = 0 # in relation to indexing the images in the folder
    path = "C:/Users/12/OneDrive/Documents/images/" # You will need to add the desired path of the folder you want to use 

    for filename in os.listdir(path):
        dest = "img" + str(i) + ".jpg" # My destination 
        m_source = path + filename # to name the files i.e images in the folder 
        dest = path + dest
        os.rename(m_source, dest) # Used this to rename 
        i += 1 #increment  i  by 1 

if __name__ == "__main__": # I used this if statement to make sure the program is immediately processed to call this function 
    main()