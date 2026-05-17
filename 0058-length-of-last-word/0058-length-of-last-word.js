/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    last = 0
    
    for (let i = 0; i < s.length; i++){
        if (s[i] !== " "){
            last += 1
        }
        else{
            if (s.slice(i, s.length) === " ".repeat(s.length - i)){
                return last
            }
            last = 0
        }
    }

    return last
};