import Data.Char (isLower, isUpper, toLower)
import Data.List (group, sort, sortBy)
import Data.Ord (comparing, Down (Down))
import Prelude hiding (Word)

type Text = String
type Word = String
type Run = (Int, Word)

canonical :: Char -> Char
canonical c | isLower c = c
            | isUpper c = toLower c
            | otherwise = ' '

codeRun :: [Word] -> (Int, Word)
codeRun ws = (length ws, head ws)

showRun :: Run -> String
showRun (n, w) = concat [w, ": ", show n, "\n"]

mostCommon :: Int -> Text -> String
mostCommon n =  concatMap showRun . take n . -- :: [Run] -> String
    sortBy (comparing Data.Ord.Down) . -- :: [Run] -> [Run]
    map codeRun . -- :: [Word] -> [Run]
    group . -- :: [Word] -> [[Word]]
    sort . -- :: [Word] -> [Word]
    words . -- :: Text -> [Word]
    map canonical -- :: Text -> Text
