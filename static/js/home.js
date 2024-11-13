function createParty() {
    fetch('/create_game', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ action: 'create' })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = '/join-party';
        } else {
            alert('Error creating party');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to create party');
    });
}
