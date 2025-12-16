/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let res = n - 1
    return function() {
        res = res + 1
        return res
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */