import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
# Directory where the data will reside, relative to 'darknet.exe'
path_data = 'data/hedef/'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.JPEG")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    #file = open(title + '.txt', 'w')
    #file.write('0 0.5 0.5 1 1')
    #file.close()

    if counter == index_test:
        counter = 1
        file_test.write(path_data + title + '.JPEG' + "\n")
    else:
        file_train.write(path_data + title + '.JPEG' + "\n")
        counter = counter + 1




