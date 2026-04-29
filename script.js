let userData = {};

function analyze() {

    // 🔥 (Later replace with AI model)
    userData = {
        name: "Client",
        undertone: "Warm Peach",
        season: "Soft Autumn",
        contrast: "Low-Medium",

        colors: ["#A67B5B", "#C2A083", "#E6C7A8", "#8B6F47"],

        recommend: "Earth tones, muted gold, warm neutrals, soft fabrics.",
        avoid: "Neon colors, harsh black-white contrast."
    };

    // show preview
    document.getElementById("pUndertone").innerText = userData.undertone;
    document.getElementById("pSeason").innerText = userData.season;
    document.getElementById("pContrast").innerText = userData.contrast;

    document.getElementById("preview").classList.remove("hidden");
}


function openReport() {

    localStorage.setItem("reportData", JSON.stringify(userData));

    window.open("luxury-report.html", "_blank");
}
