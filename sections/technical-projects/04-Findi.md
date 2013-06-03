I maintain a Python library for fetching your iPhone or other Apple device
from the FindMyiPhone API's.

It mocks a typical mobile request from an Apple application and
retrieves the meta data associated with the device.

This data includes latitude and longitude, which tracking over time
can reveal interesting data about the owner of the device in passive way
that doesn't affect battery life.

- A complete [post](http://pretengineer.com/post/tracking-iphone-location/) about findi on Pretengineer
- A [map](http://pretengineer.com/post/tracking-iphone-location/) created with the data from half a year of tracking my location
- findi on [Github](https://github.com/pearkes/findi)
- findi-heroku-example, an example of how to set-up a service to monitor
your location on [Github](https://github.com/pearkes/findi-heroku-example)

*Note: findi powers the location information in the sidebar of this website.*
