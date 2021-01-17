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
        //.then(data => document.getElementById('test').innerHTML = data)
        .then(data => {for(i = 0; i < 9; i++) {
        output.innerHTML += `
        <p>${data[i]}</p>
        `}})
        .catch(err => { console.log(err) })
    });