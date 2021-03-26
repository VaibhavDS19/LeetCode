impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let mut diff = 0;
        let mut a1 = [0; 26];
        for (i, j) in s1.as_bytes().iter().zip(s2.as_bytes().iter()) {
            a1[(*i as u8 - 97) as usize] += 1;
            a1[(*j as u8 - 97) as usize] -= 1;
            if *i != *j {
                diff += 1;
            }
        }
        for i in a1.iter() {
            if *i != 0 {
                return false;
            }
        }
        return diff == 0 || diff == 2;
    }
}
