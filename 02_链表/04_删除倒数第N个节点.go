package _2_链表

// 19 中等 哨兵节点
func removeNthFromEnd(head *Node, n int) *Node {
	ret := &Node{Next: head}
	fast, slow := ret, ret

	i := 0
	for ; fast.Next != nil; fast = fast.Next {
		if i >= n {
			slow = slow.Next
		}

		i++
	}

	slow.Next = slow.Next.Next
	return ret.Next
}
