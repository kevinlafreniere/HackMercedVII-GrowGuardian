# GrowGuardian (for HackMerced VIII)
A project aiming to provide live crop detection that uses climate sensors to determine effective crop yields.

## Inspiration
Merced is located in the Central Valley where agriculture is a defining feature of the area. However, _climate conditions greatly affect which crops can be grown_ throughout the season. I wanted to create a convenient way for someone to get live visual feedback on the crops in their area and whether they are suited for the climate conditions at the time.

## What it does
The service gathers temperature and humidity data through an Arduino. The sensor data is relayed to a computer that is tracking and labelling crops it identifies through a visual interface. The crop will be labeled and colored to inform the user whether the crop is in an ideal climate or not.

## How we built it
The project was built using an **Arduino** with a DHT11 sensor that tracks humidity. The computer uses a Python script that communicates with the Arduino through the serial port, whilst also using the webcam and labelling crops it identifies. The live crop detection was accomplished with **OpenCV** and pre-trained **machine learning** models.

## Challenges we ran into
The most difficult challenges were communicating the climate data to the computer as well as getting a machine learning model to identify the crops. Communicating the climate data was accomplished through Python's built-in socket functionality. Getting the machine learning model for the crops proved to be a difficult task under the time constraints, so the best alternative was to use more readily accessible models that track everyday objects.

## Accomplishments that we're proud of
The thing that gave the best feeling of accomplishment was communicating the Arduino data to the computer. Initially the project had the climate data gathering and live object detection features separate, so it felt good to get them working together cohesively in the end.

## What we learned
This hackathon brought me to learn about live object detection in Python which always seemed daunting, but the libraries can be easy to use once everything is set up. I also learned how to communicate through serial ports and sockets, an uncommon task for me.

## What's next for GrowGuardian
The natural next steps for the project is to integrate specially trained models to identify important crops, along with the ideal climate conditions for them.
