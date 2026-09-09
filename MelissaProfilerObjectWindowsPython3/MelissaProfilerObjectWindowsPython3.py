"""
The Profiler Object is a data quality tool that provides statistical analysis
and assessment of your data quality needs for consistency, uniqueness and correctness.

High-level flow of this sample:
  1. SETUP     - create an mdProfiler instance, license it, configure the analyses and
                 output file, point it at the data files, then InitializeDataFiles().
  2. INPUT     - define the columns (AddColumn), then read a CSV file and feed each
                 row in with SetColumn + AddRecord.
  3. PROCESS   - ProfileData() analyzes the whole table.
  4. READ      - pull table-level statistics with the GetTable* getters, and per-column
                 value/pattern distributions with the frequency iterators.
  5. CLEANUP   - the wrapper releases the object when it goes out of scope (it defines
                 __del__); there is no explicit Dispose() in the Python wrapper.

The pieces in this file map onto that flow:
  - run_as_console / parse_arguments : console harness (argument parsing + the interactive loop).
  - ProfilerObject                   : thin wrapper around mdProfiler (setup + the profiling sequence).
  - DataContainer                    : holds the input file path and a small path-wrapping helper.

Where mdProfiler comes from:
  The mdProfiler class lives in mdProfiler_pythoncode.py, a generated Python wrapper over
  mdProfiler.dll that the accompanying MelissaProfilerObjectWindowsPython3.ps1 script
  downloads on every run.

Reference:
  Quickstart    : https://docs.melissa.com/on-premise-api/profiler-object/profiler-object-quickstart.html
  Release notes : https://releasenotes.melissa.com/on-premise-api/profiler-object/
  Result codes  : https://docs.melissa.com/on-premise-api/profiler-object/result-codes.html
"""

import mdProfiler_pythoncode
import os
import sys
import json


class DataContainer:
    """Holds the input file path for one pass, plus a small display helper (get_wrapped
    wraps a long path so it prints neatly across several lines)."""
    def __init__(self, input_file="", result_codes=[]):

        # Input: path to the CSV file to profile.
        self.input_file = input_file

        # Output: result codes (unused in this sample).
        self.result_codes = result_codes

    def get_wrapped(self, path, max_line_length):
        """
        Splits a long file path into chunks no longer than max_line_length so it prints
        neatly across several lines in the console output. Display-only helper.
        """
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
    """
    Wrapper that owns a single Melissa Profiler Object instance and encapsulates the two
    things every Melissa object needs: one-time setup (license + config + data files) and
    the per-file profiling sequence. Reuse one instance; do NOT re-initialize per file.
    """
    def __init__(self, license, data_path):
        """
        Perform the mandatory one-time setup, in this required order:
          1. SetLicenseString               - authorize the object.
          2. SetFileName / SetAppendMode    - choose the profiler output file and write mode.
          3. SetPathToProfilerDataFiles     - tell it where the data files live.
          4. Set*Analysis / SetDataAggregation - choose which analyses to run (1 = on).
          5. InitializeDataFiles            - load the data into memory.

        Args:
            license: The Melissa license string used to authorize the object.
            data_path: Path to the folder containing the Profiler Object data files.
        """
        # Set license string and set path to data files
        # The underlying Melissa Profiler Object instance.
        self.md_profiler_obj = mdProfiler_pythoncode.mdProfiler()

        # Path to the Profiler Object data files.
        self.data_path = data_path

        self.md_profiler_obj.SetLicenseString(license)
        self.md_profiler_obj.SetFileName("testFile.prf")
        self.md_profiler_obj.SetAppendMode(mdProfiler_pythoncode.AppendMode.Overwrite)

        self.md_profiler_obj.SetPathToProfilerDataFiles(data_path)

        # Enable each analysis the profiler runs. The default is 1 for all four.
        self.md_profiler_obj.SetSortAnalysis(1)

        # The default is 1
        self.md_profiler_obj.SetMatchUpAnalysis(1)

        # The default is 1
        self.md_profiler_obj.SetRightFielderAnalysis(1)

        # The default is 1
        self.md_profiler_obj.SetDataAggregation(1)

        # Load the data files. The returned ProgramStatus reports whether initialization succeeded.
        # If you see a different date than expected, check your license string and either download the new data files
        # or use the Melissa Updater program to update your data files.
        p_status = self.md_profiler_obj.InitializeDataFiles()

        # If an issue occurred, please investigate the common causes.
        # Common causes: an invalid/expired license, or missing/wrong-path data files.
        if (p_status != mdProfiler_pythoncode.ProgramStatus.ErrorNone):
            print("Failed to Initialize Object.")
            print(p_status)
            return

        # Diagnostic information, handy for confirming the object loaded the data you expect:

        # Build date of the data files
        print(f"                               DataBase Date: {self.md_profiler_obj.GetDatabaseDate()}")

        # When the license stops working
        print(f"                             Expiration Date: {self.md_profiler_obj.GetLicenseExpirationDate()}")

        # This number should match with the file properties of the Melissa Object binary file.
        # If TEST appears with the build number, there may be a license key issue.
        print(f"                              Object Version: {self.md_profiler_obj.GetBuildNumber()}\n")


    def execute_object_and_result_codes(self, data):
        """
        Run the full Profiler analysis for one input file. This is the canonical call
        pattern to copy into your own application:
          AddColumn (define the schema) -> StartProfiling -> per row SetColumn + AddRecord
          -> ProfileData (analyze the table).

        Args:
            data: The record holder; its input file is the CSV file to profile.
        """
        # Define the table schema: one AddColumn per column, naming it and declaring the kind
        # of data it holds so the object knows how to profile each one.
        self.md_profiler_obj.AddColumn("first", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeFirstName)
        self.md_profiler_obj.AddColumn("last", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeLastName)
        self.md_profiler_obj.AddColumn("address", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeAddress)
        self.md_profiler_obj.AddColumn("city", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeCity)
        self.md_profiler_obj.AddColumn("state", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeStateOrProvince)
        self.md_profiler_obj.AddColumn("zip", mdProfiler_pythoncode.ProfilerColumnType.ColumnTypeVariableUnicodeString, mdProfiler_pythoncode.ProfilerDataType.DataTypeZipOrPostalCode)

        # Read the whole CSV input file into memory (one string per line).
        try:
            records = open(data.input_file, 'r', encoding='utf-8').readlines()
        except Exception as e:
            print(f"Error: Unable to open the input file\n{e}")
            exit(1)

        # Begin a profiling session, then feed every row in below.
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

        # All rows added; analyze the full table.
        self.md_profiler_obj.ProfileData()

        # ResultsCodes explain any issues Profiler Object has with the object.
        # List of result codes for Profiler Object
        # https://docs.melissa.com/on-premise-api/profiler-object/result-codes.html



