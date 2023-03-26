module Main where
import Data.Char as C
import System.Environment as E
import Text.Parsec as P
import Text.Parsec.String as P

parse_natural :: P.Parser Integer
parse_natural = do
  char_digits <- P.many1 P.digit
  let digits = map (\d -> toInteger (C.ord d - C.ord '0')) char_digits
  return (foldl (\a d -> 10 * a + d) 0 digits)

type Assignment = (Integer, Integer, Integer, Integer)

parse_assignment :: P.Parser Assignment
parse_assignment = do
  a <- parse_natural
  P.char '-'
  b <- parse_natural
  P.char ','
  c <- parse_natural
  P.char '-'
  d <- parse_natural
  P.newline
  return (a, b, c, d)

parse_input :: P.Parser [Assignment]
parse_input = do
  result <- P.many parse_assignment
  P.eof
  return result

solve1 :: [Assignment] -> Either String Int
solve1 assignments = Right (length (filter (\(a, b, c, d) ->
  a > b || c > d || (c <= a && b <= d) || (a <= c && d <= b)) assignments))

solve2 :: [Assignment] -> Either String Int
solve2 assignments = Right (length (filter (\(a, b, c, d) ->
  max a c <= min b d) assignments))

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
