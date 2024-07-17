# IOT-Project
This is the main code which all the function's takes place 
#These are the Libraries used in the code:
The code utilizes the following libraries:

* *google.auth.transport.requests:* For making authenticated requests to Google APIs.
* *google.oauth2.credentials:* For handling OAuth2 credentials for authentication with Google services.
* *google_auth_oauthlib.flow:* For implementing the OAuth2 authorization flow to obtain user consent for accessing Google Calendar data.
* *googleapiclient.discovery:* For building a client to interact with the Google Calendar API.
* *pyttsx3:* For text-to-speech conversion, allowing the script to read calendar events aloud.
* *RPLCD.i2c:* For controlling an I2C character LCD display, which is used to display event information.
* *time:* For adding delays (sleep) between actions.
* *pygame:* For playing a sound when an event is starting.
* *datetime:* For working with dates and times, such as getting the current time and parsing event start times.
* *os:* For interacting with the operating system, like checking if the token file exists.

*Key functionalities enabled by these libraries:*

* *Google API Interaction:* The google libraries enable the script to authenticate with Google services (using OAuth2) and access the Google Calendar API to fetch event data.
* *Text-to-Speech:* The pyttsx3 library allows the script to verbally announce the details of upcoming events.
* *LCD Display:* The RPLCD.i2c library facilitates the display of event information on an LCD screen connected via I2C.
* *Sound Playback:* The pygame library plays a sound to notify the user when an event is starting.
* *Time Management:* The datetime and time libraries handle time-related tasks like getting the current time, parsing event times, and introducing delays.
* *File Operations:* The os library helps check if the authentication token file exists and manage it.
