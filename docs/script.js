
const BACKEND_URL = "http://127.0.0.1:5000";

function analyze() {

    let file = document.getElementById("imageInput").files[0];

    let formData = new FormData();
    formData.append("image", file);

    fetch(BACKEND_URL + "/analyze", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {

        document.getElementById("preview").innerHTML = `
            <h3>Preview</h3>
            <p>${data.preview}</p>
        `;
    });
}

function downloadPDF() {

    fetch(BACKEND_URL + "/pdf")
    .then(res => res.blob())
    .then(blob => {

        let url = window.URL.createObjectURL(blob);
        let a = document.createElement("a");
        a.href = url;
        a.download = "Haneul_Palette_Report.pdf";
        a.click();
    });
}
