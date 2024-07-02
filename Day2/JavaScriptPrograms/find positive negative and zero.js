function checkNumber(num) {
  if (num > 0) {
    console.log(num + ' is positive');
  } else if (num < 0) {
    console.log(num + ' is negative');
  } else {
    console.log(num + ' is zero');
  }
}

// Test the function
checkNumber(5); // 5 is positive
checkNumber(-3); // -3 is negative
checkNumber(0); // 0 is zero
