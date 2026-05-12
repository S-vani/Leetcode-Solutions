function isValid(s: string): boolean {    
    // base case
    if(s.length <2) return false;

    const arr = [];

    for(let i = 0; i< s.length; i++){
        if (s[i] === "(" || s[i] === "[" || s[i] === "{"){
            arr.push(s[i])
        }
        else if (s[i] === ")" && arr[arr.length-1] !== "("){
            return false
        }
        else if (s[i] === "]" && arr[arr.length-1] !== "["){
            return false
        }
        else if (s[i] === "}" && arr[arr.length-1] !== "{"){
            return false
        }
        else{
            arr.pop()
        }
    };
    console.log(s)
    return arr.length === 0
};