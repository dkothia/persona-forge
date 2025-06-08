# persona-forge-app

# Persona Forge

Persona Forge is a full-stack application designed to generate detailed customer personas based on their reviews using advanced AI techniques. It supports both single and batch processing of customer reviews, including the ability to upload and process CSV or Excel files and download the results. The frontend is managed as a Git submodule and provides an intuitive React-based user interface.

---

## Table of Contents

- [Features](#features)  
- [Architecture](#architecture)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Frontend Submodule](#frontend-submodule)  
- [Batch Processing](#batch-processing)  
- [File Upload Support](#file-upload-support)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- Generate AI-driven customer personas from individual reviews.
- Batch processing of multiple customer reviews in one request.
- Upload CSV or Excel files containing customer reviews to process in bulk.
- Download processed results as CSV files for easy integration.
- React-based frontend for seamless user interaction.
- Backend API with endpoints for single and batch persona generation.

---

## Architecture

- **Backend:** Flask API running on AWS Elastic Beanstalk.  
- **Frontend:** React app maintained as a Git submodule under `persona-frontend` folder.  
- **AI Integration:** Uses OpenAI API for persona generation.  
- **File Processing:** Supports CSV and Excel file uploads for bulk processing.

---

## Getting Started

### Prerequisites

- Python 3.8+  
- Node.js and npm (for frontend development)  
- AWS CLI and Elastic Beanstalk CLI (if deploying)  
- Git

### Setup Backend

1. Clone the main repo with submodules:

   ```bash
   git clone --recurse-submodules https://github.com/dkothia/persona-forge.git
   cd persona-forge
Create and activate a Python virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install backend dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set your OpenAI API key as an environment variable:

bash
Copy
Edit
export OPENAI_API_KEY="your_openai_api_key"
Run the Flask backend locally:

bash
Copy
Edit
flask run
Usage
Single Review Persona Generation
Send a POST request to:

bash
Copy
Edit
POST /generate-persona
Content-Type: application/json
Body: { "text": "Your customer review here" }
Example curl command:

bash
Copy
Edit
curl -X POST http://localhost:5000/generate-persona \
-H "Content-Type: application/json" \
-d '{"text": "Amazing service and food!"}'
Batch Review Persona Generation
Send a POST request to:

bash
Copy
Edit
POST /generate-personas-batch
Content-Type: application/json
Body: {
  "data": [
    {"customer_id": "CUST001", "review": "Great ambiance and service."},
    {"customer_id": "CUST002", "review": "Food was delicious!"}
  ]
}
File Upload Processing
The frontend supports uploading CSV or Excel files containing customer reviews with columns:

customer_id

review

The backend processes the uploaded file, generates personas for each review, and returns a downloadable file with the results.

Frontend Submodule
The frontend React app lives inside the persona-frontend folder as a Git submodule.

Working with Submodule
To initialize and update the submodule after cloning:

bash
Copy
Edit
git submodule init
git submodule update
Or clone including submodules:

bash
Copy
Edit
git clone --recurse-submodules https://github.com/dkothia/persona-forge.git
To work on frontend code:

bash
Copy
Edit
cd persona-frontend
npm install
npm start
Batch Processing
Batch persona generation can be performed via the API or frontend interface, allowing efficient processing of multiple customer reviews in one go.

File Upload Support
Supported file formats:

CSV (.csv)

Excel (.xlsx, .xls)

Uploaded files should have at least these columns:

customer_id	review
CUST001	"The service was great."

The system processes all reviews and appends the persona output in the results downloadable by the user.

Contributing
Contributions and improvements are welcome! Please submit pull requests or open issues to discuss changes.

License
This project is licensed under the MIT License.

Contact
Created and maintained by Dishant Kothia.

yaml
Copy
Edit

---

If you want, I can also help you create a README for the **frontend** repo specifically.

Let me know!


markdown
Copy
Edit
# Persona Forge

**Persona Forge** is an AI-powered full-stack application that generates rich, tailored customer personas based on user reviews. It supports both individual and bulk processing of reviews, accepts CSV/Excel uploads, and returns detailed persona outputs via downloadable files. The frontend is built in React and included as a Git submodule for modularity.

---

## 📌 Features

- 🎯 **Single Review Analysis** – Generate a persona from one customer review.
- 📦 **Batch Processing** – Handle multiple reviews in a single API request.
- 📂 **File Upload Support** – Upload `.csv` or `.xlsx` files and receive processed output for all rows.
- 💾 **Downloadable Results** – Download AI-generated personas in bulk.
- 🌐 **Modern React Frontend** – Clean, user-friendly UI (included as Git submodule).
- 🚀 **Deployable on AWS Elastic Beanstalk** – Easily run and scale the app.

---

## 🧱 Project Structure

persona-forge/
├── persona-frontend/ # React frontend (Git submodule)
├── app.py # Flask backend
├── utils.py # Supporting backend utilities
├── requirements.txt # Backend dependencies
└── README.md # You're here!

yaml
Copy
Edit

---

## 🧰 Tech Stack

| Layer      | Tech Used            |
|------------|----------------------|
| Backend    | Python, Flask, OpenAI |
| Frontend   | React.js, Tailwind   |
| Deployment | AWS Elastic Beanstalk|
| File Handling | pandas, openpyxl, Flask-Uploads |

---

## 🚀 Getting Started

### 1. Clone the Repo with Submodules

```bash
git clone --recurse-submodules https://github.com/dkothia/persona-forge.git
cd persona-forge
If you already cloned it:

bash
Copy
Edit
git submodule init
git submodule update
2. Backend Setup (Flask)
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Set your OpenAI API key:

bash
Copy
Edit
export OPENAI_API_KEY="your-api-key-here"
Run the app:

bash
Copy
Edit
flask run
3. Frontend Setup (React)
bash
Copy
Edit
cd persona-frontend
npm install
npm start
App runs at http://localhost:3000 and interacts with the backend API.

💡 API Usage Guide
🔹 Single Review
http
Copy
Edit
POST /generate-persona
Content-Type: application/json

{
  "text": "The sushi was fresh and the ambiance perfect for a date night."
}
Curl Example:

bash
Copy
Edit
curl -X POST http://localhost:5000/generate-persona \
-H "Content-Type: application/json" \
-d '{"text": "Amazing service and food!"}'
🔹 Batch Review
http
Copy
Edit
POST /generate-personas-batch
Content-Type: application/json

{
  "data": [
    {
      "customer_id": "CUST001",
      "review": "Great service and fast delivery!"
    },
    {
      "customer_id": "CUST002",
      "review": "The ambiance was amazing, and the food was worth every penny."
    }
  ]
}
📄 CSV/Excel Upload (Via Frontend)
Upload .csv or .xlsx file with the following structure:

customer_id	review
CUST001	"The service was amazing!"
CUST002	"Loved the coffee and pastries."

After processing, you'll receive a downloadable file with the original content and an added persona column.

🔧 Frontend Submodule Notes
The frontend lives inside persona-frontend/ as a Git submodule.

To update or re-initialize it:

bash
Copy
Edit
git submodule update --remote
If needed:

bash
Copy
Edit
git submodule add https://github.com/dkothia/persona-frontend.git persona-frontend
📤 Deployment on AWS Elastic Beanstalk
Ensure you have the AWS CLI and EB CLI set up:

bash
Copy
Edit
eb init -p python-3.8 persona-env
eb create persona-env
eb deploy
Update frontend to point to the deployed backend URL if needed.

🤝 Contributing
Contributions are welcome! Please fork this repo, create a feature branch, and submit a pull request.

🔐 Environment Variables
Variable	Purpose
OPENAI_API_KEY	Required for persona generation

Set in .env (but don’t commit it) or export directly in your shell session.

📄 License
This project is licensed under the MIT License.

✨ Author
Dishant Kothia
Feel free to connect on GitHub

vbnet
Copy
Edit

Let me know if you'd like a separate version for `persona-frontend` as well!






