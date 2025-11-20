import subprocess
import os
import config.settings as settings

class TerminalEngine:
    def __init__(self):
        self.history = []
        self.whitelist = settings.security['whitelisted_commands']

    def execute_command(self, command):
        if command.split()[0] not in self.whitelist:
            return "Command not allowed"
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            self.history.append(command)
            return result.stdout or result.stderr
        except Exception as e:
            return f"Error: {str(e)}"

    def read_file(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                return f.read()
        return "File not found"

    def write_file(self, path, content):
        # Prompt for permission (mocked)
        if input(f"Allow write to {path}? (y/n): ") == 'y':
            with open(path, 'w') as f:
                f.write(content)
            return "File written"
        return "Permission denied"
