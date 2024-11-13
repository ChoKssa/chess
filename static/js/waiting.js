let dots = document.getElementById("dots");
let dotCount = 1;

setInterval(() => {
    dots.textContent = '.'.repeat(dotCount);
    dotCount = (dotCount % 3) + 1;
}, 500);

function cancelParty() {
    window.location.href = "/";
}
