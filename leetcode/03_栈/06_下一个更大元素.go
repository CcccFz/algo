package _3_栈

// 496 简单
func nextGreaterElement(nums1 []int, nums2 []int) []int {
	m := make(map[int]int)
	stack := []int{}

	for i := range nums2 {
		for len(stack) > 0 && nums2[i] > stack[len(stack)-1] {
			m[stack[len(stack)-1]] = nums2[i]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, nums2[i])
	}

	for i := range nums1 {
		if v, ok := m[nums1[i]]; ok {
			nums1[i] = v
		} else {
			nums1[i] = -1
		}
	}

	return nums1
}
