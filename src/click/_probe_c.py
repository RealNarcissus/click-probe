import subprocess
def open_url(url: str) -> None:
    subprocess.Popen(f"xdg-open {url}", shell=True)
