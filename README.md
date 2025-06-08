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
2. Install Dependencies
Frontend
Navigate to the persona-frontend directory and install dependencies:

Backend
Navigate to the root directory and install Python dependencies:

3. Configure Environment Variables
Create a .env file in the backend directory and add the following:

For the frontend, you can configure environment variables in .env.local:

4. Run the Application
Backend
Start the Flask server:

Frontend
Start the React development server:

5. Access the Application
Open your browser and navigate to:

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
Backend
API Endpoints
1. /generate-persona (POST)
Description: Generate a persona for a single review.
Request Body:
Response:
2. /generate-personas-batch (POST)
Description: Generate personas for multiple reviews.
Request Body:
Response:
3. /generate-personas-batch-csv (POST)
Description: Generate personas for reviews in a CSV or Excel file.
Request Body: Upload a file with the required columns (customer_id, review).
Response:
Troubleshooting
1. Backend Not Running
Ensure Flask is installed and the server is running on the correct port (8000).
Check for errors in the terminal.
2. Frontend Not Connecting to Backend
Verify the REACT_APP_BACKEND_URL in .env.local matches the backend URL.
Check the browser console for errors.
3. File Upload Issues
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