def parse_arguments():
    """
    Read the supported command-line options and return them as a (license, test_file,
    data_path) tuple.

    Recognized flags (each followed by its value):
      --license / -l   : the Melissa license string
      --file / -f      : path to the CSV file to profile in one-shot mode
      --dataPath / -d  : path to the Profiler Object data files

    Returns:
        A (license, test_file, data_path) tuple, each entry empty when its flag
        was not supplied.
    """
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
    """
    Set up the Profiler Object once, then drive the input -> process -> output cycle.

    In interactive mode (no --file) it loops, asking for a file path each pass until the
    user answers "N". In one-shot mode (--file supplied) it runs a single pass and exits.

    Args:
        license: The Melissa license string used to initialize the object.
        test_file: A CSV file to profile in one-shot mode; if empty, the program prompts
            interactively.
        data_path: Path to the Profiler Object data files.
    """
    print("\n\n================ WELCOME TO MELISSA PROFILER OBJECT WINDOWS PYTHON3 =================\n")

    # Construct the wrapper. This is where the object is licensed, configured, pointed
    # at the data files, and initialized (see the ProfilerObject constructor above).
    profiler_object = ProfilerObject(license, data_path)

    should_continue_running = True

    # Gate the program on a successful initialization. If the data files could not be
    # loaded (bad/expired license, missing or wrong-path data files, ...),
    # GetInitializeErrorString() returns the reason instead of "No error." and we skip
    # the processing loop entirely.
    if profiler_object.md_profiler_obj.GetInitializeErrorString() != "No error.":
      should_continue_running = False

    while should_continue_running:
        if test_file == None or test_file == "":
          # Interactive mode: prompt the user for a file path.
          print("\nFill in each value to see the Profiler Object results")
          input_file = str(input("File Path: "))
        else:
          # One-shot mode: use the file path passed on the command line.
          input_file = test_file

        # Holder for this pass's input file path.
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
        # Profiles the input file; the statistics are then read from the object below.
        profiler_object.execute_object_and_result_codes(data)

        # Print output
        # The output has two parts: table-level statistics (record/column counts and
        # duplicate analysis) read via GetTable* getters, then per-column frequency
        # distributions read with the iterator pattern further below.
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

        # STATE Iterator Example - walk the value-frequency list for the "state" column:
        # StartDataFrequency opens the iterator, GetDataFrequencyValue/Count read the current
        # entry, and GetNextDataFrequency advances until it returns something other than 1.
        print("                              STATE Value                 Count")
        profiler_object.md_profiler_obj.StartDataFrequency("state", mdProfiler_pythoncode.Order.OrderCountAscending)
        while profiler_object.md_profiler_obj.GetNextDataFrequency("state") == 1:
            print(f"                                   {profiler_object.md_profiler_obj.GetDataFrequencyValue('state'):16}{profiler_object.md_profiler_obj.GetDataFrequencyCount('state'):10}")
        print("")

        # POSTAL Iterator Example - StartPatternFrequency
        # reports the frequency of value *patterns* (e.g. ZIP formats) for the "zip" column.
        print("                              POSTAL Pattern              Count")
        profiler_object.md_profiler_obj.StartPatternFrequency("zip", mdProfiler_pythoncode.Order.OrderCountAscending)

        print(f"                                   {profiler_object.md_profiler_obj.GetPatternFrequencyValue('zip'):16}{profiler_object.md_profiler_obj.GetPatternFrequencyCount('zip'):10}")

        while profiler_object.md_profiler_obj.GetNextPatternFrequency("zip") == 1:
            print(f"                                   {profiler_object.md_profiler_obj.GetPatternFrequencyValue('zip'):16}{profiler_object.md_profiler_obj.GetPatternFrequencyCount('zip'):10}")


        is_valid = False

        # In one-shot mode there is nothing more to do after a single pass: mark the
        # input handled and stop the outer loop.
        if not (test_file == None or test_file == ""):
            is_valid = True
            should_continue_running = False
        # Interactive mode: ask whether to process another file. Keep prompting until we
        # get a valid Y/N. "N" ends the program; "Y" falls through to another pass.
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



# ---------------------------- MAIN STARTS HERE ----------------------------

# Read the optional command-line arguments, then hand control to run_as_console, which
# performs the actual Profiler Object setup and processing.
license, test_file, data_path = parse_arguments()

run_as_console(license, test_file, data_path)
