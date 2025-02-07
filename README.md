# Apache Log Analyzer

## Overview
This project provides a tool to analyze Apache web server logs in the [Combined Log Format](http://fileformats.archiveteam.org/wiki/Combined_Log_Format). The script processes a given log file and extracts useful statistics such as:

- Total number of requests
- Total data transmitted
- Most requested resource
- Remote host with the most requests
- Percentage distribution of HTTP response status codes

The tool ensures that any malformed log entries are ignored, allowing for robust log analysis.

## Prerequisites
Before running the script, ensure you have the following installed on your system:

- **Python 3.7+**: The script is compatible with Python 3.7 and above. You can check your Python version using:
  ```sh
  python3 --version
  ```
- **Pip**: Ensure `pip` is installed for managing dependencies:
  ```sh
  python3 -m ensurepip --default-pip
  ```
  
## Understanding the Assignment
The goal of the assignment is to develop a script that can parse and analyze web server logs efficiently. It should handle errors gracefully, extract meaningful statistics, and provide insightful reports about traffic patterns.

## Approach
1. **Parsing Log Data:**
   - Use regular expressions to extract relevant fields from each log entry.
   - Validate and process each entry for meaningful statistics.
   
2. **Counting and Aggregating Data:**
   - Track total requests and data transferred.
   - Use Python's `Counter` class to determine the most requested resource and most active remote host.
   - Categorize HTTP response status codes (1xx, 2xx, 3xx, 4xx, 5xx).

3. **Error Handling:**
   - If a log line does not match the expected format, it is skipped.
   - The script ensures meaningful output even if some data is missing.

## Why Python?
Python was chosen because of:
- **Built-in regex support** (`re` module) for efficient log parsing.
- **Powerful data structures** (`Counter` from `collections`) for quick aggregation.
- **Ease of text processing** for log file handling.
- **Libraries like `humanize`** to display data sizes in a human-readable format.

## Script Details
The core logic of the script (`src/apache_logs_parser.py`) includes:
- **`parse_log_line(line)`**: Extracts data fields from a log entry.
- **`analyze_log_file(log_file_path)`**: Reads a log file, processes entries, and computes statistics.
- **Command-line interface**: Allows the script to be run with different log files as input.

## Steps to Execute
### **1. Setup Virtual Environment and Install Dependencies**
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip3 install -r src/requirements.txt
```

### **2. Generate Sample Logs (Optional)**
If you want to generate test logs, you can use the provided script:
```sh
pip3 install -r scripts/requirements.txt
./scripts/generate-logs.py -f examples/generated.log
```

### **3. Run the Log Analyzer**
You can parse your logs using below command 
```sh
python3 log_parser.py <log_file>
```

Example:
```sh
python3 src/apache_logs_parser.py examples/example1.log # Example
```

## Example Output
```
--- Log File Analysis ---
Total Requests: 9999
Total Data Transmitted: 2.6 GiB
Most Requested Resource: /favicon.ico
Total Requests for /favicon.ico: 807
Percentage of Requests for /favicon.ico: 8.0708070807
Remote Host with the Most Requests: 66.249.73.135
Total Requests from 66.249.73.135: 482
Percentage of Requests from 66.249.73.135: 4.8204820482

HTTP Status Code Distribution:
Percentage of 100xx requests: 0.0000000000
Percentage of 200xx requests: 91.7091709171
Percentage of 300xx requests: 6.0906090609
Percentage of 400xx requests: 2.1702170217
Percentage of 500xx requests: 0.0300030003

Skipped Lines: 1
46.118.127.106 - - [20/May/2015:12:05:17 +0000] "GET /scripts/grok-py-test/configlib.py HTTP/1.1" 200 235 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html
```

## Future Enhancements
- **Support for different log formats** (e.g., Nginx logs)
- **Exporting results to a database**
- **Visualization of traffic trends using a dashboard**
- **We can automate this process on cloud. I have created one example architecture using AWS services**

   ![Alt text](img/apache_logs_processing.jpeg?raw=true "Apache Log Processor")


## Conclusion
This project successfully analyzes Apache logs, providing key insights into web server traffic. It efficiently handles log parsing, aggregation, and error handling while maintaining performance and accuracy.

