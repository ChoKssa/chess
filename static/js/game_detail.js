var ws = new WebSocket("ws://" + "127.0.0.1:8001" + "/ws/game/1/");
ws.onmessage = function (event) {
	console.log("Message from server ", event.data);
};
ws.onopen = function (event) {
	ws.send(JSON.stringify({ type: "test" }));
};
