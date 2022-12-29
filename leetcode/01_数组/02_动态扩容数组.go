package _1_数组

func add(nums *[]int, i, x int) {
	size := cap(*nums)
	if i >= size {
		newNums := make([]int, 0, size*2)
		for j := 0; j < i; j++ {
			newNums[j] = (*nums)[j]
		}
		nums = &newNums
	}

	(*nums)[i] = x
	i++
}
