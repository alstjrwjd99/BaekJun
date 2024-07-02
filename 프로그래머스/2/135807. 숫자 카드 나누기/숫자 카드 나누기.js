// 유클리드 호제법 재귀호출
const uclid = (a, b) => {
  if (b === 0) {
    return a;
  }
  return uclid(b, a % b);
};

const getGCD = (arr) => {
  let 최대공약수;
  for (let i = 0; i < arr.length - 1; i++) {
    const curr = 최대공약수 ?? arr[i];
    const next = arr[i + 1];
    const uclidResult = curr > next ? uclid(curr, next) : uclid(next, curr);
    if (uclidResult > 1) {
      최대공약수 = uclidResult;
    } else {
      최대공약수 = 1;
      break;
    }
  }
  return 최대공약수;
};

function solution(arrayA, arrayB) {
  let result = 0;

  const gcdA = arrayA.length > 1 ? getGCD(arrayA) : arrayA[0];
  if (gcdA >= 1 && arrayB.every((num) => num % gcdA !== 0) && gcdA >= result) {
    result = gcdA;
  }

  const gcdB = arrayB.length > 1 ? getGCD(arrayB) : arrayB[0];
  if (gcdB >= 1 && arrayA.every((num) => num % gcdB !== 0) && gcdB >= result) {
    result = gcdB;
  }

  return result;
}
