import os, subprocess
def run():
    editor = os.environ.get("EDITOR", "vi")
    subprocess.Popen(f"{editor} file.txt", shell=True)
run()
