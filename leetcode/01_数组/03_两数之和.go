package _1_数组

// 1 简单 hash
func twoSum(nums []int, target int) []int {
	idxMap := map[int]int{}
	for i := 0; i < len(nums); i++ {
		if v, ok := idxMap[target-nums[i]]; ok {
			return []int{v, i}
		}
		idxMap[nums[i]] = i
	}
	return []int{}
}
