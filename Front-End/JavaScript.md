# Asynchronous vs Synchronous



Resources

- Synchronous vs Asynchronous: <https://www.youtube.com/watch?v=Q-Zmc0E0GYY&t=35s>
- Callback Functions: <https://www.youtube.com/watch?v=uPCxgnLOuiQ>
- Async Await: <https://www.youtube.com/watch?v=BTDeq5HC5bU>
- Async Await with Promises: <https://www.youtube.com/watch?v=lGJbPSI-12E>
- 







- synchronous: executing line by line, in the order they appear
- asynchronous: setTimeout, callbacks, promises, fetch, Ajax, filesystem interaction, DOM event listeners...
  - functions can't be instantaneously run
  - don't know exactly when the functions will complete running
    - asynchronous functions will happen at some point in the future, but JS doesn't know exactly when that will be.
  - instead of waiting for the function to finish running, JS will continue on to the next line of code, until the initial line is completed.
  - => asynchronous codes are temporarily "set aside" to finish later
    - even if the setTimeout delay time is set to 0
- JS runs all the synchronous codes first, and then goes back to take care of asynchronous codes.
  - Multiple asynchronous codes are executed in order







10:00



promises are "wrappers" around asynchronous functions









# Callback Functions

- a function that passes/returns another function to run





