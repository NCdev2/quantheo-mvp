import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.138.0/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.138.0/examples/jsm/controls/OrbitControls.js';

// Scene setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

document.body.style.margin = '0';
document.body.style.overflow = 'hidden';

const controls = new OrbitControls(camera, renderer.domElement);
camera.position.z = 5;

// Ball properties
const radius = 0.3;
const geometry = new THREE.SphereGeometry(radius, 32, 32);
const material1 = new THREE.MeshBasicMaterial({ color: 0xff0000 });
const material2 = new THREE.MeshBasicMaterial({ color: 0x0000ff });

const ball1 = new THREE.Mesh(geometry, material1);
const ball2 = new THREE.Mesh(geometry, material2);

scene.add(ball1);
scene.add(ball2);

ball1.position.x = -1;
ball2.position.x = 1;

// Initial velocities
let v1 = 0.02;
let v2 = -0.02;
let isElastic = true; // Toggle for collision type

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    
    ball1.position.x += v1;
    ball2.position.x += v2;

    if (Math.abs(ball1.position.x - ball2.position.x) < radius * 2) {
        if (isElastic) {
            // Elastic collision velocity swap
            [v1, v2] = [v2, v1];
        } else {
            // Inelastic collision: merge velocities
            let newV = (v1 + v2) / 2;
            v1 = newV;
            v2 = newV;
        }
    }
    
    renderer.render(scene, camera);
}
animate();

// Toggle collision type
window.addEventListener('keydown', (event) => {
    if (event.key === 'e') isElastic = true;
    if (event.key === 'i') isElastic = false;
});

// Export as collisions.js
export { animate };
