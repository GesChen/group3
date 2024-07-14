// im aware this is a very bad way of doing it but shut up i dont have time for a better solution

const videoElements = document.querySelectorAll("video");
console.log(videoElements);
videoElements.forEach(function(video) {
    console.log("doing "+video.id);

    // Create a hidden checkbox toggle with the same ID
    const muteToggle = document.getElementById("cb"+video.id);

    // Attach the toggle functionality
    muteToggle.addEventListener("change", function() {
        video.muted = !muteToggle.checked;
    });
});