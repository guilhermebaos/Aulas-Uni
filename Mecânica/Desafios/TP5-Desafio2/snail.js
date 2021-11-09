export default class Snail {
    constructor(x, y, v, target, cor) {
        // Parâmetros iguais para cada caracol
        this.side = 3

        // Variáveis do Caracol
        this.x = x
        this.y = y
        this.v = {
            abs: v,
            x: 0,
            y: 0
        }

        this.cor = cor

        // Caracol para o qual a velocidade aponta
        this.target = target
    }

    update(time) {
        // Determinar a direção
        this.direction = {
            x: this.target.x - this.x,
            y: this.target.y - this.y
        }

        //Decompor v em v.x e v.y
        this.theta = Math.atan2(this.direction.y, this.direction.x)
        this.v.x = Math.cos(this.theta) * this.v.abs
        this.v.y = Math.sin(this.theta) * this.v.abs

        this.x += this.v.x * time
        this.y += this.v.y * time
    }

    draw(ctx) {
        ctx.fillStyle = this.cor
        ctx.fillRect(this.x, this.y, this.side, this.side)
    }
}