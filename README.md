# Melissa - Profiler Object Windows Python3

## Purpose

This code showcases the Melissa Profiler Object using Python3

Please feel free to copy or embed this code to your own project. Happy coding!

For the latest Melissa Profiler Object release notes, please visit: https://releasenotes.melissa.com/on-premise-api/profiler-object/

For further details, please visit: https://docs.melissa.com/on-premise-api/profiler-object/profiler-object-quickstart.html

The console will ask the user for:

- A csv that contains data that you would like to profile

And return 

- TableRecordCount
- ColumnCount
- ExactMatchDistinctCount
- ExactMatchDupesCount
- ExactMatchLargestGroup
- ContactMatchDistinctCount
- ContactMatchDupesCount
- ContactMatchLargestGroup
- HouseholdMatchDistinctCount
- HouseholdMatchDupesCount
- HouseholdMatchLargestGroup
- AddressMatchDistinctCount
- AddressMatchDupesCount
- AddressMatchLargestGroup
- States and Counts
- Postal Patterns and Counts

## Tested Environments

- Windows 64-bit Python 3.8.7
- Powershell 5.1
- Melissa data files for 2024-01

## Required File(s) and Programs


#### Binaries
This is the c++ code of the Melissa Object.

- mdProfiler.dll

#### Data File(s)
- mdProfiler.dat
- mdProfiler.mc
- mdProfiler.cfg


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

This project is compatible with Python3

#### Install the Python3
Before starting, make sure that Python3 has been correctly installed on your machine and your environment paths are configured. 

You can download Python here: 
https://www.python.org/downloads/

To set up your Path to correctly to use the python3 command, execute the following steps:
1) Run Powershell as an administrator 
2) Execute the command: 
`New-Item -ItemType SymbolicLink -Path "Link" -Target "Target"`

    where "Target" is the path to py.exe (by default this should be "C:\Windows\py.exe")\
    and "Link" is the path to py.exe, but "py.exe" is replaced with "python3.exe"\
    For Example:\
    `New-Item -ItemType SymbolicLink -Path "C:\Windows\python3.exe" -Target "C:\Windows\py.exe"`

If you are unsure, you can check by opening a command prompt window and typing the following:
`python3 --version`

![alt text](/screenshots/python_version.PNG)

If you see the version number then you have installed Python3 and set up your environment paths correctly!

----------------------------------------

#### Set up Powershell settings

If running Powershell for the first time, you will need to run this command in the Powershell console: `Set-ExecutionPolicy RemoteSigned`.
The console will then prompt you with the following warning shown in the image below. 
 - Enter `'A'`. 
 	- If successful, the console will not output any messages. (You may need to run Powershell as administrator to enforce this setting).
	
 ![alt text](/screenshots/powershell_executionpolicy.png)

----------------------------------------

#### Download this project
```
$ git clone https://github.com/MelissaData/ProfilerObject-Python3
$ cd ProfilerObject-Python3
```

#### Set up Melissa Updater 

Melissa Updater is a CLI application allowing the user to update their Melissa applications/data. 

- Download Melissa Updater here: <https://releases.melissadata.net/Download/Library/WINDOWS/NET/ANY/latest/MelissaUpdater.exe>
- Create a folder within the cloned repo called `MelissaUpdater`.
- Put `MelissaUpdater.exe` in `MelissaUpdater` folder you just created.

----------------------------------------

#### Different ways to get data file(s)
1.  Using Melissa Updater
	- It will handle all of the data download/path and dll(s) for you. 
2.  If you already have the latest release (ZIP), you can find the data file(s) and dll(s) in there
	- Use the location of where you copied/installed the data and update the "$DataPath" variable in the powershell script.
	- Copy all the dll(s) mentioned above into the `MelissaProfilerObjectWindowsPython3` project folder.
	

## Run Powershell Script
Parameters:
- -file: a test csv file
 	
  This is convenient when you want to get results for a specific csv file in one run instead of testing multiple csv files in interactive mode.

- -license (optional): a license string to test the Profiler Object
- -quiet (optional): add to the command if you do not want to get any console output from the Melissa Updater

  When you have modified the script to match your data location, let's run the script. There are two modes:
- Interactive 

	The script will prompt the user for a csv file, then use the provided inputs to test Profiler Object. For example:
	```
	$ .\MelissaProfilerObjectWindowsPython3.ps1
	```
    For quiet mode:
    ```
    $ .\MelissaProfilerObjectWindowsPython3.ps1 -quiet
    ```
- Command Line 

	You can pass a csv file and a license string into the ```-file``` and ```-license``` parameters respectively to test Profiler Object. For example:
    ```
    $ .\MelissaProfilerObjectWindowsPython3.ps1 -file "MelissaProfilerObjectSampleInput.csv"
    $ .\MelissaProfilerObjectWindowsPython3.ps1 -file "MelissaProfilerObjectSampleInput.csv" -license "<your_license_string>"
    ```

	For quiet mode:
    ```
    $ .\MelissaProfilerObjectWindowsPython3.ps1 -file "MelissaProfilerObjectSampleInput.csv"  -quiet
    $ .\MelissaProfilerObjectWindowsPython3.ps1 -file "MelissaProfilerObjectSampleInput.csv"  -license "<your_license_string>" -quiet
    ```
This is the expected output from a successful setup for interactive mode:

![alt text](/screenshots/output.png)

    
## Troubleshooting

Troubleshooting for errors found while running your program.

### Errors:

| Error      | Description |
| ----------- | ----------- |
| ErrorRequiredFileNotFound      | Program is missing a required file. Please check your Data folder and refer to the list of required files above. If you are unable to obtain all required files through the Melissa Updater, please contact technical support below. |
| ErrorFoundOldFile   | File(s) are out of date. Please make sure you are downloading and using the latest release version. (If using the Melissa Updater, check powershell script for '$RELEASE_VERSION = {version}'  and change the release version if you are using an out of date release).    |
| ErrorLicenseExpired   | Expired license string. Please contact technical support below. |


## Contact Us

For free technical support, please call us at 800-MELISSA ext. 4
(800-635-4772 ext. 4) or email us at tech@melissa.com.

To purchase this product, contact Melissa sales department at
800-MELISSA ext. 3 (800-635-4772 ext. 3).
