package _3_栈

// 20 简单
func isValid(s string) bool {
	if len(s)%2 == 1 {
		return false
	}

	stack := []byte{}
	for i := range s {
		switch s[i] {
		case '(':
			stack = append(stack, ')')
		case '[':
			stack = append(stack, ']')
		case '{':
			stack = append(stack, '}')
		default:
			last := len(stack) - 1
			if len(stack) == 0 || stack[last] != s[i] {
				return false
			}
			stack = stack[:last]
		}
	}

	return len(stack) == 0
}
