module Main where
import qualified Data.Char as C
import qualified Data.List as L
import qualified System.Environment as E
import qualified Text.Parsec as P
import qualified Text.Parsec.String as P

parse_input :: P.Parser String
parse_input = do
  result <- P.many (P.noneOf "\n")
  P.newline
  P.eof
  return result

solve :: Int -> String -> Either String Int
solve n s = if length s < n then Left "no solution found"
  else if length (L.nub (take n s)) == n then Right n
  else do
    result <- solve n (tail s)
    return (result + 1)

solve1 :: String -> Either String Int
solve1 = solve 4

solve2 :: String -> Either String Int
solve2 = solve 14

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
