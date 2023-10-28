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
- Supports partial matching for company name and shareholder name. <TODO: Should match by shareholder's name>
- Displays search results with names and registration codes.
- Clicking on a result leads to the data view.
- Provides a link to the establishment form.

### Limited Liability Company Data View
- Displays company details, including name, registration code, establishment date, total capital, and a list of shareholders.
- Shareholder information includes first name, last name, personal identification code (for natural persons), and name and registration code (for legal entities). <TODO: Add euro sign>
- Indicates the shareholder's share in euros and whether they are a founder.

### Limited Liability Company Establishment Form
- Allows entering information for a new company, including name, registration code, establishment date, and total capital.
- Shareholder information includes an existing natural or legal person and their share in euros. <TODO: Add euro sign>
- Automatically marks shareholders as founders.
- The sum of shareholders' shares must equal the total capital. <TODO: total capital validator>
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

## Installation

