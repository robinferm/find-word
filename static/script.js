const input = document.getElementById('input');
const output = document.getElementById('output');

document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault();    //stop form from submitting

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(input.value)
    }).then(response => {return response.json() })
    .then(data => { printMatrix(data) })
    .catch(err => { console.log(err) })
});


function printMatrix(data) {

    // Clear output
    output.innerHTML = ""
    const regex = /[a-z]/;

    for(i = 0; i < data.length; i++) {

        // Create rows
        output.innerHTML += `<tr id="row${i}">`

        // Add characters to rows
        for(j = 0; j < data.length; j++) {

            // Set unique IDs for each row
            row = document.getElementById(`row${i}`)

            // If character is lower case (if word is found), set highlight class and change to upper case
            if (regex.test(data[i][j])) {
                row.innerHTML += `<td class="highlight">${data[i][j].toUpperCase()}</td>`
            }
            else {
                row.innerHTML += `<td>${data[i][j]}</td>`
            }

        }
        output.innerHTML += `</tr>`
    }
}