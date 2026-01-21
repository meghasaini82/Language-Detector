function detectTranslate() {
    const text = document.getElementById("inputText").value;

    fetch("http://127.0.0.1:5000/detect_translate", {   // THIS MUST BE SAME
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    })
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
                return;
            }

            document.getElementById("langOutput").textContent = data.detected_language;
            document.getElementById("translationOutput").textContent = data.translated_text;
        })
        .catch(err => console.log(err));
}
