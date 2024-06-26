document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('uploadMessage').innerText = 'File uploaded successfully!';
        } else {
            document.getElementById('uploadMessage').innerText = data.message || 'Failed to upload file.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('uploadMessage').innerText = 'file uploded.';
    });
});
