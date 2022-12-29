package _3_栈

// 232 简单
type MyQueue struct {
	inStack  []int
	outStack []int
}

func Constructor() MyQueue {
	return MyQueue{}
}

func (this *MyQueue) Push(x int) {
	this.inStack = append(this.inStack, x)
}

func (this *MyQueue) Pop() int {
	this.Peek()

	last := len(this.outStack) - 1
	v := this.outStack[last]
	this.outStack = this.outStack[:last]
	return v
}

func (this *MyQueue) Peek() int {
	if len(this.outStack) == 0 {
		for len(this.inStack) > 0 {
			last := len(this.inStack) - 1
			this.outStack = append(this.outStack, this.inStack[last])
			this.inStack = this.inStack[:last]
		}
	}

	return this.outStack[len(this.outStack)-1]
}

func (this *MyQueue) Empty() bool {
	if len(this.inStack) == 0 && len(this.outStack) == 0 {
		return true
	}
	return false
}
