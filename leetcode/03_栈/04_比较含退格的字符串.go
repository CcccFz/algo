package _3_栈

// 844 简单 栈
func backspaceCompare(S string, T string) bool {
	build := func(s string) string {
		stack := []byte{}
		for i := range s {
			if s[i] != '#' {
				stack = append(stack, s[i])
			} else if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		}
		return string(stack)
	}

	return build(S) == build(T)
}

// 双指针
func backspaceCompare(S string, T string) bool {
	for i, j, skip := len(S)-1, len(T)-1, 0; i >= 0 || j >= 0; {
		for i >= 0 && (S[i] == '#' || skip > 0) {
			if S[i] == '#' {
				skip++
			} else {
				skip--
			}
			i--
		}
		for j >= 0 && (T[j] == '#' || skip > 0) {
			if T[j] == '#' {
				skip++
			} else {
				skip--
			}
			j--
		}

		if i >= 0 && j >= 0 {
			if S[i] != T[j] {
				return false
			}
		} else if i >= 0 || j >= 0 {
			return false
		}

		i--
		j--
	}

	return true
}
