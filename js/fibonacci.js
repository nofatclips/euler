// Recursive Fibonacci using memoization and closures
var fibonacci = function () {
    var cache = {0: 0, 1: 1, 2: 1};
    var closeFibo = function (n) {
        if (n<0) return undefined;
        if (!(n in cache)) {
            cache[n] = closeFibo(n-1) + closeFibo(n-2);
        }
        return cache[n];        
    };
    return closeFibo;
}();

console.log(fibonacci(40));