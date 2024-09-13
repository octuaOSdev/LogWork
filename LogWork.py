import datetime

def write_to_log(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.log", "a") as file:
        file.write(current_time + "\n" + message + "\n")

# Example usage
write_to_log("This is a new log entry.")
