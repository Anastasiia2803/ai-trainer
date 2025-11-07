import subprocess, sys

def test_cli_runs():
    r = subprocess.run([sys.executable, "main.py", "--goal", "balance", "--days", "2"], capture_output=True, text=True)
    assert r.returncode == 0
    assert "AI-Trainer plan" in r.stdout
