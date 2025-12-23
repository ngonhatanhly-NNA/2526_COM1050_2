function countTriangles(nums) {
    let res = 0;
    nums.sort((a, b) => a - b);

    for (i = 2; i < nums.length; ++i){
        let left = 0; right = i - 1;
        
        while (left < right){
            if (nums[left] + nums[right] > nums[i]){
                res += right - left;
                right--;
            }
            else{
                left++;
            }
        }
    }
    return res;
    
}
const arr = [4, 6, 3, 7];
console.log(countTriangles(arr));