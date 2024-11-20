const csrftoken = document.querySelector("[name=csrf-token]").content;

function createParty() {
	fetch("games/new/", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
			"X-CSRFToken": csrftoken,
		},
		body: JSON.stringify({ action: "create" }),
	}).then((response) => (window.location.href = response.url));
	// .then((data) => {
	// 	window.location.href = "/games/game/4";
	// })
	// .catch((error) => {
	// 	console.error("Error:", error);
	// 	alert("Failed to create party");
	// });
}
