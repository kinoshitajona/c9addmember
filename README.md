# c9addmember

A simple web app to send users to invite themselves to your c9 team.

## Setup

This web app is designed to be run on heroku. This can be easily set up to run on a free account or hobbyist account.

1. Sign up for a free account on github.com. This account and the repository used will not be explicitly shown to the user who is given only the app URL. However, it must be public, so do not assume it will not be found. As such, no secret info will be committed to the repository.
2. Sign up for a free account on heroku.com. This account will also not be apparent to the user. Secret info will be copy pasted into the web app project's environment variables directly.
3. While logged into github, click on the "Fork" button on the upper right hand corner of this repository you are reading right now.
4. Now, log in to heroku, go to the dashboard and click "New" > "Create New App"
5. Choose the app name, this will decide the URL to the web app: ex. if the app name is "example", then example.herokuapp.com will be your URL.
6. Choose Runtime Selection between US servers or EU servers, the one closest should be fine.
7. Click Next, then for Deployment method, click Github.
8. It will ask you to connect your Github account, click the button to connect them.
9. Once connected, select your github user in the dropdown box and type in `c9addmember` in the text box next to it.
10. Click Search, then click Connect when the repo is shown.
11. Once connected, click on the "Settings" button on the top center just below your app name in the header.
12. Click on "Reveal Config Vars" next to the "Config Variables" section.
13. Add the following 5 `"key": "value"` pairs:
    * `"C9_USER_NAME": "yourc9username"` # This is the c9 user name of an admin on the team.
      * I recommend inviting a new dummy user and making it admin for your team and using that account. That way even if this user's credentials is stolen by heroku, your main account's private workspaces etc. will not be compromised.
    * `"C9_PASSPHRASE": "yourc9password"` # If it contains \\, please write \\\\ instead.
    * `"C9_TEAM_NAME": "yourteamname"` # In team admin console, this is what is in the URL.
      * ex. https://c9.io/team/yourteamname/manage would be `yourteamname`
    * `"HEROKU_DOMAIN_NAME": "yourwebapp.herokuapp.com"` # This should be the name you gave your webapp
    * `"DISABLE_COLLECTSTATIC": "1"` # Always 1.
14. Click on the Deploy button on the main tool bar below your app name.
15. Scroll to bottom and click "Deploy Branch" on the "Manual Deploy" section. This will deploy the master branch.
16. Optional: Enable Automatic Deploys to have Heroku update the web app every time you make a change to github.

## Test your app

Your app will now be available at https://yourwebapp.herokuapp.com/
Enter any email address into the box and click the button, it will say SUCCESS if you were successfully invited to the team.
