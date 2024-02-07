
function encodeTextInput(event) {
    event.preventDefault()
    const text = document.getElementById('textarea').value;
    console.log(text);
    fetch('http://127.0.0.1:5000/process_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text_string: text })
    })
        .then(response => response.json())
        .then(data => {
            console.log('Response:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function encodeFileInput(event) {
    event.preventDefault();
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (event) {
            const text = event.target.result;
            fetch('http://127.0.0.1:5000/process_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text_string: text })
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Response:', data);

                })
                .catch(error => {
                    console.error('Error:', error);
                });
        };
        reader.readAsText(file);
    } else {
        alert('Please select a file.');
    }
}

function decodeFileInput(event) {
    event.preventDefault();
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function (event) {
            const text = event.target.result;
        
            fetch('http://127.0.0.1:5000/decode_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text_string: text })
            })
            .then(response => response.json())
            .then(data => {
                console.log('Response:', data);
                
            })
            .catch(error => {
                console.error('Error:', error);
                
            });
        };
        reader.readAsText(file);
    } else {
        alert('Please select a file.');
    }
}
const encodeTextButton = document.getElementById('upload1');
const encodeFileButton = document.getElementById('upload2');
const DecodeFileButton = document.getElementById('upload3');
encodeTextButton.addEventListener('click', encodeTextInput);
encodeFileButton.addEventListener('click', encodeFileInput);
DecodeFileButton.addEventListener('click', decodeFileInput);
