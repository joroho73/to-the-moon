# To the Moon 🚀🌙 

This repository is for use by candidates joining Future Energy Associates to demonstrate their technical skills. It contains the start of a Django project for a web application for signing small businesses up to a new marketplace.

It contains the output of the django project creation command
```
django-admin startproject mysite
```

A few simple files have been added: `models.py`, `views.py` and `templates/company.html`, and the `app` module has been registered in `settings.py` by adding its name to `INSTALLED_APPS`  

To run the project, navigate to the `app` directory and run `python manage.py runserver`. The only endpoint currently active is `/company` 

## Task

Future Energy Associates is building a new market platform for businesses to procure energy. This will involve correctly identifying and collecting data about the company that can be validated against their energy bill.  

In this app, please prioritise and start to create some of the following functionality, creating accompanying tests (as appropriate) along the way:
- Create an address lookup from postcode using `https://api.ideal-postcodes.co.uk` or other service of your choosing 
- Based on address perform search to find associated business record from `https://api.company-information.service.gov.uk/advanced-search/companies`
- Create option to indicate company registered address not the same as sign-up address.
- Introduce a front-end framework into the app to start improving the user experience
- Store any data as necessary
- Integrate with the Tariffscanner API to provide the business with an idea of current market rates `https://api.tariffscan.futureenergy.associates/docs#/general/get_best_value_tariffs_general_get_best_value_tariffs_post` 

API keys for both services above will be shared seperately.

Suggest some further improvements for these features and note how you would implement them.

## Notes

Please only spend a maximum of 2-3 hours on this task. We are not looking for a finished product, but rather a demonstration of your approach to solving problems and your ability to learn new technologies.

Feel free to include any other libraries, frameworks or scripts you feel are relevant to the task.  
Please document your process and any decisions you make in the README.md file.  
When you are finished, please send either a link to a public repository or a zip file of the project to your contact at Future Energy Associates.
