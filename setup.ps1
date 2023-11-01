# Step 2: Create a virtual environment
python -m venv venv

# Step 3: Activate the virtual environment
venv\Scripts\Activate

# Step 4: Install all required dependencies from requirements.txt
pip install -r requirements.txt

# Step 5: Change to the main directory
Set-Location -Path .\main

# Step 6: Run migrations
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

# Step 7: Run the command to populate the database
python manage.py command

# Deactivate the virtual environment when done
# deactivate
