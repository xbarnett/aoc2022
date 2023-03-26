module Main where
import qualified Control.Monad as O
import qualified Data.Char as C
import qualified Data.List as L
import qualified Data.Map as M
import qualified Data.Maybe as Y
import qualified System.Environment as E
import qualified Text.Parsec as P
import qualified Text.Parsec.String as P

type Crates = M.Map Int String
type Move = (Integer, Int, Int)
type Input = (Crates, [Move])

parse_crate :: P.Parser (Maybe Char)
parse_crate = do
  air <- P.optionMaybe (P.try (P.string "   "))
  case air of
    Nothing -> do
      P.char '['
      result <- P.anyChar
      P.char ']'
      return (Just result)
    Just _ -> return Nothing

parse_line_of :: P.Parser a -> P.Parser [a]
parse_line_of p = do
  result <- P.sepBy1 p (P.char ' ')
  P.newline
  return result

parse_natural :: P.Parser Integer
parse_natural = do
  char_digits <- P.many1 P.digit
  let digits = map (\d -> toInteger (C.ord d - C.ord '0')) char_digits
  return (foldl (\a d -> 10 * a + d) 0 digits)

parse_space_natural :: P.Parser Integer
parse_space_natural = do
  P.char ' '
  result <- parse_natural
  P.char ' '
  return result

parse_crates :: P.Parser ([[Maybe Char]], [Integer])
parse_crates = do
  nums <- P.optionMaybe (P.try (parse_line_of parse_space_natural))
  case nums of
    Nothing -> do
      crates <- parse_line_of parse_crate
      (lines, labels) <- parse_crates
      return (crates : lines, labels)
    Just labels -> return ([], labels)

parse_move :: Int -> P.Parser Move
parse_move stacks = do
  P.string "move "
  a <- parse_natural
  P.string " from "
  b <- parse_natural
  P.string " to "
  c <- parse_natural
  P.newline
  if 1 <= b && b <= toInteger stacks && 1 <= c && c <= toInteger stacks then
    return (a, fromInteger b, fromInteger c)
  else fail "invalid stack number in move"

parse_input :: P.Parser Input
parse_input = do
  (crates, labels) <- parse_crates
  let n = length labels
  if all (\cs -> length cs == n) crates then
    if labels == [1 .. toInteger n] then do
      let crates' = map (dropWhile Y.isNothing) (L.transpose crates)
      if all (all Y.isJust) crates' then do
        P.newline
        moves <- P.many (parse_move n)
        P.eof
        return (M.fromList (zip [1 ..] (map (map Y.fromJust) crates')), moves)
      else fail "floating crate"
    else fail "invalid stack label"
  else fail "invalid number of crates in row"

move :: Bool -> Crates -> Move -> Either String Crates
move rev crates (n, from, to) =
  if toInteger (length (crates M.! from)) >= n then do
    let (top, bottom) = splitAt (fromInteger n) (crates M.! from)
    let top' = if rev then reverse top else top
    if from == to then
      return crates
    else return (M.insertWith (++) to top' (M.insert from bottom crates))
  else Left "not enough crates to execute move instruction"

solve :: Bool -> Input -> Either String String
solve rev (crates, moves) = do
  result <- O.foldM (move rev) crates moves
  let result' = map snd (M.toAscList result)
  if any null result' then
    Left "all of the final stacks must be nonempty"
  else Right (map head result')

solve1 :: Input -> Either String String
solve1 = solve True

solve2 :: Input -> Either String String
solve2 = solve False

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
