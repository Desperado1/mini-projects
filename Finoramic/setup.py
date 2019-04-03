import json
from setuptools import setup, find_packages
from setuptools.command.install import install


def open_json_file(json_file_path):
    arr = []
    with open(json_file_path) as file:
        data = json.load(file)
        for (i, v) in data.items():
            
            for (j, k) in enumerate(v):
                arr.append(k)
    return arr
print("enter the name of json file with .json extension or path if it in some other diretory!!")
path = str(input())
arr1 = open_json_file(path)
arr2 = []
count = 0
class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        install.run(self)
        if count==0:
        	print("success")
        else:
        	print(arr2)
for i in arr1:
	setup(
	    install_requires = i,
	    package_data={
	                # If any package contains *.txt or *.rst files, include them:
	                '': ['*.txt', '*.rst'],
	                # And include any *.msg files found in the 'hello' package, too:
	                'hello': ['*.msg'],
	                },
	    cmdclass={'install': PostInstallCommand,
    			}
	     )
	if setup == True:
		continue
	else:
		count += 1
		arr2.append(i)

