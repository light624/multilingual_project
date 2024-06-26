### Project Title: Multilingual Blog with AI-Powered Search and Chatbot

![Django](https://img.shields.io/badge/Django-3.2.25-green) ![Python](https://img.shields.io/badge/Python-3.8-blue) ![Render](https://img.shields.io/badge/Deployed%20on-Render-blue)

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [Adding Articles](#adding-articles)
  - [AI-Powered Search](#ai-powered-search)
  - [AI Chatbot](#ai-chatbot)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

This project is a multilingual blog application built with Django. It features AI-powered search and chatbot functionalities using the Hugging Face transformers library. The application is designed to support multiple languages including English, French, Spanish, and German.

---

## Features

- **Multilingual Support**: Supports English, French, Spanish, and German.
- **AI-Powered Search**: Enhanced search functionality using Hugging Face's transformers for relevant article retrieval.
- **AI Chatbot**: A chatbot that provides answers based on a predefined knowledge base and dynamic responses.
- **Article Management**: Add, view, and delete articles.

---

## Setup and Installation

### Prerequisites

- Python 3.8+
- Django 3.2.25
- Git

### Clone the Repository

```sh
git clone https://github.com/light624/multilingual_project.git
cd multilingual_project
```

### Create and Activate Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Migrate Database

```sh
python manage.py migrate
```

### Create Superuser

```sh
python manage.py createsuperuser
```

### Run Server

```sh
python manage.py runserver
```

---

## Usage

### Adding Articles

1. **Navigate to Add Article Page**:
   - URL: `http://127.0.0.1:8000/add_article/`
   
2. **Fill in the Form**:
   - Title
   - Content

3. **Submit**:
   - Click the "Save" button.

### AI-Powered Search

1. **Navigate to Search Page**:
   - URL: `http://127.0.0.1:8000/search/`

2. **Enter Search Query**:
   - Enter the keyword or question in the search bar.

3. **View Results**:
   - Relevant articles will be displayed along with their relevance score.

### AI Chatbot

1. **Navigate to Chatbot Page**:
   - URL: `http://127.0.0.1:8000/chatbot/`

2. **Enter Question**:
   - Type your question in the input field.

3. **View Response**:
   - The chatbot will provide an answer based on the knowledge base or dynamic response.

---

## Deployment

### Deploying on Render.com

1. **Create a New Web Service** on Render.com
2. **Connect to Your GitHub Repository**
3. **Configure Environment**:
   - Set the build command: `pip install -r requirements.txt`
   - Set the start command: `gunicorn multilingual_project.wsgi:application`
4. **Add Environment Variables**:
   - `DJANGO_SECRET_KEY`: Your Django secret key.
   - `DATABASE_URL`: Your database URL.
5. **Deploy**: Render.com will automatically deploy your application.
   -My_url :"https://multilingual-project.onrender.com"
---

## Troubleshooting

### Common Issues

- **ModuleNotFoundError: No module named 'nltk'**
  - Ensure `nltk` is listed in `requirements.txt`.
  - Run `pip install nltk`.

- **RuntimeError: At least one of TensorFlow 2.0 or PyTorch should be installed**
  - Ensure `torch` is listed in `requirements.txt`.
  - Run `pip install torch`.

- **Out of Memory Error**
  - Consider upgrading your Render.com instance.
  - Use Hugging Face's hosted inference API instead of running models locally.

---

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/feature-name`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

![GitHub](https://img.shields.io/github/license/light624/multilingual_project) ![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)

---

This `README.md` provides a comprehensive guide to setting up, using, and deploying your multilingual blog application with AI-powered search and chatbot functionalities.