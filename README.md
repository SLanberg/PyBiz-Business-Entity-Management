# Limited Liability Company Management Web Application

## Objective
The aim of this project is to assess and demonstrate knowledge of Python and the ability to apply recognized development patterns and techniques.

## Business Task
Create a web application for managing limited liability companies, including the ability to establish new companies, search for existing ones, and view detailed company information.

## Functional Requirements
The application consists of the following pages:
- Home page
- Limited liability company data view
- Limited liability company establishment form
- Limited liability company data edit view

### Home Page
- Allows searching for existing limited liability companies.
- Supports partial matching for company name and shareholder name.
- Displays search results with names and registration codes.
- Clicking on a result leads to the data view.
- Provides a link to the establishment form.

### Limited Liability Company Data View
- Displays company details, including name, registration code, establishment date, total capital, and a list of shareholders.
- Shareholder information includes first name, last name, personal identification code (for natural persons), and name and registration code (for legal entities).
- Indicates the shareholder's share in euros and whether they are a founder.

### Limited Liability Company Establishment Form
- Allows entering information for a new company, including name, registration code, establishment date, and total capital.
- Shareholder information includes an existing natural or legal person and their share in euros.
- Automatically marks shareholders as founders.
- The sum of shareholders' shares must equal the total capital.
- Includes a save button to navigate to the data view upon success.

## Non-Functional Requirements
- Easily accessible software for installation. <TODO: Write installation guide>
- Source code includes installation instructions.
- Automated initial data creation.
- Separation of CSS for styling.
- Functional requirements take precedence over visual design. 

## Optional Additional Functionality
### Limited Liability Company Capital Increase Form
- Allows increasing the capital of existing shareholders or adding new ones.
- Shareholders added here are not marked as founders.
- The total capital size must match the sum of shareholders’ shares.
- Includes a save button to return to the data view.

## Installation Manual

This README provides detailed instructions for setting up and installing the application on both Linux/MacOS and Windows systems.

### Install project with script

```bash
# Step 1: Navigate to the root folder where README.md and requirements.txt are located.

### Linux/MacOS
# Step 2: 
chmod +x automate_setup.sh
# Step 3: 
./setup.py
# Step 4: 
source venv/bin/activate

### Windows
# Step 2: 
Set-ExecutionPolicy RemoteSigned
# Step 3: 
.\automate_setup.ps1
# Step 4: 
.\venv\Scripts\activate
```

### Linux/MacOS By Hand

```bash
# Step 1: Navigate to the root folder where README.md and requirements.txt are located.

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
```

### Windows Installation By Hand

```bash
# Step 1: Navigate to the root folder where README.md and requirements.txt are located.

# Step 2: Create a virtual environment
python -m venv venv

# Step 3: Activate the virtual environment
.\venv\Scripts\activate

# Step 4: If your system has a policy against running scripts, use the following command:
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Step 5: Install all required dependencies from requirements.txt
pip install -r requirements.txt

# Step 6: Change to the main directory
cd main

# Step 7: Run migrations
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

# Step 8: Run the command to populate the database
python manage.py command
```
