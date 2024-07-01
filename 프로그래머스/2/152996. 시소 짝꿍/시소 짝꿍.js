function solution(weights) {
    let answer = 0;
    const seesaw = {};

    for (let w of weights) {

        const pos1 = w;
        const pos2 = w * 2;
        const pos3 = w / 2;
        const pos4 = (w * 2) / 3;
        const pos5 = (w * 3) / 2;
        const pos6 = (w * 4) / 3;
        const pos7 = (w * 3) / 4;
        
        if (seesaw[pos1] !== undefined) answer += seesaw[pos1];
        if (seesaw[pos2] !== undefined) answer += seesaw[pos2];
        if (seesaw[pos3] !== undefined) answer += seesaw[pos3];
        if (seesaw[pos4] !== undefined) answer += seesaw[pos4];
        if (seesaw[pos5] !== undefined) answer += seesaw[pos5];
        if (seesaw[pos6] !== undefined) answer += seesaw[pos6];
        if (seesaw[pos7] !== undefined) answer += seesaw[pos7];

        if (seesaw[w] === undefined) {
            seesaw[w] = 1;
        } else {
            seesaw[w]++;
        }
    }

    return answer;
}