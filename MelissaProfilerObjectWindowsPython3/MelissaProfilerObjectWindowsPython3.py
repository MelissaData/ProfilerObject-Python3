import mdProfiler_pythoncode
import os
import sys
import json


class DataContainer:
    def __init__(self, input_file="", result_codes=[]):
        self.input_file = input_file
        self.result_codes = result_codes

    def get_wrapped(self, path, max_line_length):
        file = f"{os.getcwd()}\{path}"
        file_parts = file.split(os.sep)
        
        current_line = ""
        wrapped_strings = []

        for section in file_parts:
            if len(current_line + section) > max_line_length:
                wrapped_strings.append(current_line.strip())
                current_line = ""

            if section == file:
                current_line += section
            else:
                current_line += section + os.sep

        if len(current_line) > 0:
            wrapped_strings.append(current_line.strip())

        return wrapped_strings


class ProfilerObject:
    """ Set license string and set path to data files  (.dat, etc) """
    def __init__(self, license, data_path):
        self.md_profiler_obj = mdProfiler_pythoncode.mdProfiler()
        self.data_path = data_path

        """
        If you see a different date than expected, check your license string and either download the new data files or use the Melissa Updater program to update your data files.  
        """

        self.md_profiler_obj.SetLicenseString(license)
        self.md_profiler_obj.SetFileName("testFile.prf")
        self.md_profiler_obj.SetAppendMode(mdProfiler_pythoncode.AppendMode.Overwrite)

        self.md_profiler_obj.SetPathToProfilerDataFiles(data_path)

        self.md_profiler_obj.SetSortAnalysis(1)  # the default is 1
        self.md_profiler_obj.SetMatchUpAnalysis(1) # the default is 1
        self.md_profiler_obj.SetRightFielderAnalysis(1) # the default is 1
        self.md_profiler_obj.SetDataAggregation(1) # the default is 1

        # If you see a different date than expected, check your license string and either download the new data files or use the Melissa Updater program to update your data files.  
        p_status = self.md_profiler_obj.InitializeDataFiles()


        if (p_status != mdProfiler_pythoncode.ProgramStatus.ErrorNone):
            print("Failed to Initialize Object.")
            print(p_status)
            return
        
        print(f"                               DataBase Date: {self.md_profiler_obj.GetDatabaseDate()}")
        print(f"                             Expiration Date: {self.md_profiler_obj.GetLicenseExpirationDate()}")
      
        """
        This number should match with file properties of the Melissa Object binary file.
        If TEST appears with the build number, there may be a license key issue.
        """
        print(f"                              Object Version: {self.md_profiler_obj.GetBuildNumber()}\n")
    

    def execute_object_and_result_codes(self, data):
        self.md_profiler_obj.AddColumn("first", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeFirstName)
        self.md_profiler_obj.AddColumn("last", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeLastName)
        self.md_profiler_obj.AddColumn("address", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeAddress)
        self.md_profiler_obj.AddColumn("city", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeCity)
        self.md_profiler_obj.AddColumn("state", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeStateOrProvince)
        self.md_profiler_obj.AddColumn("zip", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeZipOrPostalCode)

        try:
            records = open(data.input_file, 'r', encoding='utf-8').readlines()
        except Exception as e:
            print(f"Error: Unable to open the input file\n{e}")
            exit(1)

        self.md_profiler_obj.StartProfiling()

        # Preparing the header for the output file.
        output = "First\tLast\tAddress\tCity\tState\tZip\tFirstResults\tLastResults\tAddressResults\tCityResults\tStateResults\tZipResults\r\n"

        # Inputting the records to the Profiler Object
        for record in records:
            fields = record.strip().split(',')
            self.md_profiler_obj.SetColumn("first", fields[0])
            self.md_profiler_obj.SetColumn("last", fields[1])
            self.md_profiler_obj.SetColumn("address", fields[2])
            self.md_profiler_obj.SetColumn("city", fields[3])
            self.md_profiler_obj.SetColumn("state", fields[4])
            self.md_profiler_obj.SetColumn("zip", fields[5])

            self.md_profiler_obj.AddRecord()

        self.md_profiler_obj.ProfileData()

        # ResultsCodes explain any issues Profiler Object has with the object.
        # List of result codes for Profiler Object
        # https://wiki.melissadata.com/index.php?title=Result_Code_Details#Profiler_Object



def parse_arguments():
    license, test_file, data_path = "", "", ""

    args = sys.argv
    index = 0
    for arg in args:
        
        if (arg == "--license") or (arg == "-l"):
            if (args[index+1] != None):
                license = args[index+1]
        if (arg == "--file") or (arg == "-f"):
            if (args[index+1] != None):
                test_file = args[index+1]
        if (arg == "--dataPath") or (arg == "-d"):
            if (args[index+1] != None):
                data_path = args[index+1]
        index += 1

    return (license, test_file, data_path)

