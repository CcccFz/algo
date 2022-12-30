package _2_链表

type Node struct {
	Val  int
	Next *Node
}

// 206 简单 遍历
func reverseList(head *Node) *Node {
	var prev *Node
	for head != nil {
		head.Next, head, prev = prev, head.Next, head
	}
	return prev
}
