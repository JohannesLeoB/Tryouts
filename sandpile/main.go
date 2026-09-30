// Abelian sandpile: identity element of the sandpile group on an n×n grid.
//
// Model (Bak, Tang, Wiesenfeld 1987; Dhar 1990): each cell holds 0..3 grains.
// A cell with ≥4 grains topples: it loses 4, each of its 4 neighbours gains 1.
// Grains that fall off the edge are lost (sink). Stabilization is confluent,
// so the final stable configuration is independent of toppling order.
//
// The recurrent configurations form an abelian group. Its identity is
//
//	e = ( 2m − (2m)° )°
//
// where m is the all-3 configuration and ° denotes stabilization
// (Levine & Propp, "What is a sandpile?", Notices AMS 57(8), 2010).
package main

import (
	"flag"
	"fmt"
	"image"
	"image/color"
	"image/png"
	"os"
	"time"
)

type grid struct {
	n int
	c []int32
}

func newGrid(n int) *grid { return &grid{n: n, c: make([]int32, n*n)} }

func (g *grid) fill(v int32) {
	for i := range g.c {
		g.c[i] = v
	}
}

func (g *grid) clone() *grid {
	h := newGrid(g.n)
	copy(h.c, g.c)
	return h
}

// stabilize topples until every cell holds < 4 grains. Returns topple count.
func (g *grid) stabilize() uint64 {
	n := g.n
	var topples uint64
	queue := make([]int32, 0, n*n)
	inq := make([]bool, n*n)
	for i, v := range g.c {
		if v >= 4 {
			queue = append(queue, int32(i))
			inq[i] = true
		}
	}
	push := func(j int32) {
		if g.c[j] >= 4 && !inq[j] {
			inq[j] = true
			queue = append(queue, j)
		}
	}
	for len(queue) > 0 {
		i := queue[len(queue)-1]
		queue = queue[:len(queue)-1]
		inq[i] = false
		v := g.c[i]
		if v < 4 {
			continue
		}
		k := v / 4 // topple k times at once (still confluent)
		g.c[i] = v - 4*k
		topples += uint64(k)
		x, y := int(i)%n, int(i)/n
		if x > 0 {
			g.c[i-1] += k
			push(i - 1)
		}
		if x < n-1 {
			g.c[i+1] += k
			push(i + 1)
		}
		if y > 0 {
			g.c[i-int32(n)] += k
			push(i - int32(n))
		}
		if y < n-1 {
			g.c[i+int32(n)] += k
			push(i + int32(n))
		}
		if g.c[i] >= 4 {
			push(i)
		}
	}
	return topples
}

func (g *grid) add(h *grid) {
	for i := range g.c {
		g.c[i] += h.c[i]
	}
}

func (g *grid) equal(h *grid) bool {
	for i := range g.c {
		if g.c[i] != h.c[i] {
			return false
		}
	}
	return true
}

func (g *grid) histogram() [4]int {
	var h [4]int
	for _, v := range g.c {
		h[v]++
	}
	return h
}

func (g *grid) savePNG(path string, scale int) error {
	palette := []color.RGBA{
		{0x1b, 0x1f, 0x3b, 255}, // 0 grains
		{0x3a, 0x7d, 0xbf, 255}, // 1
		{0xf2, 0xc1, 0x4e, 255}, // 2
		{0xf7, 0xf4, 0xea, 255}, // 3
	}
	img := image.NewRGBA(image.Rect(0, 0, g.n*scale, g.n*scale))
	for y := 0; y < g.n; y++ {
		for x := 0; x < g.n; x++ {
			col := palette[g.c[y*g.n+x]]
			for dy := 0; dy < scale; dy++ {
				for dx := 0; dx < scale; dx++ {
					img.SetRGBA(x*scale+dx, y*scale+dy, col)
				}
			}
		}
	}
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()
	return png.Encode(f, img)
}

func main() {
	n := flag.Int("n", 400, "grid side length")
	out := flag.String("out", "identity.png", "output PNG")
	scale := flag.Int("scale", 2, "pixels per cell")
	flag.Parse()

	start := time.Now()

	// m = all-3 configuration (maximal stable).
	m := newGrid(*n)
	m.fill(3)

	// (2m)°
	twoM := newGrid(*n)
	twoM.fill(6)
	t1 := twoM.stabilize()

	// 2m − (2m)°, then stabilize → identity e
	e := newGrid(*n)
	for i := range e.c {
		e.c[i] = 6 - twoM.c[i]
	}
	t2 := e.stabilize()
	elapsed := time.Since(start)

	fmt.Printf("n=%d  topples: (2m)°=%d  e=%d  time=%s\n", *n, t1, t2, elapsed.Round(time.Millisecond))
	h := e.histogram()
	fmt.Printf("grain histogram of e: 0:%d 1:%d 2:%d 3:%d\n", h[0], h[1], h[2], h[3])

	// Verification 1: e is idempotent, (e+e)° == e.
	ee := e.clone()
	ee.add(e)
	ee.stabilize()
	fmt.Printf("check (e+e)° == e : %v\n", ee.equal(e))

	// Verification 2: e acts as identity on the recurrent config m: (m+e)° == m.
	me := m.clone()
	me.add(e)
	me.stabilize()
	fmt.Printf("check (m+e)° == m : %v\n", me.equal(m))

	// Verification 3 (negative control): m itself is NOT the identity, (m+m)° != m.
	mm := m.clone()
	mm.add(m)
	mm.stabilize()
	fmt.Printf("check (m+m)° != m : %v\n", !mm.equal(m))

	// Measure the central all-2 square: grow outward from the centre while all 2s.
	side := 0
	for r := 0; ; r++ {
		lo, hi := *n/2-r-1, *n/2+r
		if lo < 0 || hi >= *n {
			break
		}
		ok := true
		for y := lo; y <= hi && ok; y++ {
			for x := lo; x <= hi; x++ {
				if e.c[y**n+x] != 2 {
					ok = false
					break
				}
			}
		}
		if !ok {
			break
		}
		side = hi - lo + 1
	}
	fmt.Printf("central all-2 square: side=%d  ratio side/n=%.4f\n", side, float64(side)/float64(*n))

	if err := e.savePNG(*out, *scale); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	fmt.Printf("wrote %s (%dx%d px)\n", *out, *n**scale, *n**scale)
}
