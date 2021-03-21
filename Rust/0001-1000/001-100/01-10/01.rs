use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut h:HashMap<i32, usize> = HashMap::new();
        let mut v = Vec::new();
        for i in 0..nums.len() {
            if !h.contains_key(&nums[i]) {
                h.insert(target - nums[i], i);
            }
            else {
                v.push(i as i32);
                v.push( *h.get(&nums[i]).unwrap() as i32 );
            }
        }
        v
    }
}