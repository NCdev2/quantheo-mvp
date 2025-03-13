// Newton's First Law Simulation using Three.js
import * as THREE from 'https://unpkg.com/three@0.146.0/build/three.module.js';
import { OrbitControls } from 'https://unpkg.com/three@0.146.0/examples/jsm/controls/OrbitControls.js';

// Scene setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Lighting
const light = new THREE.AmbientLight(0xffffff);
scene.add(light);

// Create ground plane
const groundGeometry = new THREE.PlaneGeometry(10, 10);
const groundMaterial = new THREE.MeshStandardMaterial({ color: 0x808080 });
const ground = new THREE.Mesh(groundGeometry, groundMaterial);
ground.rotation.x = -Math.PI / 2;
scene.add(ground);

// Create moving object (sphere)
const geometry = new THREE.SphereGeometry(0.3, 32, 32);
const material = new THREE.MeshStandardMaterial({ color: 0xff0000 });
const ball = new THREE.Mesh(geometry, material);
ball.position.set(0, 0.3, 0);
scene.add(ball);

// Camera position
camera.position.set(0, 2, 5);

// Controls
const controls = new OrbitControls(camera, renderer.domElement);

// Motion parameters
let velocity = 0.02; // Initial velocity
let friction = 0.99; // Resistance factor
let moving = true;

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    
    if (moving) {
        ball.position.x += velocity;
        velocity *= friction; // Slow down due to friction
        if (Math.abs(velocity) < 0.001) moving = false; // Stop motion
    }
    
    controls.update();
    renderer.render(scene, camera);
}
animate();

// UI Controls (Buttons)
const stopButton = document.createElement("button");
stopButton.innerText = "Stop Motion";
stopButton.style.position = "absolute";
stopButton.style.top = "10px";
stopButton.style.left = "10px";
document.body.appendChild(stopButton);
stopButton.addEventListener("click", () => {
    moving = false;
});

const startButton = document.createElement("button");
startButton.innerText = "Start Motion";
startButton.style.position = "absolute";
startButton.style.top = "40px";
startButton.style.left = "10px";
document.body.appendChild(startButton);
startButton.addEventListener("click", () => {
    moving = true;
    velocity = 0.02;
});
