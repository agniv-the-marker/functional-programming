toBinary :: Int -> [Int]
toBinary 0 = [0]
toBinary n = reverse (helper n)

helper :: Int -> [Int]
helper 0 = []
helper n = (n `mod` 2) : helper (n `div` 2)

simpleFunction :: Integer -> Bool -> Bool
simpleFunction n x = case n `mod` 4 of
    0    -> False
    1    -> not x
    2    -> x
    _    -> True