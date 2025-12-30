# spotlight README

## v0
Specifically target the `addEventListener` use case:

cursor is inside the block which defines the callback behavior for the eventListener

We can infer that the DOM element is defined somewhere previously in the js file since the function is called on the element.

Utilize `executeDocumentSymbolProvider` to find the definition of the element, then grab the ID if applicable (could be found via class or element type etc) 

Also utilize `executeDocumentSymbolProvider` to find definitions for any other functions used inside of the eventListener callback

Check HTML for the ID found above, and highlight the element to which the eventListener is being applied, and a tier_2 highlight if it's within some type of containing element (div). NOTE: this means we probably want some type of tree repr of the HTML doc.



"Train the spotlight" -> command in the palette which looks at a bunch of different rules given the highlighted word as input.
    Each rule is a "filter" you can add (like a filter lense over a spotlight).
    AKA: each can be individually added or removed as a config activity.

    Individual rule examples:
    - if (isJSFile && contents.contains('document.getElementById')) {  find HTML file, check for element w/ id, highlight container_or_self()  }
    - if (isJSFile && contents.contains('classList')) {  find CSS file, check for '.<class_name>', highlight '{...}'  }




_____________________
## what to target?
Want to define references relative to the current block within which the cursor resides. Don't necessarily want to highlight refs for a single line of code - e.g. when a developer is working on the contents of the callback for an event listener, we want to find references for the object to which the event listener is tied.

```javascript
const button = document.getElementById("button-id");

button.addEventListener(
    "click", 
    () => {
        console.log("Hello, World!"); // cursor on this line
    }
);
```

In the above example, we don't want to  look for references to console, we want what that block of code is operating on from the developer's perspective (e.g. `button#button-id`)




```javascript
const button = document.getElementById("button-id");

const callback = () => {
    console.log("Hello, World!"); // cursor on this line
}

button.addEventListener(
    "click", 
    callback
);
```

In the above example, when working on the `callback` function, we'd expect both the event listener and the button in our HTML file to be highlighted for focus.

NOTE: tiered levels of opacity to indicate distance from current cursor's focus? The event listener code would have the highest tier focus, and the button definition, as well as button references in other files would have the next tier down (slightly dimmer) level of focus. This can visually indicate how tightly/loosely different sections of code are tied together. Allow config of depth here - how many tiers of references do we want to be looking for currently? How emphatic do we want the visual indicator to be for the different tiers?


-----

What if the cursor is currently in a block such as: 
- an event listener which references several components in the DOM?
- a function 

 Make a determination of if there's a sub-scope of the HTML which contains all of those references, or do we need to highlight a couple different sections? How to indicate which ref matches where?