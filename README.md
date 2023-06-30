This project is a distributed test automation system developed in Python. It allows you to execute tests in a scalable and distributed manner. The system includes an API that can be consumed by HTTP requests, a queue for task management, and multiple test execution agents to parallelize test execution.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Execute tests in a distributed and scalable manner.
- API for managing test runs, configurations, and retrieving test results.
- Test execution agents that listen to a queue for task distribution.
- Parallel test execution to improve efficiency.
- Centralized storage of test results.

## Installation

To set up the project, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/distributed-test-automation.git
   cd distributed-test-automation
1. Install the dependencies:

   ```shell
   pip install -r requirements.txt
## API Endpoints
- `GET /api/health/liveness`: Checks if the application is live. Returns a response with status code 200 if the application is running.

- `GET /api/tests/<test_id>`: Retrieves information about a specific test. The `test_id` parameter should be replaced with the ID of the desired test. Returns the test details and status.

- `POST /api/tests/<test_id>`: Adds a test to the queue for consumption. The `test_id` parameter should be replaced with the ID of the test to be added. Use this endpoint to initiate the execution of a specific test.

- `GET /api/tests/report/<test_id>`: Retrieves a report of the tests that have been run. The `test_id` parameter should be replaced with the ID of the desired test. Returns a detailed report containing the test results, including outcomes, errors, and other relevant metrics.
