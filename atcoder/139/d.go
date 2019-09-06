package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func run() {
	n := nextInt()
	println((n) * (n - 1) / 2)
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


func nextArray() []string {
	sc.Scan()
	return strings.Split(sc.Text()," ")
}

func nextIntArray() []int {
	str := nextArray()
	buf := make([]int, len(str))
	for i,s:=range str{
		buf[i],_ = strconv.Atoi(s)
	}
	return buf
}

func main() {
	sc.Buffer(make([]byte, 0, bufferSize), bufferSize)
	sc.Split(bufio.ScanWords)
	run()
	out.Flush()
}
