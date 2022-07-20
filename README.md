# LikeTimeline

The main application is in ```/FlaskApp```, the requirements are specified in ```requirements.txt```

The application aims to retireve ***only tweets with images*** that were published between a given timeframe.
The application requires the usename and two dates as an input.

IMPORTANT: the application is not built for spying other Users' tweets likes/preferences( since it's possible to do it by default in the Twitter app), any abuse is the end user's responsibilty. 

Note that it can happen that the application does not visualize any tweet, since its possible that in the period selected, the user liked some tweets that were created outside the specified period.

To test it out:
- you need your Twitter Dev authentication keys to be set up as env variables.
- Install the requirements with ```pip install -r requirements.txt``` from the ```/info``` folder
- To execute in local the application, run ```python /FlaskApp/app.py```. It will run a server on```127.0.0.1:5000```
- Enjoy!

TO BE DONE:
 
-add a go back button from index

-add video player (https://www.codegrepper.com/code-examples/whatever/bootstrap+5+responsive+video)

-add a new function to discover the followed accounts of the user.

-general style polishing and efficiency
