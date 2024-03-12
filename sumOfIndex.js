const arr = [1, 2, 4, 5, 0, 6, 3, 8, 1];

function findSum(arr, target) {
  let n;
  for (let i = 0; i < arr.length; i++) {
    n = i + 1;
    let sumof = arr[i] + arr[n];
    if (sumof == target) {
      return [arr.indexOf(arr[i]), arr.indexOf(arr[n])];
    }
  }
}
console.log(findSum(arr, 9));