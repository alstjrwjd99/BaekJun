function solution(numbers) {
    const ch_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    const change = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    };
    
    for (ch of ch_list){
        numbers = numbers.replaceAll(ch,change[ch])
    }
    return +numbers;
}