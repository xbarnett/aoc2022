module Main where
import Data.Char as C
import Data.List as L
import System.Environment as E
import Text.Parsec as P
import Text.Parsec.String as P

parse_rucksack :: P.Parser String
parse_rucksack = do
  result <- P.many (P.satisfy (\c -> isAsciiLower c || isAsciiUpper c))
  P.newline
  return result

parse_input :: P.Parser [String]
parse_input = do
  result <- P.many parse_rucksack
  P.eof
  return result

item_value :: Char -> Int
item_value c = C.ord c - case isAsciiLower c of
  False -> 38
  True -> 96

sack_value :: String -> Either String Int
sack_value sack = let (n, r) = divMod (length sack) 2 in case r of
  0 -> case L.group (L.intersect (take n sack) (drop n sack)) of
    [x : _] -> Right (item_value x)
    _ -> Left "the compartments in each rucksack must \
              \share exactly one item type"
  1 -> Left "each rucksack must contain an even number of items"

solve1 :: [String] -> Either String Integer
solve1 sacks = do
  values <- mapM sack_value sacks
  return (sum (map toInteger values))

groups :: [String] -> [[String]]
groups xs = case null xs of
  True -> []
  False -> take 3 xs : groups (drop 3 xs)

group_value :: [String] -> Either String Int
group_value group = case L.group (foldr1 L.intersect group) of
  [x : _] -> Right (item_value x)
  _ -> Left "the rucksacks in each group must share exactly one item type"

solve2 :: [String] -> Either String Integer
solve2 sacks = case mod (length sacks) 3 of
  0 -> do
    values <- mapM group_value (groups sacks)
    return (sum (map toInteger values))
  _ -> Left "the number of rucksacks must be divisible by 3"

process_file :: String -> IO ()
process_file fname = do
  parsed <- P.parseFromFile parse_input fname
  case parsed of
    Left error -> putStrLn ("parse failed\n" ++ show error)
    Right input -> do
      case solve1 input of
        Left error -> putStrLn ("part 1 failed\n" ++ error)
        Right output -> putStrLn ("part 1 succeeded\n" ++ show output)
      case solve2 input of
        Left error -> putStrLn ("part 2 failed\n" ++ error)
        Right output -> putStrLn ("part 2 succeeded\n" ++ show output)

main :: IO ()
main = do
  args <- E.getArgs
  sequence_ (map process_file args)
