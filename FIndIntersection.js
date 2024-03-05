function BracketCombinations(num) {
  if (num < 0) {
    return 0; // Invalid input
  }

  // Create an array to store the number of combinations for each subproblem
  const dp = new Array(num + 1).fill(0);
  console.log(dp);
  // Base case: there is one way to have zero pairs of parentheses (empty string)
  dp[0] = 1;

  // Calculate the number of combinations for each number of pairs of parentheses
  for (let i = 1; i <= num; i++) {
    for (let j = 0; j < i; j++) {
      let output = (dp[i] += dp[j] * dp[i - 1 - j]);
      console.log(output);
      //   console.log((dp[i] += dp[j]));
      //   console.log(dp[i - 1 - j]);
      //   console.log("its dp i", dp[i]);
      //   console.log("its dp j", dp[j]);
    }
  }

  return dp[num];
}

// Example usage:
const result = BracketCombinations(3);
console.log("Total number of Combination's : ", result);
