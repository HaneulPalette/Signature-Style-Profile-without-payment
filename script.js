let data = null;

async function analyze() {

    let file = document.getElementById("img").files[0];

    let form = new FormData();
    form.append("image", file);

    let res = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: form
    });

    data = await res.json();

    document.getElementById("p1").innerText = data.undertone;
    document.getElementById("p2").innerText = data.season;
    document.getElementById("p3").innerText = data.contrast;

    document.getElementById("preview").style.display = "block";
}

function openReport() {
    localStorage.setItem("report", JSON.stringify(data));
    window.open("luxury-report.html");
}
