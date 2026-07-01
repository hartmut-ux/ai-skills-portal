/**
 * Programmatic Infographics - p5.js Generator Template
 *
 * This template demonstrates best practices for building generative algorithms
 * with seeded randomness and parametric control.
 *
 * NOTE: This file is a REFERENCE for code organization and principles.
 * Embed your algorithms directly in the HTML artifact (templates/viewer.html),
 * do NOT create separate .js files.
 */

// ============================================
// PARAMETER DEFINITION
// ============================================
// Always define parameters that emerge naturally from your algorithm's philosophy.
// Consider: "What qualities of this system can be adjusted?"

const createParams = () => {
    return {
        seed: 12345,              // ALWAYS include seed for reproducibility
        // Quantity parameters
        particleCount: 150,       // How many particles/elements?
        // Scale parameters
        scale: 1.0,               // Global scale factor
        noiseScale: 0.005,        // Perlin noise frequency
        // Behavioral parameters
        velocity: 2.5,            // Movement speed
        // Visual parameters
        opacity: 200,             // Transparency (0-255)
        // Color parameters (if applicable)
        hueShift: 0,              // Color variation
    };
};

// ============================================
// SETUP & INITIALIZATION
// ============================================
// Initialize canvas and random seeds for reproducibility

function initializeSketch(p, params) {
    p.createCanvas(1200, 1200);

    // CRITICAL: Always apply seed BEFORE any random operations
    p.randomSeed(params.seed);
    p.noiseSeed(params.seed);

    // Initialize algorithm-specific data structures
    return {
        particles: generateParticles(p, params),
        time: 0,
    };
}

// ============================================
// GENERATIVE ALGORITHM STRUCTURE
// ============================================

/**
 * Example: Particle System with Noise Field
 * This demonstrates how to structure a generative algorithm.
 */

class Particle {
    constructor(p, params, x, y) {
        this.p = p;
        this.x = x || p.random(p.width);
        this.y = y || p.random(p.height);
        this.vx = 0;
        this.vy = 0;
        this.age = 0;
        this.maxAge = p.random(200, 500);
    }

    update(p, params, noiseValue) {
        // Example: move based on noise field
        const angle = noiseValue * Math.PI * 2;
        this.vx += Math.cos(angle) * params.velocity;
        this.vy += Math.sin(angle) * params.velocity;

        // Apply friction
        this.vx *= 0.98;
        this.vy *= 0.98;

        this.x += this.vx;
        this.y += this.vy;
        this.age++;

        // Boundary wrapping
        if (this.x < 0) this.x = p.width;
        if (this.x > p.width) this.x = 0;
        if (this.y < 0) this.y = p.height;
        if (this.y > p.height) this.y = 0;
    }

    display(p, params) {
        const opacity = params.opacity * (1 - this.age / this.maxAge);
        p.fill(p.color(50, 150, 255, opacity));
        p.noStroke();
        p.ellipse(this.x, this.y, 4 * params.scale);
    }

    isAlive() {
        return this.age < this.maxAge;
    }
}

function generateParticles(p, params) {
    const particles = [];
    for (let i = 0; i < params.particleCount; i++) {
        particles.push(new Particle(p, params, p.random(p.width), p.random(p.height)));
    }
    return particles;
}

// ============================================
// RENDER FUNCTION
// ============================================
// Core drawing loop that expresses the algorithm

function drawAlgorithm(p, params, state) {
    p.background(255, 20);  // Slight transparency for trails

    // Example: iterate over particles and apply noise-field behavior
    state.particles.forEach(particle => {
        // Get noise value at particle position
        const nx = particle.x * params.noiseScale;
        const ny = particle.y * params.noiseScale;
        const nt = state.time * 0.01;
        const noiseValue = p.noise(nx, ny, nt);

        // Update and display
        particle.update(p, params, noiseValue);
        particle.display(p, params);
    });

    // Remove dead particles and spawn new ones
    state.particles = state.particles.filter(p => p.isAlive());

    const particlesToAdd = params.particleCount - state.particles.length;
    for (let i = 0; i < particlesToAdd; i++) {
        state.particles.push(new Particle(p, params));
    }

    state.time++;
}

// ============================================
// MATHEMATICAL PATTERNS & TECHNIQUES
// ============================================

/**
 * Flow Field: Invisible vector field guiding particles
 * Use this when philosophy is about "forces made visible"
 */
