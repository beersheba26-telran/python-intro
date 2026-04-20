const N = 100_000_000
console.time(`running time of cretaing array with ${N} random numbers`)
const big_array = Array.from({length:N}, () => Math.random())
console.timeEnd(`running time of cretaing array with ${N} random numbers`)
