---
dg-publish: true
---

If you want to make an executable, you need a main function. To do this, have;

```haskell
main = do {- whatever -}
```

Also, to print stuff out, do

```haskell
putStrLn "String"
print whatever
```

For comments, do

```haskell
{- these comments are self contained -}

{-
but they can go on for many lines as well
-}

main = do it -- or you can just do this for single line comments
```

To access an element in a list, do `list!!idx` where lists are zero indexed, and for logical operators they're the similar to Java, with `&&, ||, ==, /=` meaning the obvious things. For exponentiation, they do `^`. To convert functions to be infixed, you can use back quotes like below:

```haskell
a `divMod` b == divMod a b
```

For switch statements you have (these are checked in order):

```haskell
parity n = 
 | n == 1    = 1
 | n == 2    = 0
 | n == 3    = 1
 ...
 | otherwise = ???

example :: Int -> String
example n = if n < 100 then " condition met " else " condition not met "
```

For concatenation of strings, you can do the following:

```haskell
concat ['a', 'b', ..] == 'a' ++ 'b' ++ ..
```

For local setting of variables, see [[2.5 local definitions let expressions and where clauses]].
