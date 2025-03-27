const ws = new WebSocket('ws://' + window.location.host + '/ws/sc/');

ws.onopen = function () {
    console.log('Websocket Connected.')
    ws.send('Hello, Server!')
}

ws.onmessage = function (event) {
    console.log('Message Received From Server:', event)
    document.getElementById("cnt").innerText = "Counting:" + event.data
}

ws.onerror = function (event) {
    console.log('Websocket Error Occurred:', event)
}

ws.onclose = function (event) {
    console.log('Websocket Disconnected:', event)
}
