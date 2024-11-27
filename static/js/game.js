let socket = new WebSocket('ws://' + window.location.host + '/ws/game/' + gameId + '/');

socket.onopen = function(e) {
    console.log("Connection to WebSocket established");
};

socket.onmessage = function(e) {
    let data = JSON.parse(e.data);
    console.log(data);  // Afficher la donnée reçue pour le débogage
    let updatedBoard = data.move;  // Plateau mis à jour envoyé par le serveur

    updateBoard(updatedBoard);
};

let selectedSquare = null;

function updateBoard(board) {
    const chessBoard = document.getElementById("chessBoard");
    const squares = chessBoard.getElementsByClassName("chess-square");

    board.forEach((row, rowIndex) => {
        row.forEach((square, colIndex) => {
            const index = rowIndex * 8 + colIndex;  // Calculer l'index de la case
            const div = squares[index];

            if (div.innerText !== square) {
                div.innerText = square || "";  // Mettre à jour la case uniquement si elle a changé
            }
        });
    });
}

function handleClickOnSquare(row, col) {
    if (selectedSquare) {
        // Si une case est déjà sélectionnée, déplacer la pièce
        movePiece(selectedSquare, { row, col });
        selectedSquare = null;  // Réinitialiser la sélection
    } else {
        selectedSquare = { row, col };  // Sélectionner la case
    }
}

function movePiece(from, to) {
    let move = {
        from: from,
        to: to
    };

    // Envoyer le mouvement au serveur via WebSocket
    socket.send(JSON.stringify({
        'move': move
    }));
}
