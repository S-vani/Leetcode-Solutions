/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
    return function(x) {
        let i = x
        for (n = functions.length - 1; n>-1; n--){
            i = functions[n](i)
        }
        return i
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */