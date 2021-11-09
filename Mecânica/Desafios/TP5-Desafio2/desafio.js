import Snail from './snail.js'

// Canvas
const canvas = document.getElementById('mainCanvas')
const ctx = canvas.getContext('2d')

// Constantes
const colors = ['red', 'blue', 'green', 'black']
const v = 50
const l = 500
const start = {
    x: 50,
    y: 50
}

// Coordenadas dos caracóis, por ordem
const coords = [
    [50, 50],
    [50 + l, 50],
    [50 + l, 50 + l],
    [50, 50 + l]
]

// Criar os nossos caracóis
let snails = []
for(let n = 0; n < 4; n++) {
    let target = n > 0 ? snails[n - 1] : undefined

    snails.push(new Snail(
        coords[n][0],
        coords[n][1],
        v,
        target,
        colors[n]))
}
snails[0].target = snails[3]


let lastTime
function loopSnails(time) {
    if (lastTime === undefined) {
        lastTime = time
    }

    let dTime = (time - lastTime) / 1000
    lastTime = time

    for(let i in snails) {
        snails[i].update(dTime)
        snails[i].draw(ctx)
    }
    let mySnail = snails[0]
    if (mySnail.direction.x ** 2 + mySnail.direction.y ** 2 < 1) {
        return
    }

    requestAnimationFrame(loopSnails)
}

loopSnails(0)