def run_as_console(license, test_file, data_path):
    print("\n\n================ WELCOME TO MELISSA PROFILER OBJECT WINDOWS PYTHON3 =================\n")

    profiler_object = ProfilerObject(license, data_path)

    should_continue_running = True

    if profiler_object.md_profiler_obj.GetInitializeErrorString() != "No error.":
      should_continue_running = False
      
    while should_continue_running:
        if test_file == None or test_file == "":        
          print("\nFill in each value to see the Profiler Object results")
          input_file = str(input("File Path: "))
        else:        
          input_file = test_file
        
        data = DataContainer(input_file)

        # Print user input
        print("\n======================================= INPUTS ======================================\n")

        sections = data.get_wrapped(data.input_file, 50)

        print(f"\t                Input File: {sections[0]}")

        for i in range(1, len(sections)):
            if i == len(sections) - 1 and sections[i].endswith("\\"):
                sections[i] = sections[i][0:len(sections[i]) - 1]
            print(f"\t                            {sections[i]}")

        # Execute Profiler Object
        profiler_object.execute_object_and_result_codes(data)

        # Print output
        print("\n======================================= OUTPUT ======================================\n")
        print("\n                      Profiler Object Information:")
        print("\n                             TABLE STATISTICS\n\n")
        print(f"                              TableRecordCount           :  {profiler_object.md_profiler_obj.GetTableRecordCount()}")
        print(f"                              ColumnCount                :  {profiler_object.md_profiler_obj.GetColumnCount()}")
        print("")
        print(f"                              ExactMatchDistinctCount    :  {profiler_object.md_profiler_obj.GetTableExactMatchDistinctCount()}")
        print(f"                              ExactMatchDupesCount       :  {profiler_object.md_profiler_obj.GetTableExactMatchDupesCount()}")
        print(f"                              ExactMatchLargestGroup     :  {profiler_object.md_profiler_obj.GetTableExactMatchLargestGroup()}")
        print("")
        print(f"                              ContactMatchDistinctCount  :  {profiler_object.md_profiler_obj.GetTableContactMatchDistinctCount()}")
        print(f"                              ContactMatchDupesCount     :  {profiler_object.md_profiler_obj.GetTableContactMatchDupesCount()}")
        print(f"                              ContactMatchLargestGroup   :  {profiler_object.md_profiler_obj.GetTableContactMatchLargestGroup()}")
        print("")
        print(f"                              HouseholdMatchDistinctCount:  {profiler_object.md_profiler_obj.GetTableHouseholdMatchDistinctCount()}")
        print(f"                              HouseholdMatchDupesCount   :  {profiler_object.md_profiler_obj.GetTableHouseholdMatchDupesCount()}")
        print(f"                              HouseholdMatchLargestGroup :  {profiler_object.md_profiler_obj.GetTableHouseholdMatchLargestGroup()}")
        print("")
        print(f"                              AddressMatchDistinctCount  :  {profiler_object.md_profiler_obj.GetTableAddressMatchDistinctCount()}")
        print(f"                              AddressMatchDupesCount     :  {profiler_object.md_profiler_obj.GetTableAddressMatchDupesCount()}")
        print(f"                              AddressMatchLargestGroup   :  {profiler_object.md_profiler_obj.GetTableAddressMatchLargestGroup()}")

        print("\n\n                             COLUMN STATISTICS\n\n")

        # STATE Iterator Example
        # print("                                 STATE Value     Count")
        print("                              STATE Value                 Count")
        profiler_object.md_profiler_obj.StartDataFrequency("state", mdProfiler_pythoncode.Order.OrderCountAscending)
        while profiler_object.md_profiler_obj.GetNextDataFrequency("state") == 1:
            print(f"                                   {profiler_object.md_profiler_obj.GetDataFrequencyValue('state'):16}{profiler_object.md_profiler_obj.GetDataFrequencyCount('state'):10}")
        print("")

        # POSTAL Iterator Example
        print("                              POSTAL Pattern              Count")
        #print("                                      POSTAL Pattern     Count")
        profiler_object.md_profiler_obj.StartPatternFrequency("zip", mdProfiler_pythoncode.Order.OrderCountAscending)

        print(f"                                   {profiler_object.md_profiler_obj.GetPatternFrequencyValue('zip'):16}{profiler_object.md_profiler_obj.GetPatternFrequencyCount('zip'):10}")

        while profiler_object.md_profiler_obj.GetNextPatternFrequency("zip") == 1:
            print(f"                                   {profiler_object.md_profiler_obj.GetPatternFrequencyValue('zip'):16}{profiler_object.md_profiler_obj.GetPatternFrequencyCount('zip'):10}")


        is_valid = False
        if not (test_file == None or test_file == ""):
            is_valid = True
            should_continue_running = False    
        while not is_valid:
        
            test_another_response = input(str("\nTest another file? (Y/N)\n"))
            

            if not (test_another_response == None or test_another_response == ""):         
                test_another_response = test_another_response.lower()
            if test_another_response == "y":
                is_valid = True
            
            elif test_another_response == "n":
                is_valid = True
                should_continue_running = False            
            else:
            
              print("Invalid Response, please respond 'Y' or 'N'")

    print("\n====================== THANK YOU FOR USING MELISSA PYTHON3 OBJECT ===================\n")
    


"""  MAIN STARTS HERE   """

license, test_file, data_path = parse_arguments()

run_as_console(license, test_file, data_path)