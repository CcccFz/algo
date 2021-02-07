package _3_栈

import "strconv"

// 682 简单
func calPoints(ops []string) int {
	stack := []int{}
	for i := 0; i < len(ops); i++ {
		if ops[i] == "C" {
			stack = stack[:len(stack)-1]
		} else if ops[i] == "D" {
			stack = append(stack, stack[len(stack)-1]*2)
		} else if ops[i] == "+" {
			stack = append(stack, stack[len(stack)-1]+stack[len(stack)-2])
		} else {
			v, _ := strconv.Atoi(ops[i])
			stack = append(stack, v)
		}
	}

	sum := 0
	for i := 0; i < len(stack); i++ {
		sum += stack[i]
	}

	return sum
}
