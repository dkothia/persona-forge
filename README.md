Persona Forge
Persona Forge is a powerful application designed to generate user personas based on customer reviews. It provides functionality for processing individual reviews, batch reviews, and file uploads (CSV/Excel). This tool is ideal for businesses and marketers looking to understand their customers better and create targeted strategies based on persona insights.

Features
1. Single Review Processing
Input a single customer review in the text area.
Generate a detailed persona based on the review.
The persona includes demographics, goals, pain points, personality traits, and preferred communication styles.
2. Batch Review Processing
Input multiple customer reviews separated by new lines.
Generate personas for each review in a batch.
View the results in a table format.
3. File Upload Processing
Upload a CSV or Excel file containing customer reviews.
The file must include the columns customer_id and review.
Generate personas for all reviews in the file.
View the results in a table format and download them as an Excel file.
4. Download Results
Export the generated personas to an Excel file for further analysis or sharing.
Technologies Used
Frontend
React.js: For building the user interface.
XLSX.js: For exporting persona results to Excel files.
Backend
Flask: For handling API requests and persona generation logic.
Python Libraries:
pandas: For processing Excel files.
csv: For processing CSV files.
Deployment
AWS Elastic Beanstalk: For deploying the backend.
Netlify: For deploying the frontend.
Setup Instructions
Follow these steps to set up and run the Persona Forge application locally:

1. Clone the Repository

```
git clone https://github.com/your-repo/persona-forge.git
cd persona-forge
```

2. Install Dependencies
Frontend
Navigate to the persona-frontend directory and install dependencies:
```
cd persona-frontend
npm install
```
3. Configure Environment Variables
Create a .env file in the backend directory and add the following:
FLASK_ENV=development
PORT=8000
For the frontend, you can configure environment variables in .env.local:
REACT_APP_BACKEND_URL=http://localhost:8000

4. Run the Application
Backend
Start the Flask server:
```
python application.py
```
Frontend
Start the React development server:
```
npm start
```
5. Access the Application
Open your browser and navigate to:
```
http://localhost:3000
```

Usage Guide
1. Single Review Processing
Enter a customer review in the text area.
Click the "Generate Personas" button.
View the generated persona in the result box.

2. Batch Review Processing
Enter multiple customer reviews separated by new lines in the text area.
Click the "Generate Personas" button.
View the generated personas in a table below.

3. File Upload Processing
Click the "Upload File" button and select a CSV or Excel file.
Ensure the file contains the columns customer_id and review.
View the generated personas in a table below.
Click the "Download Results" button to export the results to an Excel file.

File Structure
Frontend

```
persona-frontend/
├── src/
│   ├── App.js          # Main React component
│   ├── styles.js       # Styling for components
│   ├── components/     # Reusable components
│   └── utils/          # Utility functions
├── public/
│   └── index.html      # HTML template
└── .gitignore          # Files to ignore in version control
```

Backend
````
persona-forge/
├── application.py      # Flask application
├── requirements.txt    # Python dependencies
├── utils/              # Utility functions
└── .gitignore          # Files to ignore in version control
````

API Endpoints
1. /generate-persona (POST)
Description: Generate a persona for a single review.

````
{
  "text": "The pasta was rich and creamy, and our waiter was incredibly attentive."
}
````
Response:

````
{
  "persona": "A food enthusiast who values quality and attentive service."
}
````

2. /generate-personas-batch (POST)
Description: Generate personas for multiple reviews.
Request Body:
````
{
  "data": [
    {
      "customer_id": "CUST001",
      "review": "The pasta was rich and creamy, and our waiter was incredibly attentive."
    },
    {
      "customer_id": "CUST002",
      "review": "Loved the cozy ambiance and the dessert—chocolate lava cake was divine."
    }
  ]
}
````

Response:

````
{
  "status": "success",
  "data": [
    {
      "Customer ID": "CUST001",
      "Review": "The pasta was rich and creamy, and our waiter was incredibly attentive.",
      "Persona": "A food enthusiast who values quality and attentive service."
    },
    {
      "Customer ID": "CUST002",
      "Review": "Loved the cozy ambiance and the dessert—chocolate lava cake was divine.",
      "Persona": "A customer who enjoys a relaxing atmosphere and indulgent desserts."
    }
  ]
}
````

3. /generate-personas-batch-csv (POST)
Description: Generate personas for reviews in a CSV or Excel file.
Request Body: Upload a file with the required columns (customer_id, review).
Response:

````
{
  "status": "success",
  "data": [
    {
      "Customer ID": "CUST001",
      "Review": "The pasta was rich and creamy, and our waiter was incredibly attentive.",
      "Persona": "A food enthusiast who values quality and attentive service."
    },
    {
      "Customer ID": "CUST002",
      "Review": "Loved the cozy ambiance and the dessert—chocolate lava cake was divine.",
      "Persona": "A customer who enjoys a relaxing atmosphere and indulgent desserts."
    }
  ]
}
````

3. /generate-personas-batch-csv (POST)
Description: Generate personas for reviews in a CSV or Excel file.
Request Body: Upload a file with the required columns (customer_id, review).
Response:

````
{
  "status": "success",
  "data": [
    {
      "Customer ID": "CUST001",
      "Review": "The pasta was rich and creamy, and our waiter was incredibly attentive.",
      "Persona": "A food enthusiast who values quality and attentive service."
    },
    {
      "Customer ID": "CUST002",
      "Review": "Loved the cozy ambiance and the dessert—chocolate lava cake was divine.",
      "Persona": "A customer who enjoys a relaxing atmosphere and indulgent desserts."
    }
  ]
}
````

Troubleshooting

1. Backend Not Running
Ensure Flask is installed and the server is running on the correct port (8000).
Check for errors in the terminal.

3. Frontend Not Connecting to Backend
Verify the REACT_APP_BACKEND_URL in .env.local matches the backend URL.
Check the browser console for errors.

5. File Upload Issues
Ensure the file contains the required columns (customer_id, review).
Check the backend logs for errors during file processing.

Contributing
We welcome contributions to improve Persona Forge! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request with a detailed description of your changes.
License
Persona Forge is licensed under the MIT License.

Contact
For questions or support, please contact:

Email: support@personaforge.com
GitHub Issues: GitHub Issues
Thank you for using Persona Forge! 🎉




