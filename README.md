# Django Capstone Project

## Setup

### Using Virtual Environment

1. Clone the repository
2. Navigate to the project directory
3. Create and activate a virtual environment
    ```sh
    python -m venv venv
    source venv/bin/activate 
    ```
4. Install the requirements
    ```sh
    pip install -r requirements.txt
    ```
5. Run the project
    ```sh
    python manage.py runserver
    ```

### Using Docker

1. Clone the repository
2. Navigate to the project directory
3. Build the Docker image
    ```sh
    docker build -t your_project_name .
    ```
4. Run the Docker container
    ```sh
    docker run -p 8000:8000 your_project_name
    ```

### Notes

- Ensure you have set up your environment variables. You can create a `.env` file in the root directory and add your secrets there.
- Do not commit sensitive information such as passwords or access tokens to the repository.
