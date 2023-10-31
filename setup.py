import os
import platform
import subprocess

# Determine the user's system
system = platform.system()

# Go to the root folder where README.md and requirements.txt is placed
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create virtual environment
if system in ('Linux', 'Darwin'):  # Linux or MacOS
    subprocess.run(['python3', '-m', 'venv', 'venv'])
    activate_cmd = 'source venv/bin/activate'
else:  # Windows
    subprocess.run(['python', '-m', 'venv', 'venv'])
    activate_cmd = '.\\venv\\Scripts\\activate'

# Activate virtual environment
subprocess.run(activate_cmd, shell=True)

# Install requirements
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

# Go to the main directory
os.chdir('main')

# Run migrations
subprocess.run(['python', 'manage.py', 'makemigrations'])
subprocess.run(['python', 'manage.py', 'migrate'])
subprocess.run(['python', 'manage.py', 'migrate', '--run-syncdb'])

# Run command to populate the database
subprocess.run(['python', 'manage.py', 'command'])
