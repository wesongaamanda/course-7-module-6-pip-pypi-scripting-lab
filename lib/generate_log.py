from datetime import datetime
import os

def generate_log(data):
    """
    Generate a log file from a list of entries.

    - data must be a list, otherwise raises ValueError
    - Creates a file named log_YYYYMMDD.txt with today's date
    - Writes each entry on its own line
    - Prints a confirmation message with the filename
    - Returns the filename
    """

    # STEP 1: Validate input — must be a list
    if not isinstance(data, list):
        raise ValueError("Input must be a list.")

    # STEP 2: Generate filename with today's date e.g. "log_20250408.txt"
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write each entry to the file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print confirmation message
    print(f"Log written to {filename}")

    # Return the filename so tests and callers can use it
    return filename


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)