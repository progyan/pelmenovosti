let lowercase_names = {
    "Пельмень": "пельменя",
    "Бойстул": "бойстула",
    "Ян": "яна"
};
fetch("/getuser")
    .then((resp) => { resp.text().then((user) => { 
        if (user == "Гость") {
            alert("ты слишком чужой = нельзя");
            window.location.href = '../main/index.html';
        }
        document.getElementById("c-name").innerText = lowercase_names[user];
        document.getElementById("creator-name").innerText = "-- " + user; 
        document.getElementById("face").src = "../faces/" + user + ".jpg"
    }) });

function submitNews() {
    let newsType = document.getElementById("news-type").value;
    let title = document.getElementById("title").value;
    let text = document.getElementById("text").value;
    fetch("/getuser")
        .then((resp) => { resp.text().then((user) => {        
            let result = [user, title, text, newsType];
            console.log(result);
            fetch("/addnews", { 
                'method': "post", 
                'headers': {
                    'Content-Type': 'application/json'
                },      
                'body': JSON.stringify(result)
            }).then((resp) => { window.location.href = '../main/index.html' });
        }) 
    });
}

