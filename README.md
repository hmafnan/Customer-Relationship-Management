# Customer-Relationship-Management
Purpose of this portal is to allow our admins to create new leads.
Be able to be in touch with the leads and see all available leads and their touches.

## How it works
- First User or Admin must register themselves in this portal
- Login to the portal with your newly created account
- Now they can create new leads and their touches from navigation links
- They can also see list of leads and their touches if they exists

## Dependencies
- Python 3+ (Ideally 3.7)
- PIP

## Instructions to setup
- CD to root of the repo
- Create new virtual environment by using python 3.7
- Activate newly created virtual environment
- At the root do `pip install -r requirements.txt`
- Enter into python interpreter of this environment, then
- `>>> from crm import db`
- `>>> db.create_all()`
- `>>> exit()`
- Above commands should initialize databases
- Do `python run.py` to run server locally
- Visit localhost in the browser
- Register from registration form
- Login with those credentials to view full functionality
