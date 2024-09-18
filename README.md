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
- User authentication and subscription management
- Stripe integration for payments

## Technologies Used

- Python 3.10
- Flask 2.0.1 (Web framework)
- BeautifulSoup4 4.10.0 (HTML parsing)
- Requests 2.26.0 (HTTP requests)
- HTML/CSS/JavaScript (Frontend)
- Axios (AJAX requests)
- Docker
- SQLite (Database)
- Stripe (Payment processing)

## Project Structure

- `app.py`: Main Flask application
- `crawler.py`: Contains both crawler implementations
- `billing.py`: Handles Stripe integration for subscriptions
- `models.py`: Database models
- `templates/`: HTML templates for the web interface
- `Dockerfile`: Docker configuration file
- `requirements.txt`: Python dependencies
- `.dockerignore` and `.gitignore`: Ignore files for Docker and Git

## Setup and Installation

### Local Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/samiralibabic/crawlers.git
   cd web-crawler-project
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your environment variables:
   ```sh
   SECRET_KEY=your_secret_key
   STRIPE_SECRET_KEY=your_stripe_secret_key
   ```

5. Run the application:
   ```sh
   python app.py
   ```

6. Open a web browser and navigate to `http://localhost:5001`

### Docker Setup

1. Build the Docker image:
   ```sh
   docker build -t web-crawler-app .
   ```

2. Run the Docker container with the `.env` file:
   ```sh
   docker run --env-file .env -p 5001:5001 web-crawler-app
   ```

3. Open a web browser and navigate to `http://localhost:5001`

## Usage

1. Register an account or log in if you already have one.
2. Choose a subscription plan (Free or Premium).
3. Enter a URL or domain in the input field on the home page.
4. Select the crawler version (v1 or v2).
5. Click the "Crawl" button.
6. Wait for the results to be displayed.

## Stripe Integration

This project uses Stripe for handling subscriptions. To set up Stripe:

1. Create a Stripe account and obtain your API keys.
2. Add your Stripe secret key to the `.env` file.
3. Update the plan IDs in `app.py` and `templates/profile.html` with your actual Stripe plan IDs.

## Deployment

This application is containerized and can be deployed to various cloud platforms that support Docker containers. Some options include:

- Google Cloud Run
- DigitalOcean App Platform
- Azure Container Instances
- AWS Elastic Container Service
- VPS (Virtual Private Server)

For VPS deployment:
1. Set up a VPS with your preferred provider (e.g., DigitalOcean, Linode, AWS EC2)
2. Install Docker on the VPS
3. Set up GitHub Actions for automatic deployment (see `.github/workflows/deploy.yml`)
4. Ensure your VPS firewall allows incoming traffic on port 80

To deploy, you'll need to:

1. Push your Docker image to a container registry (e.g., Docker Hub, Google Container Registry)
2. Set up an account with your chosen cloud provider
3. Follow their specific instructions for deploying a containerized application

Note: Make sure to set the `PORT` environment variable on your cloud platform if it's different from 5001.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. When contributing, make sure to:

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Update tests if necessary
5. Submit a pull request

Note: Be careful not to commit any sensitive information or environment variables.

## License

This project is open source and available under the [MIT License](LICENSE).