package _2_链表

// 876 简单
func middleNode(head *Node) *Node {
	fast, slow := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	return slow
}
