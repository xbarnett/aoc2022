module Main where
import qualified Data.Char as C
import qualified System.Environment as E
import qualified Text.Parsec as P
import qualified Text.Parsec.String as P

parse_natural :: P.Parser Integer
parse_natural = do
  char_digits <- P.many1 P.digit
  let digits = map (\d -> toInteger (C.ord d - C.ord '0')) char_digits
  return (foldl (\a d -> 10 * a + d) 0 digits)

parse_input :: P.Parser Integer
parse_input = parse_natural

solve1 :: Integer -> Either String Integer
solve1 input = Right input

solve2 :: Integer -> Either String Integer
solve2 input = Right input

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
