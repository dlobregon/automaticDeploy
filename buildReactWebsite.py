import shutil
import json 
import subprocess

# The React Project is under Rekit.js framework
# The algorithm has the following steps:
# 0- Open the configuration file
# 1- Replace the development "constants" by the productoin "constants" file
# 2- Run the Rekit's build script to build the website
# 3- Replace the production "constants"  file by the development "constants" file.

############ Step No.0  ###########

with open('websiteConfig.json', 'r') as myfile:
    data=myfile.read()
configFile=json.loads(data)
# declaring variables
productionFile= str(configFile["productionFile"])
developmentFileCopy=str(configFile["developmentFile"])
projectLocation=str(configFile["projectLocation"])

############ Step No.1 ############

# Copying the production file
print("----- Replacing the development file for the production file ---------------")

print("The project's location is %s" % projectLocation)
print("The production file is %s" % productionFile)
# replacing the developmentFile
shutil.copyfile(productionFile,projectLocation+"src/features/common/redux/constantes.js")
# executing the build command

############ Step No.2 ############
print("----- executing the build script ------------")
bashInstruction = "cd "+projectLocation+" && npm run build "
process = subprocess.Popen(bashInstruction, 
                           stdout=subprocess.PIPE, 
                           shell=True)
for line in process.stdout:
    print(line.decode("utf-8"))

############ Step No.3 ############
print("------ Replacing the production file by the development file -------------------")
shutil.copyfile(developmentFileCopy, projectLocation+"src/features/common/redux/constantes.js")
