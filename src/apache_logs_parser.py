import re
import sys
from collections import Counter
from humanize import naturalsize

# Regular expression for parsing Combined Log Format
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<resource>\S+) (?P<protocol>\S+)" '
    r'(?P<status>\d+) (?P<size>\S+) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
)

def parse_log_line(line):
    """Parses a single log line and returns a dictionary of values."""
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    data = match.groupdict()
    data["size"] = int(data["size"]) if data["size"].isdigit() else 0
    data["status"] = int(data["status"])
    return data

def analyze_log_file(log_file_path):
    """Analyzes the log file and prints statistics."""
    total_requests = 0
    total_data = 0
    resource_counter = Counter()
    host_counter = Counter()
    status_counter = Counter()
    skipped_lines = []
    
    with open(log_file_path, "r", encoding="utf-8") as file:
        for line in file:
            data = parse_log_line(line)
            if not data:
                skipped_lines.append(line.strip())
                continue
            
            total_requests += 1
            total_data += data["size"]
            resource_counter[data["resource"]] += 1
            host_counter[data["ip"]] += 1
            status_counter[data["status"]] += 1
    
    if total_requests == 0:
        print("No valid log entries found.")
        return
    
    most_requested_resource, resource_requests = resource_counter.most_common(1)[0]
    most_active_host, host_requests = host_counter.most_common(1)[0]
    
    print("--- Log File Analysis ---")
    print(f"Total Requests: {total_requests}")
    print(f"Total Data Transmitted: {naturalsize(total_data, binary=True)}")
    print(f"Most Requested Resource: {most_requested_resource}")
    print(f"Total Requests for {most_requested_resource}: {resource_requests}")
    print(f"Percentage of Requests for {most_requested_resource}: {resource_requests / total_requests * 100:.10f}")
    print(f"Remote Host with the Most Requests: {most_active_host}")
    print(f"Total Requests from {most_active_host}: {host_requests}")
    print(f"Percentage of Requests from {most_active_host}: {host_requests / total_requests * 100:.10f}")
    
    print("\nHTTP Status Code Distribution:")
    for category in [100, 200, 300, 400, 500]:
        category_count = sum(count for status, count in status_counter.items() if category <= status < category + 100)
        print(f"Percentage of {category}xx requests: {category_count / total_requests * 100:.10f}")
    
    if skipped_lines:
        print("\nSkipped Lines:",len(skipped_lines))
        for line in skipped_lines:
            print(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_parser.py <log_file>")
        sys.exit(1)
    analyze_log_file(sys.argv[1])
