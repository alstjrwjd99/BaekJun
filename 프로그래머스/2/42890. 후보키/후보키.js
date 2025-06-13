/*
완전탐색
후보키 - 유일성 + 최소성을 만족 시켜야함

1. 컬럼 8개 -> 2 ^ 8 -> 완전 탐색으로 subset구하기
2. 전체 length vs Set()의 length 비교해서 고유한지 판별
*/

function solution(relation) {
    const combi = [];
    const n = relation[0].length;

    function getSubSet(start, path) {
        if (path.length > 0) combi.push([...path]);
        for (let i = start; i < n; i++) {
            path.push(i);
            getSubSet(i + 1, path);
            path.pop();
        }
    }

    getSubSet(0, []);

    const candidateKeys = [];

    combi.sort((a, b) => a.length - b.length);

    for (const cols of combi) {
        const tuples = relation.map(row =>
            cols.map(i => row[i]).join(',')
        );
        const set = new Set(tuples);

        if (set.size !== relation.length) continue;
        if (candidateKeys.some(ck => ck.every(c => cols.includes(c)))) continue;

        candidateKeys.push(cols);
    }

    return candidateKeys.length;
}