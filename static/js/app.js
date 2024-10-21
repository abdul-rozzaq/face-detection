const video = document.getElementById('videoElement');
const canvas = document.getElementById('canvasElement');
const img = document.getElementById('capturedImage');
const imageInput = document.getElementById('id_image') || document.getElementById('imageInput');
const imageForm = document.getElementById('imageForm');
const captureButton = document.getElementById('captureButton');
const resetButton = document.getElementById('resetButton');
const saveImageButton = document.getElementById('saveImage');


const reset = () => {
    img.src = "";
    img.style.display = 'none';
    video.style.display = 'block';
};


document.querySelector('[data-mdb-target="#camera-modal"]').addEventListener('click', () => {
    reset();

    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            video.srcObject = stream;
        })
        .catch((err) => {
            console.error("Kameraga kirish rad etildi yoki boshqa muammo yuzaga keldi: ", err);
        });
});


captureButton.addEventListener('click', () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imageDataURL = canvas.toDataURL('image/png');
    img.src = imageDataURL;

    img.style.display = 'block';
    video.style.display = 'none';
});


function dataURLToBlob(dataURL) {
    const binary = atob(dataURL.split(',')[1]);
    const array = [];
    for (let i = 0; i < binary.length; i++) {
        array.push(binary.charCodeAt(i));
    }
    return new Blob([new Uint8Array(array)], { type: 'image/png' });
}


saveImageButton.addEventListener('click', () => {
    const imageDataURL = canvas.toDataURL('image/png');
    const imageBlob = dataURLToBlob(imageDataURL);

    const file = new File([imageBlob], "captured_image.png", { type: 'image/png' });
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    imageInput.files = dataTransfer.files;

    if (imageForm) {
        imageForm.submit();
    }
});


resetButton.addEventListener('click', reset);