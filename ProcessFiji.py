import subprocess
import time

def open_fiji_and_run_plugin():
    # Path to the Fiji executable
    fiji_path = r"C:\Users\felix\OneDrive\Documents\ENSMA\R&D\Fiji.app"

    # Command to run Fiji
    fiji_command = [fiji_path]

    # Run Fiji
    fiji_process = subprocess.Popen(fiji_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # Wait for Fiji to start
    time.sleep(5)

    # Send key shortcuts to open the plugin
    fiji_process.stdin.write("run('Trainable Weka Segmentation');\n")
    fiji_process.stdin.write("waitForImage();\n")

    # Close Fiji
    fiji_process.stdin.write("run('Quit');\n")

    # Wait for Fiji to close
    fiji_process.wait()

if __name__ == "__main__":
    open_fiji_and_run_plugin()
