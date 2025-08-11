# agent/worker.py
import subprocess
import sys
import time
import os
import requests

CI_SERVER = "http://localhost:8000"

def run_loop():
    # Demo: Agents would poll server for tasks. Here we simulate an agent that runs a command passed as arg.
    if len(sys.argv) > 1:
        cmd = " ".join(sys.argv[1:])
        print("Agent executing:", cmd)
        proc = subprocess.run(cmd, shell=True)
        print("Exit:", proc.returncode)
        return
    print("Agent idle. To run a command: python worker.py echo hello")

if __name__ == "__main__":
    run_loop()
