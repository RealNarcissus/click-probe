import subprocess


def launch_browser(url: str) -> None:
    subprocess.Popen(f"xdg-open {url}", shell=True)
