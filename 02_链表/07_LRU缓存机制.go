package _2_链表

// 146 中等 哈希+双向链式队列
type LRUCache struct {
	size, cap  int
	head, tail *DNode
	m          map[int]*DNode
}

func Constructor(capacity int) LRUCache {
	cache := LRUCache{
		cap:  capacity,
		head: &DNode{},
		tail: &DNode{},
		m:    make(map[int]*DNode, capacity),
	}

	cache.head.Next = cache.tail
	cache.tail.Prev = cache.head

	return cache
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.m[key]; ok {
		this.moveToTail(node)
		return node.Val
	}

	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.m[key]; ok {
		this.moveToTail(node)
		node.Val = value
		return
	}

	if this.size == this.cap {
		delete(this.m, this.head.Next.Key)
		this.deleteHead()
	} else {
		this.size++
	}

	this.m[key] = &DNode{Key: key, Val: value}
	this.insertTail(this.m[key])
}

func (this *LRUCache) deleteHead() {
	this.deleteNode(this.head.Next)
}

func (this *LRUCache) moveToTail(node *DNode) {
	this.deleteNode(node)
	this.insertTail(node)
}

func (this *LRUCache) deleteNode(node *DNode) {
	node.Next.Prev = node.Prev
	node.Prev.Next = node.Next
}

func (this *LRUCache) insertTail(node *DNode) {
	node.Next = this.tail
	node.Prev = this.tail.Prev
	this.tail.Prev.Next = node
	this.tail.Prev = node
}
