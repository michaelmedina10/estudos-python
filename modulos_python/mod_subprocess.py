import subprocess

terminal = ['ping', '217.0.0.1', '-c', '4']

subprocess.run(terminal, capture_output=True)
print(terminal)