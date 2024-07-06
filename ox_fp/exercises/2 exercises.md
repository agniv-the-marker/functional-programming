---
dg-publish: true
location: "[[fp_notes.pdf#page=16&selection=174,0,174,9|fp_notes, page 16]]"
---
chapter: [[2 definitions]]

*Problem 1.*

```haskell
factorial :: Integer -> Integer
factorial n = product [1..n]

choose :: Integer -> Integer -> Integer
choose n r = factorial n `div` (factorial r * factorial(n-r))
choose n r
    | r > n || r < 0 = 0
    | r == 0         = 1
	| otherwise      = factorial n `div` (factorial r * factorial (n-r))

check :: Integer -> Bool
check n = sum [choose n r | r <- [0..n]] == 2^n
```

*Problem 2.*

```haskell
not1, not2, not3, not4 :: Bool -> Bool
not1 True = False
not1 False = True

not2 bool = if bool then False else True

not3 bool = case bool of
            True  -> False
            False -> True

not4 bool
    | bool == True = False
    | otherwise    = True
```

*Problem 3.*

Since a function is a relation and parenthesis are ignored, its 2^^{# of Bools} (tetration). 

1. 4
	- T and F both have 2 options, so its 4.
2. 16
	- This is equal to Bool -> (Bool, Bool), so there's 4 options each for T, F, so its 16.
3. 256
	- Same as before, except with Bool -> (Bool -> Bool -> Bool), which is mapping 2 things to 16 options, so its 256.
4. 4
5. 16
	- 4 things can map to 2 things, so its $2^4$, which is 16.
6. 8
	- This is $2^3$, so its 8.
7. 256
	- 8 things map to 2 things, so its $2^8,$ which is 256.
8. 16
	- 4 things mapping to two things, so its 16.
9. 65536
	- 16 things mapping to 2, so its $2^{16},$ which is 65536. 
10. 65536
	-  (Bool -> Bool) is 4 mapping to 2, so there's 16.
	- Then we're mapping 16 things to 2 things, so its $2^{16}.$

*Problem 4.*

Not 100% secure on this answer tbh.

```haskell
intToBin :: Int -> String
intToBin 0 = "0"
intToBin n = reverse (helper n)
  where
    helper 0 = "0"
    helper n = let (q, r) = n `divMod` 2 in (if r == 0 then '0' else '1') : helper q

f :: Int -> (Bool -> Bool)
f n = let binary = drop 2 $ intToBin n
      in \b -> if b then head binary == '1' else binary !! 1 == '1'

g :: Int -> ((Bool -> Bool) -> Bool)
g n output = let binary = drop 2 $ intToBin n
                 outputFunc func
                   | func == f 0 = head binary == '1'
                   | func == f 1 = binary !! 1 == '1'
                   | func == f 2 = binary !! 2 == '1'
                   | otherwise = binary !! 3 == '1'
             in output outputFunc
```

*Problem 5.*

Assume $\lfloor x \rfloor < n$ for $n \in \mathbb{Z}.$ Assume towards a contradiction that $x \geq n.$ By definition of floor, as $n \leq x$, we have $\lfloor x \rfloor \geq n,$ which is a contradiction to the assumption. Therefore $x < n.$

Assume that $x < n$ for $n \in \mathbb{Z}.$ Then we must have $\lfloor x \rfloor \leq x < n$. As $\lfloor x \rfloor + 1$ is an integer greater than $x$, we have $$\lfloor x \rfloor \leq x < \lfloor x \rfloor + 1.$$
*Problem 6.*

The floor function is using the greatest lower bound property of the reals, and when flipping it via $-$, we now have the lowest upper bound property. Therefore we have $\lceil x \rceil = \max \{n \mid n \in \mathbb{Z}, n > x \}.$ Similarly, $\lceil x \rceil - 1 < x \leq \lceil x \rceil .$

*Problem 7.*

Let $l + 1 < r$, $l, r \in \mathbb{N}.$ We then have $(l + r) div\ 2 < (2r) div\ 2 < r.$ For the other direction, we have $l = (2l)div\ 2 < (l + r)div \ 2.$ 