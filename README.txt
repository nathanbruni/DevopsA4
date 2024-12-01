This is a website blocker application that adds the url of any website beginning with "www." to the hosts file with a preceeding "127.0.0.1".

This application only works in Windows since it uses a Windows only absolute path to get to the file. 
The application must be run as an administrator in order for the application to write to the file properly.

The application will prompt the user for a website. One the website is entered, the application will ask the user if they would like to add additional websites.
If Y is selected, the application will prompt for another website. Note - if the website does not begin with "www.", the application will throw an exception and crash.

If N is selected, the application will prompt the user for if they would like to block the website or unblock the website.
If B is selected, the website is added to the hosts file. If U is selected, the website is removed from the hosts file.

Once a website has been added, the program must run again with the unblock option selected to be able to visit the website again.

In order for the website blocker to work properly, it is recommended the user clear their browser cache or use their browser in incognito mode.

Enjoy!

GitHub repository: https://github.com/nathanbruni/DevopsA4
Docker Hub Image (Pull Command): docker pull nathanbruni/website_blocker.v7
Docker Hub Image URL: https://hub.docker.com/r/nathanbruni/website_blocker.v7

Note: Does not run well from Docker container. The image should have some function in interactive mode but because Docker runs through Linux, the code will not function properly.
For proper function, please download the code from GitHub and run on a Windows based IDE.
