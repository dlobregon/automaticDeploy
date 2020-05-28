import json
import shutil
import subprocess

# This script works with the "buildReactWebsite.py" script and the "buildBackend.py" script.
# The algorithm has the following steps:
# 0- Open the configuration file.
# 1- Execute the buildReactWebsite.py script
# 2- Execute the buildBackend.py script
# 3- Compress the output folder.
# 6- Upload the build output file to the server

############ Step No.0  ###########

with open('websiteConfig.json', 'r') as myfile:
    data=myfile.read()
configFile=json.loads(data)
myfile.close()
# declaring variables
outputFolder = str(configFile["outputFolder"])
deploymentFolder=str(configFile["deploymentFolder"])
sshKey=str(configFile["sshKey"])
remoteUser=str(configFile["remoteUser"])
remoteHost=str(configFile["remoteHost"])

############ Step No.1  ###########
print("------------------ Executing the 'buildReactWebsite.py' script ------------------")
bashInstructions="python buildReactWebsite.py"
with subprocess.Popen([bashInstructions], stdout=subprocess.PIPE,shell=True) as proc:
    print(proc.stdout.read().decode("utf-8"))


############ Step No.2  ###########
print("------------------ Executing the 'buildBackend.py' script ------------------")
bashInstructions="python buildBackend.py"

with subprocess.Popen([bashInstructions], stdout=subprocess.PIPE,shell=True) as proc:
    print(proc.stdout.read().decode("utf-8"))

############ Step No.3  ###########
print("------------------ Compressing the output folder ------------------")
bashInstructions="cd "+ deploymentFolder+" && tar -czvf deploymentPmpro.tar.gz preparedFiles/"
with subprocess.Popen([bashInstructions], stdout=subprocess.PIPE,shell=True) as proc:
    print(proc.stdout.read().decode("utf-8"))


############ Step No.4 uploading the output folder  ###########
print("------------------ Uploading the build output file to the server ------------------")
bashInstructions="scp -i "+ sshKey+" "+deploymentFolder+"deploymentPmpro.tar.gz " +remoteUser+"@"+remoteHost+":~"
with subprocess.Popen([bashInstructions], stdout=subprocess.PIPE,shell=True) as proc:
    print(proc.stdout.read().decode("utf-8"))    

print("------------------ The process is finished ------------------")
