# c-Clickr

This is a mirrored repository of a group project. I worked mainly on the pattern design and Android app.

[Click here for the YouTube demo video](https://www.youtube.com/watch?v=jtZS6DpiGlQ&t=3s)

### Overview
Designed to be an i-clicker replacement for uiuc students. Students download an app to visually display their uin with an array of colored boxes. A camera in the
front of the room is then able to pick up all the different arrays on each student's phone. Behind the scenes, we convert the colored arrays back to uins using
computer vision algorithms and the teacher is able to see a list of all the present uins in a table format.

### MVP
Our minimum viable product was an app that could pick up the colored code from one phone in ideal conditions, convert the code to a uin, and then send the uin to 
a front end so the teacher can see who is present and not present. We also wanted to create a simple app to display the user's unique color code given their uin.

### Pipeline
    1. Student downloads our application that creates their unique color code from a given uin and displays the color code on their screen
    2. IPCamera picks up android camera feed and sends it wirelessly to a computer using Selenium. This camera is pointed at the student's phone showing the color code.
    3. Our python backend picks up the camera data and identifies where the student's phone is. It is then able to process the color code and convert it back into a uin.
    4. The uin is sent to a firebase server where it is stored under the current date and that student is marked present.
    5. The teacher views a React front end with a dropdown where they can choose a date and see the attendance for that date.

### Technologies and Methods
Backend:
- opencv
- pillow image processing
- imutils
- bilateral filtering
- gaussian blur
- firebase

Frontend:
- React
- Bootstrap
- lodash
- npm

### To Run
`npm start` from the `web-frontend` directory

Set up camera (can use ipcamera or computer webcam)

`python colorcoordinates.py` from the `Backend` directory
