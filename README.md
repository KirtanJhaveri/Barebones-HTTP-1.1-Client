# Barebones HTTP/1.1 Client

This project showcases an independently developed barebones HTTP/1.1 client capable of performing fundamental HTTP GET requests and efficiently retrieving document bodies from URLs. Creating a barebones HTTP/1.1 client from scratch offers insights into protocol intricacies, networking fundamentals, and the inner workings of HTTP requests and responses.

## Table of Contents

- [Features Implemented](#features-implemented)
- [How to Use](#how-to-use)
- [Code Structure](#code-structure)
- [Testing](#testing)
- [Testing Script](#testing-script)
- [Future Enhancements](#future-enhancements)

## Features Implemented

### HTTP/1.1 Functionality
- **Host Header**: The client includes a `Host` header in requests, as required by HTTP/1.1 specifications.
- **Transfer-Encoding: chunked**: Correct interpretation of chunked transfer encoding in responses.
- **Connection Header**: Implementation of `Connection: close` for handling persistent connections.

### GET Method
- Focused on the GET method to retrieve content from URLs.
- Handles the initial line, headers, and content bytes as per the HTTP protocol.

### Redirect Handling
- Capable of handling redirects (status code 301) by following the location provided in the response.

### Error Handling
- Basic error handling implemented for socket-related errors. Returns `None` if there's an issue retrieving the resource.

## How to Use

The main functionality lies in the `retrieve_url` function, which takes a URL string as an argument and returns the body of the document as bytes.

### Usage
```bash
python3 client.py <URL>
```
## Code Structure

The code is structured as follows:

- `client.py`: Contains the main implementation of the HTTP/1.1 client.
- `test.py`: Testing script with test cases for the implemented client.
- `README.md`: Detailed information about the project.

## Testing

The implemented client can be tested using various URLs to verify its functionality. Consider using the provided testing script or crafting your own tests to ensure correctness and robustness.

### Testing Script

The repository includes a testing script (`test.py`) that contains test cases for a simple HTTP client. This script compares the output of your implementation (`retrieve_url`) against the expected output fetched by using `requests`. It conducts tests on standard URLs as well as bonus cases covering HTTPS, redirects, and UTF-8 characters in URLs.

To execute the testing script:

```bash
python3 test.py
```
The script will compare your implementation with the expected output for various URLs and provide feedback on correctness.

## Future Enhancements

Potential improvements or additional features that could be implemented:

- **HTTP Methods**: Extension to support other HTTP methods like POST, PUT, DELETE, etc.
- **Header Parsing**: Improved parsing of headers for more comprehensive handling.
- **Performance Optimization**: Optimizing socket handling for better performance.
- **Logging and Debugging**: Incorporating logging for better debugging capabilities.
