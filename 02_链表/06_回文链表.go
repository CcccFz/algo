package _2_链表

// 234 简单
func isPalindrome(head *Node) bool {
	fast, slow := head, head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	var prev *Node
	for slow != nil {
		slow.Next, slow, prev = prev, slow.Next, slow
	}

	for head != nil && prev != nil {
		if head.Val != prev.Val {
			return false
		}
		head = head.Next
		prev = prev.Next
	}

	return true
}
