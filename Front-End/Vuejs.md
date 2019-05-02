# Terminology

`const app = new Vue({})`

- creating a new instance

el, data, methods, computed, watch, filter ... => options







# Options

### data

- may be accessed as `app.$data`



### component 

- reusable modules



### methods

- all defined functions run whenever any changes are detected (regardless of whether or not the change will directly affect the function's results)
  - c.f) **computed** functions will run only when necessary (when the specifically-linked value changes)
  - 
- need a direct action from a user (i.e. event) (c.f computed will run based on data changes)
- `<p>{{ addValues() }}</p>` => render whatever return value of method `addValues`





### computed

- computed functions are defined in almost the same way as methods functions
- `<p>{{ addValues }}</p>` => render whatever return value of method `addValues`
  - (no parentheses appended to the function name)
- compared with methods functions, computed functions only run when needed
  - has the ability to check if one of their dependencies has changed (if there is no change, function will not necessarily rerun as the function result will not have changed)
    - computed functions have cache (which would store the most recent function status), whereas methods don't (which is why they rerun every time without attempting to see if there have been any changes in the first place)
  - thus at times, more efficient than methods functions
- used for synchronous tasks (for asynchronous tasks, use a combination of methods + watch)  => results will be displayed immediately after the computation
- needs a return value





### filter









### created: function()



### mounted: function()





### updated: function()





### destroyed: function()









# Directives

### v-if   vs  v-show

- `v-if` // `v-else-if`   /// `v-else`
- both are dependent on conditions
- `v-if`: component is NOT rendered into the HTML document at all.
- `v-show`: component _is_ rendered into HTML, but set as `display = none`





### v-model

- controls value of input tags (text, radio, textarea, select, ...)
- will ignore the initial value, checked, or selected attributes should there be any changes made to the input after the HTML document loads.
  - (initial value may be specified inside the `data` option of the Vue instance)



### v-bind

- used with: src, class, style, disabled, ...
- short-hand: 
  - v-bind:src ==> :src
- dynamically changing classes depending on specified condition
  - e.g) `:class="{red: email.length < 2}"` => assign class `red` whenever email length is less than 2
- 





### v-text   vs   v-html   vs   v-once

- similar to using the `{{  }}` syntax when it comes to rendering text
- `<p> {{ sample }} </p>`   <=>  `<p v-text="sample"></p>`

- `v-html` will parse any html tags included, such as `<h1>`
- `v-once` : only shows the initial value, even if any changes are made afterwards (not updated)



### v-for

- for loops



### v-on + events

- events: click, keyup, keydown, ...
  - click.prevent.stop...   (stopPropagation ...)
- shorthand:  `v-on:click` ==> `@click`
- add function in `methods`













