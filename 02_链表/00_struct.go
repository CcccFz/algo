package _2_链表

type Node struct {
	Val  int
	Next *Node
}
type ListNode = Node

type DNode struct {
	Key, Val   int
	Prev, Next *DNode
}
