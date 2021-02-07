package _1_数组

import "strings"

// 125

func isPalindrome(s string) bool {
	isAlnum := func(c byte) bool {
		return c >= 'a' && c <= 'z' || c >= '0' && c <= '9'
	}

	s = strings.ToLower(s)
	i, j := 0, len(s)-1
	for i < j {
		if !isAlnum(s[i]) {
			i++
			continue
		} else if !isAlnum(s[j]) {
			j--
			continue
		} else if s[i] != s[j] {
			return false
		} else {
			i++
			j--
		}
	}
	return true
}
