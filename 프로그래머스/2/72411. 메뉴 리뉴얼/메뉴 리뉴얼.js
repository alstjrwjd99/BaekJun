function solution(orders, course) {
    var answer = [];
    
    const getCombinations = (arr, length) => {
        const results = [];
        if (length === 1) return arr.map((v) => [v]);

        arr.forEach((current, index, array) => {
            const smallerCombos = getCombinations(array.slice(index + 1), length - 1);
            smallerCombos.forEach((combo) => {
                results.push([current, ...combo]);
            });
        });

        return results;
    };

    course.forEach((courseLength) => {
        const comboCount = new Map();
        
        orders.forEach((order) => {
            const sortedOrder = order.split('').sort();
            const combinations = getCombinations(sortedOrder, courseLength);
            combinations.forEach((combo) => {
                const comboKey = combo.join('');
                comboCount.set(comboKey, (comboCount.get(comboKey) || 0) + 1);
            });
        });

        let maxCount = 0;
        comboCount.forEach((count) => {
            if (count > maxCount) maxCount = count;
        });

        if (maxCount >= 2) {
            comboCount.forEach((count, combo) => {
                if (count === maxCount) answer.push(combo);
            });
        }
    });

    return answer.sort();
}