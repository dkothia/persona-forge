]Persona Forge
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
````
python application.py
````
