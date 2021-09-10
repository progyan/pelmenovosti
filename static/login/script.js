function toggleVisibility() {
    let x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

function submitLogin() {
    let login = document.getElementById("login").value.slice(4);
    let password = document.getElementById("password").value;
    console.log(login, password);
    fetch("/login", { 
        'method': "post", 
        'headers': {
            'Content-Type': 'application/json'
        },      
        'body': JSON.stringify([
            login, password
        ])
    }).then((resp) => {
        console.log(resp) 
        resp.json().then((t) => {
            if(t == "OK") {
                alert("Добро пожаловать к пельменям.");
                window.location.href = '../main/index.html';
            } else {
                alert("Неправильный пароль. Проверьте правописание и свою трезвость.");
            }
        })
    })
}