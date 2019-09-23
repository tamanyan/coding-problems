package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"math"
	"strconv"
	_ "strings"
	_ "container/heap"
)

func run() {
	var m = 0
	n := nextInt()
	a := make([]int, n)
	box := make([]int, n)

	for i := 0; i < n; i++ {
		a[i] = nextInt()
	}

	// var n = 2 * pow(10, 5)
	// box := make([]int, n)
	// a := make([]int, n)
	// for i := 0; i < n; i++ {
	// 	a[i] = i % 2
	// }

	for i := n - 1; i >= 0; i-- {
		// println(i+1)
		// var value = 0
		var ai = a[i]
		// println(i + 1, ai)
		var sum = 0

		for j := i; j < n; j += (i + 1)  {
			sum += box[j]
		}

		if sum % 2 != ai {
			box[i]++
			m++
		}

		// if ai == 1 {
		// 	box[i] = 1
		// }

		// for j := i; j < n; j += (i + 1) {
		// 	a[]
		// }
		// a[]
	}

	println(m)
	for i := 0; i < n; i++ {
		if box[i] > 0 {
			println(string(i) + " ")
		}
	}
	println("")
}

// --- template ---
// Thanks https://gist.github.com/halllllll/853ab587fd82ee3ffe6f7fb7fb499695

var sc = bufio.NewScanner(os.Stdin)
var out = bufio.NewWriter(os.Stdout)

const bufferSize = 64 * 1024 * 1024

func print(a ...interface{}) (n int, err error) {
	return fmt.Fprint(out, a...)
}

func printf(format string, a ...interface{}) (n int, err error) {
	return fmt.Fprintf(out, format, a...)
}

func println(a ...interface{}) (n int, err error) {
	return fmt.Fprintln(out, a...)
}

func next() string {
	sc.Scan()
	return sc.Text()
}

func nextInt() int {
	a, err := strconv.Atoi(next())
	if err != nil {
		log.Fatal(err)
	}
	return a
}

func nextFloat() float64 {
	a, err := strconv.ParseFloat(next(), 64)
	if err != nil {
		log.Fatal(err)
	}
	return a
}

func min(nums []int) int {
    if len(nums) == 0 {
        panic("funciton min() requires at least one argument.")
    }
    res := nums[0]
    for i := 0; i < len(nums); i++ {
        res = int(math.Min(float64(res), float64(nums[i])))
    }
    return res
}

func max(nums []int) int {
    if len(nums) == 0 {
        panic("funciton max() requires at least one argument.")
    }
    res := nums[0]
    for i := 0; i < len(nums); i++ {
        res = int(math.Max(float64(res), float64(nums[i])))
    }
    return res
}

func abs(a int) int {
    return int(math.Abs(float64(a)))
}

func pow(p, q int) int {
    return int(math.Pow(float64(p), float64(q)))
}

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// Push to heap
func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

// Pop from heap
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {
	sc.Buffer(make([]byte, 0, bufferSize), bufferSize)
	sc.Split(bufio.ScanWords)
	run()
	out.Flush()
}
