module Main where
import Data.Char as C
import System.Environment as E
import Text.Parsec as P
import Text.Parsec.String as P

parse_round :: P.Parser (Char, Char)
parse_round = do
  a <- P.oneOf "ABC"
  P.char ' '
  b <- P.oneOf "XYZ"
  P.newline
  return (a, b)

parse_input :: P.Parser [(Char, Char)]
parse_input = P.many parse_round

solve_round :: (Char, Char) -> (Integer, Integer)
solve_round (a, b) = case a : b : [] of
  "AX" -> (4, 3)
  "AY" -> (8, 4)
  "AZ" -> (3, 8)
  "BX" -> (1, 1)
  "BY" -> (5, 5)
  "BZ" -> (9, 9)
  "CX" -> (7, 2)
  "CY" -> (2, 6)
  "CZ" -> (6, 7)

solve1 :: [(Char, Char)] -> Either String Integer
solve1 = Right . sum . map (fst . solve_round)

solve2 :: [(Char, Char)] -> Either String Integer
solve2 = Right . sum . map (snd . solve_round)

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
