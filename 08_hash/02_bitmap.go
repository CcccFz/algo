package main

import "fmt"

type BitMap struct {
	nbits uint
	bytes []byte
	last  uint
}

func NewBitMap(n uint) *BitMap {
	last := n / 8
	return &BitMap{
		nbits: n,
		bytes: make([]byte, last+1, last+1),
		last:  last,
	}
}

func (m *BitMap) Add(x uint) {
	if x > m.nbits {
		return
	}
	idx, offset := x/8, x%8
	m.bytes[idx] |= (1 << offset)
}

func (m *BitMap) Exist(x uint) bool {
	if x > m.nbits {
		return false
	}
	idx, offset := x/8, x%8
	return (m.bytes[idx] & (1 << offset)) > 0
}

type BloomFilter struct {
	*BitMap
}

func NewBloomFilter(n uint) *BloomFilter {
	return &BloomFilter{
		BitMap: NewBitMap(n),
	}
}

func (b *BloomFilter) Add(x uint) {
	idx, offset := x/8, x%8
	if idx < 0 {
		idx = 0
	}
	if idx > b.last {
		idx = b.last
	}
	idx1, idx2 := b.hash1(idx), b.hash2(idx)
	b.bytes[idx] |= (1 << offset)
	b.bytes[idx1] |= (1 << offset)
	b.bytes[idx2] |= (1 << offset)
}

func (b *BloomFilter) Exist(x uint) bool {
	idx, offset := x/8, x%8
	if idx < 0 {
		idx = 0
	}
	if idx > b.last {
		idx = b.last
	}
	idx1, idx2 := b.hash1(idx), b.hash2(idx)
	return (b.bytes[idx]&(1<<offset)) > 0 &&
		(b.bytes[idx1]&(1<<offset)) > 0 &&
		(b.bytes[idx2]&(1<<offset)) > 0
}

func (b *BloomFilter) hash1(idx uint) uint {
	if idx > b.last {
		return b.last
	} else if idx == 0 {
		return 0
	} else {
		return b.last - 1
	}
}

func (b *BloomFilter) hash2(idx uint) uint {
	if idx >= b.last {
		return b.last
	} else {
		return idx + 1
	}
}

func main() {
	fmt.Println("##### BitMap #####")

	m := NewBitMap(17)
	m.Add(1)
	m.Add(17)

	fmt.Println(m.Exist(2))  // false
	fmt.Println(m.Exist(16)) // false

	fmt.Println(m.Exist(1))  // true
	fmt.Println(m.Exist(17)) // true

	fmt.Println("##### Bloom Filter #####")

	b := NewBloomFilter(17)
	b.Add(1)
	b.Add(17)
	b.Add(100)

	fmt.Println(b.Exist(2))  // false
	fmt.Println(b.Exist(16)) // false
	fmt.Println(b.Exist(99)) // false

	fmt.Println(b.Exist(1))   // true
	fmt.Println(b.Exist(17))  // true
	fmt.Println(b.Exist(100)) // true
}
