unitStrings, teenStrings, tenStrings :: [String]
unitStrings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teenStrings = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
tenStrings = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

units, teens, tens :: Int -> String
units u = unitStrings!!u
teens u = teenStrings!!u
tens t = tenStrings!!(t-2)

digits2, digits3, digits6 :: Int -> (Int, Int)
digits2 n = n `divMod` 10
digits3 n = n `divMod` 100
digits6 n = n `divMod` 1000

convert2, convert3, convert6 :: Int -> String
convert2 = combine2 . digits2
convert3 = combine3 . digits3
convert6 = combine6 . digits6

link :: Int -> String
link n = if n < 100 then " and " else " "

combine2, combine3, combine6 :: (Int, Int) -> String
combine2 (t, u)
    | t == 0    = units u
    | t == 1    = teens u
    | u == 0    = tens t
    | otherwise = tens t ++ "-" ++ units u
combine3 (h, n)
    | h == 0    = convert2 n
    | n == 0    = units h ++ " hundred"
    | otherwise = units h ++ " hundred and " ++ convert2 n
combine6 (m, n)
    | m == 0    = convert3 n
    | n == 0    = convert3 m ++ " thousand"
    | otherwise = convert3 m ++ " thousand" ++ link n ++ convert3 n

convert :: Int -> String
convert n
    | n < 0     = "negative " ++ convert (-n)
    | otherwise = convert6 n

main :: IO ()
main = print $ convert 123456