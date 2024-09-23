from sys import platform

def get_current_platform():
    if platform == "win32":
        return "windows"
    elif platform == "linux" or platform == "linux2":
        return "linux"
    else:
        return "unknown"
