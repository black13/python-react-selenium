1. create a react application:
    npm init react-app ./calculator
2. this will create a basic calculator app.
   send keys to the calculator and check result.
3. send result to github.
4. the sources required significant clean up:
   a. delete modules directory remove the 
   b. del package-lock.json yarn.lock
   c. npm audit fix --force
5. you will need to download the drive for edge.
    Chrome:	  https://sites.google.com/chromium.org/driver/
    Edge:	  https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    Firefox:  https://github.com/mozilla/geckodriver/releases
    Safari:	  https://webkit.org/blog/6900/webdriver-support-in-safari-10/
   
   https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   find the correct driver for the version of edge you have.

https://stackoverflow.com/questions/49828493/upgrading-react-version-and-its-dependencies-by-reading-package-json
python setup: create a virtual environment.

pip.exe install selenium


notes:
how to check if npm web server is running:
C:\Users\me\projectdir>netstat -ano | findstr :3000
  TCP    0.0.0.0:3000           0.0.0.0:0              LISTENING       number
  TCP    127.0.0.1:3000         127.0.0.1:53856        TIME_WAIT       0
  TCP    127.0.0.1:3000         127.0.0.1:53857        TIME_WAIT       0
  TCP    127.0.0.1:3000         127.0.0.1:53858        TIME_WAIT       0

C:\Users\me\projectdir>taskkill /PID number /F
SUCCESS: The process with PID 18172 has been terminated.

C:\Users\me\projectdir>netstat -ano | findstr :3000