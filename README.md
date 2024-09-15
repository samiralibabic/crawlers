# Web Crawler Project

This project is a web-based application that provides two types of web crawlers to extract external links from websites.

## Features

- Two crawler versions:
  1. Single-page crawler (v1): Extracts external links from a single provided URL.
  2. Domain crawler (v2): Crawls an entire domain and extracts all external links.
- Web interface for easy interaction
- Asynchronous crawling process
- Display of extracted external links

## Technologies Used

- Python
- Flask (Web framework)
- BeautifulSoup (HTML parsing)
- Requests (HTTP requests)
- HTML/CSS/JavaScript (Frontend)
- Axios (AJAX requests)

## Setup and Installation

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
   pip install flask requests beautifulsoup4
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Enter a URL or domain in the input field.
2. Select the crawler version (v1 or v2).
3. Click the "Crawl" button.
4. Wait for the results to be displayed.

## Project Structure

- `app.py`: Main Flask application
- `crawler.py`: Contains both crawler implementations
- `templates/index.html`: HTML template for the web interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).