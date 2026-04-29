let reportData = null;

async function analyze() {

    let file = document.getElementById("imageUpload").files[0];

    if (!file) {
        alert("Upload image first");
        return;
    }

    let formData = new FormData();
    formData.append("image", file);

    let res = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: formData
    });

    reportData = await res.json();

    document.getElementById("p1").innerText = reportData.undertone;
    document.getElementById("p2").innerText = reportData.season;
    document.getElementById("p3").innerText = reportData.contrast;

    document.getElementById("preview").classList.remove("hidden");
}

function openReport() {

    if (!reportData) {
        alert("Analyze first");
        return;
    }

    localStorage.setItem("reportData", JSON.stringify(reportData));

    window.open("luxury-report.html");
}
