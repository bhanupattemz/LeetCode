/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    let toBe=(a)=>{
        if(val===a) return true
        else throw new Error("Not Equal")
    }
    let notToBe =(a)=>{
        if(val!==a) return true
        else throw new Error("Equal")
    }
    return {toBe,notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */