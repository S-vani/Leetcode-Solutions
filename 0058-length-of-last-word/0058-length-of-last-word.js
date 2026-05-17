/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    last = 0
    string = s.trim(" ")

    
    for (let i = 0; i < string.length; i++){
        console.log(string[i])
        if (string[i] !== " "){
            last += 1
        }
        else{
            last = 0
        }
    }

    return last
};