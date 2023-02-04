import Snail from './snail.js'
import Quadrado from './quadrado.js'

// Canvas
const snailCanvas = document.getElementById('lowerCanvas')
const snailCtx = snailCanvas.getContext('2d')

const quadCanvas = document.getElementById('higherCanvas')
const quadCtx = quadCanvas.getContext('2d')


// Constantes
const cores = ['red', 'rgb(10, 100, 230)', 'rgb(145, 200, 20)', 'black']
const v = 50
const l = 500
const start = {
    x: 50,
    y: 50
}

// Coordenadas dos caracóis, por ordem
const coords = [
    [start.x, start.y],
    [start.x + l, start.y],
    [start.x + l, start.y + l],
    [start.x, start.y + l]
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
        cores[n]))
}
snails[0].alvo = snails[3]


// Quadrado que une os caracóis
const oQuadrado = new Quadrado(snails, 'rgb(255, 130, 35)')

// Condições relativamente ao quadrado que une os caracóis
let desenharQuadrado = true
let apagarQuadrado = true

let ultimoTempo
function loopSnails(tempo) {
    // Avançar o tempo
    if (ultimoTempo === undefined) {
        ultimoTempo = tempo
    }
    let dTime = (tempo - ultimoTempo) / 1000
    ultimoTempo = tempo


    // Desenhar os caracóis
    for(let i in snails) {
        snails[i].update(dTime)
        snails[i].draw(snailCtx)
    }

    // Desenhar o quadrado que une os caracóis
    if (desenharQuadrado) {
        if (apagarQuadrado) quadCtx.clearRect(0, 0, quadCanvas.width, quadCanvas.height)
        oQuadrado.draw(quadCtx)
    }

    // Parar se os caracóis estiverem muito próximos uns dos outros
    let mySnail = snails[0]
    if (mySnail.direction.x ** 2 + mySnail.direction.y ** 2 < 1) {
        desenharQuadrado = false
        return
    }

    requestAnimationFrame(loopSnails)
}

window.setTimeout(requestAnimationFrame, 400, loopSnails)
