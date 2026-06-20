/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    len = digits.length
    const newList = []
    if (digits[len-1] !== 9){
        for (let i = 0; i< len-1; i++){
            newList.push(digits[i])
        }
        newList.push(digits[len-1]+1)
        return newList
    }
    else{
        if (len === 1){
            return [1, 0]
        }
        else{
            newList.push(...plusOne(digits.slice(0, len-1)))
            newList.push(0)
            return newList
        }
    }
};