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
   git clone https://github.com/yourusername/web-crawler-project.git
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

4. Run the application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://localhost:5001`

### Docker Setup

1. Build the Docker image:
   ```
   docker build -t web-crawler-app .
   ```

2. Run the Docker container:
   ```
   docker run -p 5001:5001 web-crawler-app
   ```

3. Open a web browser and navigate to `http://localhost:5001`

## Usage

1. Enter a URL or domain in the input field.
2. Select the crawler version (v1 or v2).
3. Click the "Crawl" button.
4. Wait for the results to be displayed.

## Accessing the Application

The application can be accessed in several ways:

- Localhost: `http://localhost:5001`
- Loopback IP: `http://127.0.0.1:5001`
- Local Network: `http://<your-local-ip>:5001` (replace <your-local-ip> with your machine's IP address)

## Changing the Port

To use a different port:

1. For local setup, modify the `app.py` file.
2. For Docker setup, update the `Dockerfile` and run command:
   ```
   docker run -p <new-port>:5001 -e PORT=<new-port> web-crawler-app
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).