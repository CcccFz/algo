package _0_未分类

// 09 简单
func isPalindrome(x int) bool {
	if x < 0 || (x%10 == 0 && x != 0) {
		return false
	}

	reverseNum := 0
	for reverseNum < x {
		reverseNum = reverseNum*10 + x%10
		x /= 10
	}

	if reverseNum == x || reverseNum/10 == x {
		return true
	}

	return false
}
