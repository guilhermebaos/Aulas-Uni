export default class Snail {
    constructor(x, y, v, alvo, cor) {
        // Parâmetros iguais para cada caracol
        this.side = 3

        // Variáveis da Cinemática Caracol
        this.x = x
        this.y = y
        this.v = {
            abs: v,
            x: 0,
            y: 0
        }

        this.cor = cor

        // Caracol para o qual a velocidade aponta
        this.alvo = alvo
    }

    update(time) {
        // Determinar a direção
        this.direction = {
            x: this.alvo.x - this.x,
            y: this.alvo.y - this.y
        }

        //Decompor v em v.x e v.y
        this.theta = Math.atan2(this.direction.y, this.direction.x)
        this.v.x = Math.cos(this.theta) * this.v.abs
        this.v.y = Math.sin(this.theta) * this.v.abs

        // Avançar de acordo com a velocidade
        this.x += this.v.x * time
        this.y += this.v.y * time
    }

    draw(ctx) {
        ctx.fillStyle = this.cor
        ctx.fillRect(this.x, this.y, this.side, this.side)
    }
}