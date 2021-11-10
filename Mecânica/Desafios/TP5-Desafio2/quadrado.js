export default class Quadrado {
    constructor(snailArr, cor) {
        this.snailArr = snailArr
        this.cor = cor
    }

    draw(ctx) {
        ctx.strokeStyle = this.cor

        // Fazer uma linha que passa em todos os caracóis
        ctx.beginPath()
        ctx.moveTo(
            this.snailArr[this.snailArr.length - 1].x,
            this.snailArr[this.snailArr.length - 1].y
        )
        for(let i in this.snailArr) {
            ctx.lineTo(
                this.snailArr[i].x,
                this.snailArr[i].y
            )
        }
        ctx.stroke()
    }
}