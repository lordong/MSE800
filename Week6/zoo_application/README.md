## Zoo application

1. Create the zoo application.

2. Admin logs in to the system.

3. Admin views action, such as feeding the lions.

4. Admin logs out of the system.

## All the above functions use the decorator to print the activities' time.

The system will use the function as a parameter to call the decorator's function, and the decorator builds an inside function, then returns it. This inside function will be called directly, and prints some information about the activities, then calls the original function.
