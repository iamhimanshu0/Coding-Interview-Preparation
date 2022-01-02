var maxArea = function (height) {
  var left = 0;
  var right = height.length - 1;
  var res = 0;
  var ans = 0;

  while (left < right) {
    ans = (right - left) * Math.min(height[left], height[right]);
    res = Math.max(res, ans);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }
  return res;
};

height = [1, 8, 6, 2, 5, 4, 8, 3, 7];
console.log(maxArea(height));
