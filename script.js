function encodeTextInput() {
    const text = document.getElementById('textarea').value;
    // const encodedText = encodeText(text);
    // displayResult(encodedText)
    console.log(text);
}

function encodeFileInput() {
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];
    
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const text = event.target.result;
            console.log(text);
            // const encodedText = encodeText(text);
            // displayResult(encodedText);
        };
        reader.readAsText(file);
    } else {
        alert('Please select a file.');
    }
}
const encodeTextButton = document.getElementById('upload1');
const encodeFileButton = document.getElementById('upload2');
encodeTextButton.addEventListener('click', encodeTextInput);
encodeFileButton.addEventListener('click', encodeFileInput);
// function encodeText(text) {
//     // Implement Huffman encoding logic here
//     // You can call your existing encoding functions
//     // and return the encoded result.
//     return "Encoded result: " + text.toUpperCase(); // Example encoding
// }

// function displayResult(result) {
//     const encodedResultDiv = document.getElementById('encodedResult');
//     encodedResultDiv.innerHTML = "<p>" + result + "</p>";
// }