package _2_链表

// 21 简单 哨兵节点
func mergeTwoLists(l1 *Node, l2 *Node) *Node {
	ret := &Node{}
	cur := ret

	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			cur.Next = l1
			l1 = l1.Next
		} else {
			cur.Next = l2
			l2 = l2.Next
		}
		cur = cur.Next
	}

	if l1 != nil {
		cur.Next = l1
	}

	if l2 != nil {
		cur.Next = l2
	}

	return ret.Next
}
