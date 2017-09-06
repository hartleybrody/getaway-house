# Find a Getaway House

The goal of this project is to create an ETL pipeline (Extract, Transform, Load) that takes in a list of lakes in various US states and incrementally adds data about those lakes and the nearby homes for sale and filters everything down until we have a few candidate properties that are worth looking into.

Some filters we want to have for lakes

- lake size between 50 and 1000 acres
- lake can be natural or man-made (ie reservoir)
- lake should be 1-6 hours from hometown

Some filters we want to have for the property

- property should be "waterfront" or "lakefront", shouldn't be down the street or require driving/parking
- property should have 3 or more bedrooms
- property should be recently updated
- property should be between $100k and $500k USD

## Steps:

Using the `scripts` directory, we start with copy/pasted value from wikipedia's list of lakes for Ohio in `get_lakes.py`.

From there, we look up geocoding information to get lat/lon pairs for each lake based on the town name in `geocode.py`.

Finally, we [upload the CSV with the lat/lon pairs to a new Google My Map](https://support.google.com/mymaps/answer/3024836?vid=0-795295964273-1504581025568), [for visual analysis here](https://www.google.com/maps/d/edit?mid=1gwxkbn109jMqNndiCNtJJYCCXjQ&ll=41.16764219675483%2C-81.50702766595617&z=9).

## To Do:

1. Add lists of lakes from nearby Pennsylvania, New York and Michigan
1. Instead of visualizing the lakes on a map, look each lake up to get its driving distance from hometown via some API (which one?)
1. Use the Zillow API to look up 3 bedroom properties in the area of each lake
1. Filter properties based on "waterfront", recently updated, price, etc