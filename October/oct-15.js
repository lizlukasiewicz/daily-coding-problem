// This problem was asked by Apple.

// Implement a job scheduler which takes in a function f and an integer n, 
//and calls f after n milliseconds.

function jobScheduler(f, n) {
    setTimeout(f, n)
}
const f = () => {
    console.log("run function! run!")
}
const n = 5000
jobScheduler(f, n)