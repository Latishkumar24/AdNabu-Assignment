# AdNabu Test Store

This repository contains Selenium-based automated tests for the AdNabu Test Store application.

## Project Structure

- `assets/`: Contains stylesheets and other static assets
- `testcases/`: Test case documentation
- `tests/`: Python test files using Selenium
  - `test_add_to_cart.py`: Tests for adding items to cart functionality
  - `reports/`: Test execution reports

## Prerequisites

- Python 3.x
- Chrome browser (or other supported browsers)
- ChromeDriver (matching your Chrome version)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Latishkumar24/AdNabu-Assignment.git
   cd AdNabu-Assignment
   ```

2. Install dependencies:
   ```bash
   pip install selenium pytest
   ```

3. Download and install ChromeDriver from https://chromedriver.chromium.org/

## Running Tests

Execute the tests using pytest:

```bash
pytest tests/
```

To run a specific test file:

```bash
pytest tests/test_add_to_cart.py
```

## Test Reports

After running tests, check the `tests/reports/` directory for HTML reports:
- `report.html`: Detailed test report
- `final_report.html`: Final summary report

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure everything works
5. Submit a pull request

## License

This project is licensed under the MIT License.