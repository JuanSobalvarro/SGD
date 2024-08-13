const el = document.getElementById('ttr');
const height = el.clientHeight;
const width = el.clientWidth;

el.addEventListener('mousemove', (e) => {
    const xVal = e.layerX;
    const yVal = e.layerY;

    const yRotation = 80 * ((xVal - width / 2) / width);
    const xRotation = -80 * ((yVal - height / 2) / height);

    const string = 'perspective(500px) scale(1.1) rotateX(' + xRotation + 'deg) rotateY(' + yRotation + 'deg)';

    el.style.transform = string;
});