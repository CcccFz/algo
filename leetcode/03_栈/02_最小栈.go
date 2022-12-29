package _3_栈

// 155 简单
type MinStack struct {
	stack []item
}

type item struct {
	val, mVal int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{stack: []item{}}
}

func (this *MinStack) Push(x int) {
	item := item{val: x, mVal: x}

	last := len(this.stack) - 1
	if last > -1 && this.stack[last].mVal < x {
		item.mVal = this.stack[last].mVal
	}

	this.stack = append(this.stack, item)
}

func (this *MinStack) Pop() {
	this.stack = this.stack[:len(this.stack)-1]
}

func (this *MinStack) Top() int {
	return this.stack[len(this.stack)-1].val
}

func (this *MinStack) GetMin() int {
	return this.stack[len(this.stack)-1].mVal
}
