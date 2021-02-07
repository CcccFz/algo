package _3_栈

// 224 困难
func calculate(s string) int {
	ret, num, symbol := 0, 0, 1
	stack := []int{}

	for i := range s {
		if s[i] >= '0' && s[i] <= '9' {
			num = num*10 + int(s[i]-'0')
		} else if s[i] == ' ' {
			continue
		} else if s[i] == '+' {
			ret += num * symbol
			num, symbol = 0, 1
		} else if s[i] == '-' {
			ret += num * symbol
			num, symbol = 0, -1
		} else if s[i] == '(' {
			stack = append(stack, ret, symbol)
			ret, symbol = 0, 1
		} else if s[i] == ')' {
			ret += num * symbol
			ret = stack[len(stack)-2] + stack[len(stack)-1]*ret
			stack = stack[:len(stack)-2]
			num = 0
		}
	}

	return ret + symbol*num
}
