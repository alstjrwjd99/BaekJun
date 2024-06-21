function solution(my_string, m, c) {
  return my_string
    .split("")
    .slice(0, Math.ceil(my_string.length / m))
    .map((_, idx) => my_string.charAt(idx * m + c - 1))
    .join("");
}