function createFlowField(p, params, resolution = 10) {
    const field = [];
    for (let i = 0; i < p.width; i += resolution) {
        for (let j = 0; j < p.height; j += resolution) {
            const angle = p.noise(i * params.noiseScale, j * params.noiseScale) * Math.PI * 2;
            field.push({
                x: i,
                y: j,
                angle: angle,
                vx: Math.cos(angle),
                vy: Math.sin(angle)
            });
        }
    }
    return field;
}

/**
 * Recursive Structures: Self-similar patterns across scales
 * Use this when philosophy is about "self-similarity" or "fractals"
 */
function drawRecursiveTree(p, x, y, length, angle, depth, params) {
    if (depth === 0) return;

    const nextX = x + Math.cos(angle) * length;
    const nextY = y + Math.sin(angle) * length;

    p.stroke(50, 150, 255, params.opacity * (depth / 10));
    p.line(x, y, nextX, nextY);

    // Randomized branching based on seed
    const leftAngle = angle + p.random(0.3, 0.7);
    const rightAngle = angle - p.random(0.3, 0.7);
    const newLength = length * 0.7 * params.scale;

    drawRecursiveTree(p, nextX, nextY, newLength, leftAngle, depth - 1, params);
    drawRecursiveTree(p, nextX, nextY, newLength, rightAngle, depth - 1, params);
}

/**
 * Harmonic Resonance: Wave interference patterns
 * Use this when philosophy is about "interference" or "resonance"
 */
function drawHarmonicPattern(p, params) {
    p.background(255);
    for (let x = 0; x < p.width; x += 5) {
        for (let y = 0; y < p.height; y += 5) {
            // Multiple sine waves interfering
            const wave1 = Math.sin(x * 0.01) * Math.cos(y * 0.01);
            const wave2 = Math.sin((x - y) * 0.015);
            const interference = wave1 + wave2;

            const brightness = p.map(interference, -2, 2, 0, 255);
            p.fill(brightness);
            p.noStroke();
            p.rect(x, y, 5, 5);
        }
    }
}

/**
 * Cellular Automation: Simple rules creating complex patterns
 * Use this when philosophy emphasizes "emergence from simple rules"
 */
function updateCellularAutomata(grid, params) {
    const newGrid = grid.map(row => [...row]);
    for (let i = 1; i < grid.length - 1; i++) {
        for (let j = 1; j < grid[i].length - 1; j++) {
            const neighbors = countLiveNeighbors(grid, i, j);
            // Example rules (customize for your algorithm)
            if (grid[i][j] === 1 && (neighbors < 2 || neighbors > 3)) {
                newGrid[i][j] = 0;
            } else if (grid[i][j] === 0 && neighbors === 3) {
                newGrid[i][j] = 1;
            }
        }
    }
    return newGrid;
}

function countLiveNeighbors(grid, x, y) {
    let count = 0;
    for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
            if (i === 0 && j === 0) continue;
            count += grid[x + i][y + j] ? 1 : 0;
        }
    }
    return count;
}

// ============================================
// COLOR HARMONY UTILITIES
// ============================================
// Build thoughtful color palettes, not random RGB

function createColorPalette(params) {
    // Example: Analogous color scheme
    const baseHue = params.hueShift;
    return {
        primary: colorFromHSB(baseHue, 0.8, 0.9),
        secondary: colorFromHSB(baseHue + 30, 0.7, 0.85),
        accent: colorFromHSB(baseHue + 60, 0.9, 0.95),
        shadow: colorFromHSB(baseHue, 0.3, 0.2),
    };
}

function colorFromHSB(h, s, b) {
    // Simplified HSB to RGB conversion
    const c = b * s;
    const x = c * (1 - Math.abs((h / 60) % 2 - 1));
    const m = b - c;
    return { h, s, b, c, x, m };
}

// ============================================
// BEST PRACTICES SUMMARY
// ============================================
/*
 * 1. SEEDED RANDOMNESS: Always seed before random operations
 *    randomSeed(params.seed);
 *    noiseSeed(params.seed);
 *
 * 2. PARAMETER STRUCTURE: Define params that affect behavior
 *    Don't think "pattern types" - think "system qualities"
 *
 * 3. ALGORITHM FOLLOWS PHILOSOPHY: Implement the vision
 *    Let the philosophy guide algorithm choice
 *
 * 4. REPRODUCIBILITY: Same seed = same output, always
 *
 * 5. COMPOSITION: Even in randomness, maintain visual balance
 *
 * 6. COLOR HARMONY: Thoughtful palettes, not random values
 *
 * 7. PERFORMANCE: Optimize for smooth real-time execution
 *
 * 8. CRAFTSMANSHIP: Every parameter tuned with care
 *    Feels like hundreds of hours of refinement
 */
