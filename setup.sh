#!/bin/bash

# Step 2: Create a virtual environment
python3 -m venv venv

# Step 3: Activate the virtual environment
source venv/bin/activate

# Step 4: Install all required dependencies from requirements.txt
pip install -r requirements.txt

# Step 5: Change to the main directory
cd main

# Step 6: Run migrations
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate --run-syncdb

# Step 7: Run the command to populate the database
python3 manage.py command

# Deactivate the virtual environment when done
deactivate
