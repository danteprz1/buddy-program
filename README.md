# QA Buddy Program

## Description
This repository showcases a Proof-of-Concept (POC) for the QA Buddy Program. It includes automated test cases 
for both the frontend and backend of the Todoist (https://app.todoist.com/) website.

## Tech Stack
    - Python 3.5+
    - Pytest
    - Playwright
    - BrowserStack
## Setup
### Requirements
```bash
pip install -r requirements.txt
```

### Local
```bash
export USER_EMAIL="YOUR_EMAIL"
export USER_PASSWORD="YOUR_PASSWORD"
export API_TOKEN="YOUR_API_TOKEN"
```

### Additional setup for BrowserStack
```bash
export BROWSERSTACK_USERNAME="YOUR_USERNAME"
export BROWSERSTACK_ACCESS_KEY="YOUR_ACCESS_KEY"
```

## Run locally
```bash
pytest --local=True tests/ui --html-report=ui-report.html
pytest tests/api -html-report=api-report.html
```

## Run UI tests on BrowserStack
```bash
pytest --local=False tests/ui --html-report=ui-report.html
```

## Frontend demo
![](https://github.com/danteprz1/buddy-program/blob/main/demos/frontend.gif)

## Backend demo

![](https://github.com/danteprz1/buddy-program/blob/main/demos/backend.gif)

## High level interaction diagram

![](https://github.com/danteprz1/buddy-program/blob/main/diagram.drawio.png)
