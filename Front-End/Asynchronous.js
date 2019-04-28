let s1 = (() => "001 1st synchronous func")();  // s1: return value of executed function
let s2 = () => "002 2nd synchronous func";     // s2: function definition (to be executed later)
console.log(s1);
console.log(s2());


let s3 = (n) => 5*n;
let s4 = () => 9;
console.log(`003 ${s3(s4())}`);


let a1 = 1000;
setTimeout(function(){
    a1++;
    console.log(`007 a1: ${a1} - 1st async`);   // first asynchronous function
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
    console.log(p);   // "pending" only if p has not been resolved at this point
}, 10);
console.log(p);       // 6th item printed; last synchronous function
p.then(function(val){
    console.log(`009 or 010 p.then ${val}`);  // executed as soon as p is resolved
});