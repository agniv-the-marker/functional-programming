---
dg-publish: true
location: "[[fp_notes.pdf#page=9&selection=59,0,59,9|fp_notes, page 9]]"
---
chapter: [[1 function and lists]]

*Problem 1.*

```haskell
a plus f x + x times y * x 
=
(a(plus(f(x)))) + (x(times(y)) * x) -- That's not confusing... at all.

3 4 + 5 + 6 -- Doesn't evaluate because 3(4) is not well defined.
=
(3(4) + (5)) + (6)

2^2^2^2
=
2^(2^(2^2))

```

*Problem 2.*

Let $f, g, h$ be functions such that $h: A \to B, g: B \to C, f: C\to D$ for some sets $A, B, C, D.$ Define $F_1 = f \circ (g \circ h), F_2 = (f \circ g) \circ h.$

The domain of $f \circ (g \circ h)$ is the domain of $g \circ h$, which in turn is the domain of $h$, which is equal to $A$. Similarly, the domain of $(f \circ g) \circ h$  is equal to the domain of $h$, which is $A$. So $F_1$ and $F_2$ share domains.

The codomain of $F_1$ is equal to the codomain of $f$, which is $D$. Similarly, the codomain of $F_2$ is equal to the codomain of $f \circ g$, which is equal to the codomain of $f$, which is equal to $D$. So $F_1$ and $F_2$ share codomains.

Then, let us consider an element $x \in A$ and where $F_1$ and $F_2$ send it.

$$\begin{align}F_1(x) &= ((f \circ g) \circ h)(x)\\ &= (f\circ g)(h(x))\\ &= f(g(h(x)))\\ &= f(g \circ h(x)) \\&= (f \circ (g \circ h))(x) \\&= F_2(x).\end{align}$$
As such, $F_1 = F_2$ and composition is associative.

*Problem 3.*

Define $+\mkern-10mu+$ as the concat operator. This is associative, which follows from an inductive proof. Consider $as, bs$ to be lists, and induct on the length of $cs$. It is not commutative since $[1, 2] \neq [2, 1]$, and its identity element is equal to the empty list $[]$ . This does not have a zero element. In this way concatenation over a consistent type forms a free monoid.

*Problem 4.*

```haskell
map double [3, 7, 4, 2] = [6, 14, 8, 4]
map (double.double) [3, 7, 4, 2] = [12, 28, 16, 8]
map double [] = [].

sum . map double = double . sum -- True, as the integers are a commutative ring
sum . map sum = sum . concat -- True, assuming type [[Integer]]
sum . sort = sum -- True as addition is commutative in the integers
```
