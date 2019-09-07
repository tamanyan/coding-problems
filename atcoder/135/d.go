package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
	// "math"
	"fmt"
	"math/rand"
	"time"
)

var (
	sc = bufio.NewScanner(os.Stdin)
)

const mod = 1e9 + 7

func main() {
	var s = nextLine()
	var L = len(s)

	dp := make([][]int, L+1)
	for i := 0; i < L+1; i++ {
		dp[i] = make([]int, 13)
	}

	dp[0][0] = 1

	for k := 0; k < L; k++ {
		for m := 0; m < 13; m++ {
			if s[k] == '?' {
				for i := 0; i < 10; i++ {
					dp[k+1][(m * 10 + i) % 13] += dp[k][m]
					dp[k+1][(m * 10 + i) % 13] %= mod
				}
			} else {
				var si = int(s[k] - '0')
				dp[k+1][(m * 10 + si) % 13] += dp[k][m]
				dp[k+1][(m * 10 + si) % 13] %= mod
			}
		}
	}

	fmt.Println(dp[L][5])
}

// Input helpers
func init()  {
	rand.Seed(time.Now().UnixNano())
	buf := make([]byte, 0) //ここのサイズは何でもよさそう
	sc.Buffer(buf, 1000000009)
}

func nextInt() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return i
}

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

func spaceLine() []string {
	sc.Scan()
	return strings.Split(sc.Text()," ")
}

func intLine() []int {
	str := spaceLine()
	buf := make([]int,len(str))
	for i,s:=range str{
		buf[i],_ = strconv.Atoi(s)
	}
	return buf
}
