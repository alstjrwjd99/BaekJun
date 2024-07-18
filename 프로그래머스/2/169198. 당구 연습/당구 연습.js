function distanceBetweenTwoPoints(x1, y1, x2, y2) {
    return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
}

function getAnswer(startX, startY, endX, endY, m, n) {
    let top = Infinity, bottom = Infinity, left = Infinity, right = Infinity;
    if (!(startX === endX && startY > endY)) {
        bottom = distanceBetweenTwoPoints(startX, -startY, endX, endY);
    }
    if (!(startX > endX && startY === endY)) {
        left = distanceBetweenTwoPoints(-startX, startY, endX, endY);
    }
    if (!(startX === endX && startY < endY)) {
        top = distanceBetweenTwoPoints(startX, 2 * n - startY, endX, endY);
    }
    if (!(startX < endX && startY === endY)) {
        right = distanceBetweenTwoPoints(2 * m - startX, startY, endX, endY);
    }
    return Math.round(Math.pow(Math.min(top, bottom, left, right), 2));
}

function solution(m, n, startX, startY, balls) {
    return balls.map(([endX, endY]) => getAnswer(startX, startY, endX, endY, m, n));
}