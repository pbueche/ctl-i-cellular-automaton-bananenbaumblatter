import numpy as np
import sys
import re

# 1. within vscode: Create new file named speedtest.py, copy & paste content of this website into it, and save it.
# 2. Execute this file using python (press the triangle)

print("\nNote: If it freezes: Stop execution by clicking on the red square (top right in vscode). Open settings: Wheel (bottom left) -> Settings -> search code runner -> goto : Code-runner: Run In Terminal -> check the box -> go back to your python file (click on the python file name) -> excute your python file again. For all other problems see the CTL-FAQ pages.\n")

answer = input("Are you running vscode [y/n]?")

if any(answer.lower() == f for f in ["yes","y"]):
    print("excellent")
else:
    print("Please start vscode. Open your GitHub classroom in vscode. Add a new file speedtest.py and paste the present file content into it. Save the file, and start it again.")
    sys.exit()

if "speedtest.py" not in sys.argv[0]:
    print("save this file as speedtest.py and start over"); sys.exit()

if "ctl-" not in sys.argv[0]:
    print("save this file as speedtest.py in your github classroom repository and start over"); sys.exit()

answer = input("Did you click the GitHub symbol and see your classroom files [y/n]? ")
if any(answer.lower() == f for f in ["yes","y"]):
    print("excellent")
else:
    print("Please start vscode. Open your GitHub classroom in vscode. Add a new file and paste the present file content into it. Save the file, and start it again.")
    sys.exit()

GithubName = str(input("Enter your GitHub user name: "))    # wait for input
GithubName = re.sub(r"\s+","",GithubName)                   # erase blanks
GithubName = GithubName.lower()                             # convert to lower case

ans = []
ans.append(input("Question 1/3: How much time did you spend with installing vscode+python+git+extensions? [a single line of free text] "))
ans.append(input("Question 2/3: Did your group test the live share feature and did it work? [a single line of free text] "))
ans.append(input("Question 3/3: Did your group start writing the code for our first project [a single line of free text] "))

filename = "answer-"+GithubName+".txt"
text_file = open(filename,"w")
text_file.write(ans[0]+"\n")
text_file.write(ans[1]+"\n")
text_file.write(ans[2]+"\n")
text_file.close()

print("\nBy now, you should have created a new file named "+filename+" in your current folder. Check, if it exists.")
print("If so, delete speedtest.py and afterwards commit your change to upload the new "+filename+" to your GitHub repository.")
print("Once this lecture is over, you can also remove the answer*.txt files from your directory.")y