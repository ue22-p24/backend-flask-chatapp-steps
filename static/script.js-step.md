## retrieve nickname and subscribe to the channel

from then on, the nickname becomes accessible in the JS code, thanks to this
line, that inspects the `data-` attributes in the body tag of the HTML page:

```javascript
    // retrieve the nickname from the body tag
    const nickname = document.body.dataset.nickname
```

and from there, we can simply subscribe to the nickname channel, using the
`socket.on()` method like before
