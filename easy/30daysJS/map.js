/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    result=[]
    for(let i=0;i<arr.length;i+=1){
        result.push(fn(arr[i],i))
    }
    return result
};