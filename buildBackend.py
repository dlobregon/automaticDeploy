import json
import shutil
import subprocess

# The backend project is on the NodeJS/Express environment
# The algorithm has the following steps:
# 0- Open the configuration file.
# 1- Copy the project's directory to the output directory
# 2- Delete the "node-modules" folder
# 3- Replace the development configuration files file by the production configuration files

############ Step No.0  ###########

with open('websiteConfig.json', 'r') as myfile:
    data=myfile.read()
configFile=json.loads(data)
myfile.close()
# declaring variables
backendProductionFile =str(configFile["backendProductionFile"])
backendProjectLocation=str(configFile["backendProjectLocation"])
outputFolder = str(configFile["outputFolder"])
############ Step No.1 ############
print("------ Cloning the backend folder ------------------")
bashInstructions="cp -r "+backendProjectLocation+" "+outputFolder
process = subprocess.Popen(bashInstructions, 
                           stdout=subprocess.PIPE, 
                           shell=True)
for line in process.stdout:
    print(line.decode("utf-8"))

############ Step No.2 ############
print("------ Deleting the 'node-modules' ----------")
bashInstructions="rm -r "+outputFolder+"pm-pro-backend/node_modules/"
process = subprocess.Popen(bashInstructions, 
                           stdout=subprocess.PIPE, 
                           shell=True)
for line in process.stdout:
    print(line.decode("utf-8"))

############ Step No.3 ############
print("------ Replacing the development config file by the production config file ----------")
shutil.copyfile(backendProductionFile,outputFolder+"pm-pro-backend/db_config.json")
