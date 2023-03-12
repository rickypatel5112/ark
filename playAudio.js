const audio = new Audio();

const audioUrl = "http://localhost:5000/audio";
fetch(audioUrl)
    .then(response => response.blob())
    .then(blob => {
        audio.src = URL.createObjectURL(blob);
        audio.autoplay = true;
        audio.controls = true;
        document.body.appendChild(audio);
    })
    .catch(error => console.log(error));