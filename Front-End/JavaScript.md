# Asynchronous vs Synchronous

#### Resources

- https://www.youtube.com/watch?v=Q-Zmc0E0GYY&t=35s



#### Synchronous

- Execute line by line, in the order of appearance
- Functions can be executed instantaneously, without even a chance of delay
- All synchronous functions are executed before any other asynchronous functions



#### Asynchronous

- Functions will happen at some point in the future, but JS doesn't immediately know exactly when that will be (NOT instantaneous; don't know exactly when the function will finish running).
- Instead of waiting for asynchronous functions to finish running, JS will continue on to the next line of code.
  - Asynchronous functions are temporarily "set aside" to come back to later, even if the delay time for a setTimeout is set to 0.
- Multiple asynchronous functions are executed in order (after all other synchronous functions)
- Promises act as "wrappers" around asynchronous functions
- Examples of asynchronous functions:
  - setTimeout
  - Callbacks
  - promises
  - fetch
  - Ajax
  - filesystem interaction
  - DOM event listeners



#### Example

```javascript
let s1 = (() => "001 1st synchronous func")();  // executed and returned
let s2 = () => "002 2nd synchronous func";     // definition only
console.log(s1);
console.log(s2());


let s3 = (n) => 5*n;
let s4 = () => 9;
console.log(`003 ${s3(s4())}`);


let a1 = 1000;
setTimeout(function(){
    a1++;
    console.log(`007 a1: ${a1} - 1st async`);   // 1st asynch. func
}, 0);
console.log(`004 a1: ${a1}`);
setTimeout(function(){
    console.log(`008 a1: ${a1}`);
}, 0);


let p = new Promise(function(resolve, reject){
    setTimeout(function(){
        resolve("Resolve Msg");
    }, 10);
});
console.log(p);       // 5th item printed
setTimeout(function(){
    console.log("009 or 010 promise")
    console.log(p);   // "pending" only if p hasn't been resolved at this point
}, 10);
console.log(p);       // 6th item printed; last synchronous function
p.then(function(val){
    console.log(`009 or 010 p.then ${val}`);  // executed as soon as p is resolved
});
```

Results:

```
001 1st synchronous func
002 2nd synchronous func
003 45
004 a1: 1000
Promise {<pending>}
Promise {<pending>}
007 a1: 1001 - 1st async
008 a1: 1001
009 or 010 p.then Resolve Msg
009 or 010 promise
Promise {<resolved>: "Resolve Msg"}
```







# Async Await

#### Resources

- https://www.youtube.com/watch?v=BTDeq5HC5bU (Intro)
- https://www.youtube.com/watch?v=lGJbPSI-12E (Async, Await with Promises)



#### `async` + function ==> promise

- adding `async` in front of a function turns that entire function into a promise
- adding `await` in front of an asynchronous function => wait until the particular line of code has finished executing, and then move on to the next line
  - `await` may only be used in an `async` function



#### Without `async` and `await`

```javascript
url = "https://koreanjson.com/posts/1"

const getData = function(){
    const response = fetch(url);
    const data = response.json();
    return "Return Value of getData"
}

console.log(getData());
```

- `fetch()` is an asynchronous function, so by the time JS reaches `response.json()`, `response` is merely a pending promise (as `fetch(url)` has been temporarily set aside). Thus `.json` is not a valid method of `response` at this point, resulting in a TypeError.



#### Adding `async` in front of the main function

##### BEFORE adding `async`:

```javascript
const getData = function(){
    return "Return Value of getData"
}
console.log(getData());
```

- `getData` is a synchronous function
- Result: `Return Value of getData`

##### AFTER adding `async`:

```javascript
const getData = async function(){
    return "Return Value of getData"
}
console.log(getData());
```

- `getData` is now a promise (asynchronous) which is instantaneously resolved
- Result: `Promise {<resolved>: "Return Value of getData"}`

```javascript
const getData = async function(){
    const response = fetch(url);
    console.log(response);           // [1] Promise {<pending>}
    const data = response.json();
    return "Return Value of getData"
}
console.log(getData());  // [2] Promise {<rejected>: TypeError}
```

- `getData` is a rejected promise, while `response` is a pending promise at the moment it is written to the console via `console.log(response)`.

```javascript
const getData = async function(){
    const response = await fetch(url);
    console.log(response);           // [2] Response object
    const data = await response.json();
    console.log(data);             // [3] {id: 1, title: "정당의 목적이나 활동이 ...
    return "Return Value of getData"
}
console.log(getData());         // [1] Promise {<pending>}
```

- `await`: wait until `fetch(url)` is completely executed, and then place the result in `response`. When `await` is omitted, `response` will hold a pending promise.
- `await` would replace `.then` calls















# Callback Functions

#### Resources

- https://www.youtube.com/watch?v=uPCxgnLOuiQ





- 
- a function that passes/returns another function to run





