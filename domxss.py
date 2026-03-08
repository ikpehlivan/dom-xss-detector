import re
import sys
import os

SOURCES = [
    "location",
    "location.href",
    "location.search",
    "location.hash",
    "document.URL",
    "document.documentURI",
    "document.referrer",
    "window.name"
]

SINKS = [
    "innerHTML",
    "outerHTML",
    "document.write",
    "document.writeln",
    "eval",
    "setTimeout",
    "setInterval",
    "Function",
    "insertAdjacentHTML"
]

def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.readlines()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def detect_sources(line):
    detected = []
    for source in SOURCES:
        if source in line:
            detected.append(source)
    return detected

def detect_sinks(line):
    detected = []
    for sink in SINKS:
        if sink in line:
            detected.append(sink)
    return detected

def scan_file(file_path):
    lines = read_file(file_path)

    print(f"\nScanning: {file_path}")
    print("-" * 40)

    sources_found = []
    sinks_found = []

    for i, line in enumerate(lines, start=1):

        sources = detect_sources(line)
        sinks = detect_sinks(line)

        if sources:
            for s in sources:
                sources_found.append((s, i))

        if sinks:
            for s in sinks:
                sinks_found.append((s, i))

        if sources and sinks:
            print(f"[HIGH] Possible DOM XSS")
            print(f"Line {i}")
            print(f"Source: {sources}")
            print(f"Sink: {sinks}")
            print()

    if not sources_found and not sinks_found:
        print("No obvious sources or sinks detected.")

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".js"):
                scan_file(os.path.join(root, file))

def main():

    if len(sys.argv) != 2:
        print("Usage:")
        print("python domxss.py <file.js | directory>")
        sys.exit(1)

    target = sys.argv[1]

    if os.path.isfile(target):
        scan_file(target)

    elif os.path.isdir(target):
        scan_directory(target)

    else:
        print("Invalid path")

if __name__ == "__main__":
    main()