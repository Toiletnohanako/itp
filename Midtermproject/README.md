# LMSC-261 Midterm Project

## Hana Lin 2025SP LMSC-261-002

## Project Description

- This project is a simple interactive sound project built with **p5.js**. It allows the user to trigger different sounds by pressing specific keys on the keyboard (`a`, `b`, `c`). Each key plays a specific sound file that I uploaded into the project.

- Here is the link to [my project](https://editor.p5js.org/Toiletnohanako/sketches/5jjZO-Nj_).

### My Steps

- I copy and paste the codealong.
- I upload my three file, and add two new variables based on the original code.
- I copy the paths to my three file and paste them into the code, the code looks like this:

```javascript
let myFirstSound, mySecondSound, myThirdSound;

function preload() {
  soundFormats('wav', 'mp3');  
  myFirstSound = loadSound('EXPLOSION.mp3', soundLoaded);
  mySecondSound = loadSound('censoredbeep.wav', soundLoaded);
  myThirdSound = loadSound('Radio Tuning Static 2.mp3', soundLoaded);
}
```

- I create two new functions based on the original code, and I also added a `keyPressed()` function to listen for key input (`a`, `b`, or `c`). The new code looks like this:

```javascript
function keyPressed() {
  console.log("Key pressed:", key);
  if (key.toLowerCase() === 'a') {
    playFirstSound();
  }
  if (key.toLowerCase() === 'b') {
    playSecondSound();
  }
  if (key.toLowerCase() === 'c') {
    playThirdSound();
  }
}

function playFirstSound() {
  if (myFirstSound.isLoaded()) {
    myFirstSound.play();
    console.log("Sound played.");
  } else {
    console.log("Sound not loaded yet.");
  }
}

function playSecondSound() {
  if (mySecondSound.isLoaded()) {
    mySecondSound.play();
    console.log("Sound played.");
  } else {
    console.log("Sound not loaded yet.");
  }
}

function playThirdSound() {
  if (myThirdSound.isLoaded()) {
    myThirdSound.play();
    console.log("Sound played.");
  } else {
    console.log("Sound not loaded yet.");
  }
}
```

- I test my final code on p5js.org and it works.
