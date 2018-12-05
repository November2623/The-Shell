from shell import handle_execute_command
from subprocess import PIPE, run

command = ['cat', 'File1']
result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
a = result.stdout
