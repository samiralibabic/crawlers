# Web Crawler Project

This project is a web-based application that provides two types of web crawlers to extract external links from websites. It's containerized using Docker for easy deployment and consistency across environments.

## Features

- Two crawler versions:
  1. Single-page crawler (v1): Extracts external links from a single provided URL.
  2. Domain crawler (v2): Crawls an entire domain and extracts all external links.
- Web interface for easy interaction
- Dockerized for consistent deployment
- Asynchronous crawling process
- Display of extracted external links

## Technologies Used

- Python 3.10
- Flask 2.0.1 (Web framework)
- BeautifulSoup4 4.10.0 (HTML parsing)
- Requests 2.26.0 (HTTP requests)
- HTML/CSS/JavaScript (Frontend)
- Axios (AJAX requests)
- Docker

## Project Structure

- `app.py`: Main Flask application
- `crawler.py`: Contains both crawler implementations
- `templates/index.html`: HTML template for the web interface
- `Dockerfile`: Docker configuration file
- `requirements.txt`: Python dependencies
- `.dockerignore` and `.gitignore`: Ignore files for Docker and Git

## Setup and Installation

### Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/samiralibabic/crawlers.git
   cd web-crawler-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Initialize the Database:
   Ensure the `instance` directory exists:
   ```bash
   mkdir -p instance
   ```

   Run the database migrations to set up the database:
   ```bash
   flask db upgrade
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open a web browser and navigate to `http://localhost:5001`

### Docker Setup

1. Build the Docker image:
   ```
   docker build -t web-crawler-app .
   ```

2. Run the Docker container:
   ```
   docker run --name web-crawler-app --env-file .env -p 5001:5001 web-crawler-app
   ```

3. Open a web browser and navigate to `http://localhost:5001`

## Usage

1. Enter a URL or domain in the input field.
2. Select the crawler version (v1 or v2).
3. Click the "Crawl" button.
4. Wait for the results to be displayed.

## Deployment

This application is containerized and can be deployed to various cloud platforms that support Docker containers. Some options include:

- Google Cloud Run
- DigitalOcean App Platform
- Azure Container Instances
- AWS Elastic Container Service

To deploy, you'll need to:

1. Push your Docker image to a container registry (e.g., Docker Hub, Google Container Registry)
2. Set up an account with your chosen cloud provider
3. Follow their specific instructions for deploying a containerized application

Note: Make sure to set the `PORT` environment variable on your cloud platform if it's different from 5001.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).