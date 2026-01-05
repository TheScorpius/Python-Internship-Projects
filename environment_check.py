import sys
import platform
import pkg_resources

def check_python_version():
    print("🐍 Python Version:")
    print(sys.version)
    print("-" * 50)

def check_os_details():
    print("💻 Operating System Details:")
    print("System:", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("-" * 50)

def check_installed_packages():
    print("📦 Installed Python Packages:")
    packages = sorted(["%s==%s" % (i.key, i.version) for i in pkg_resources.working_set])
    for pkg in packages:
        print(pkg)
    print("-" * 50)

def main():
    print("🔍 Python Environment Verification Tool\n")
    check_python_version()
    check_os_details()
    check_installed_packages()
    print("✅ Environment verification completed successfully.")

if __name__ == "__main__":
    main()