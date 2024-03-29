package _2_链表

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head := &ListNode{}
	cur := head
	carry := 0

	for l1 != nil || l2 != nil || carry > 0 {
		cur.Next = &ListNode{}
		cur = cur.Next

		if l1 != nil {
			carry += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			carry += l2.Val
			l2 = l2.Next
		}
		cur.Val = carry % 10
		carry /= 10
	}

	return head.Next
}
