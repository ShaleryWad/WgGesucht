## WgGesucht
Script which updates the ads listed on WgGesucht

### Getting Started:
Currently only the Firefox webdriver is supported. In order to use other browsers too you have to download the specific drivers (e.g. Chrome: https://sites.google.com/chromium.org/driver/) and unpack them. Next you to add the path where the unpacked driver is stored to the environemnt variable setting (add path to PATH). In the script code you only have to replace the browser.Firefox() with e.g. browser.Chrome().

### Adjusting Login-Info:
Adjust the username and password info. At last you only have to update the ads-array with the specific ad_ids (Lookup in Page-URL)

### To-Do's:
-  Testing
-  Support for other browsers
-  Setting up a "how to" to turn it into a batch file and add it to the task scheduler
