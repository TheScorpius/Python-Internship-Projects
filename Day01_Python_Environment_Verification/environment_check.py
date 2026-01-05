import sys
import platform

def check_python_version():
    print("Python Version:")
    print(sys.version)
    print("-" * 40)

def check_os_details():
    print("Operating System Details:")
    print("System:", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("-" * 40)

def main():
    print("Python Environment Verification Tool\n")
    check_python_version()
    check_os_details()
    print("Environment verification completed successfully.")

if __name__ == "__main__":
    main()