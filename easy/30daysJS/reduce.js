/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function (nums, fn, init) {
    for (let n of nums) {
        init = fn(init, n)
    }
    return init

};