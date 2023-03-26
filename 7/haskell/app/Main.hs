module Main where
import qualified Control.Monad as O
import qualified Data.Char as C
import qualified Data.Map.Strict as M
import qualified Data.Set as S
import qualified System.Environment as E
import qualified Text.Parsec as P
import qualified Text.Parsec.String as P

data DirEnt = Dir String | File String Integer
  deriving Show

data Command = Outermost | Out | In String | Ls [DirEnt]
  deriving Show

data DirInfo = DirInfo {
  listed :: Bool,
  dirs :: S.Set String,
  files :: M.Map String Integer,
  size :: Integer }
  deriving Show

type State = ([String], M.Map [String] DirInfo)

parse_natural :: P.Parser Integer
parse_natural = do
  char_digits <- P.many1 P.digit
  let digits = map (\d -> toInteger (C.ord d - C.ord '0')) char_digits
  return (foldl (\a d -> 10 * a + d) 0 digits)

parse_cd :: P.Parser Command
parse_cd = do
  P.string "$ cd "
  result <- P.many (P.noneOf "\n")
  P.newline
  case result of
    ".." -> return Out
    "/" -> return Outermost
    _ -> return (In result)

parse_dirent :: P.Parser DirEnt
parse_dirent = do
  result <- P.choice [O.liftM Left (P.string "dir")
                     ,O.liftM Right parse_natural]
  P.char ' '
  name <- P.many (P.noneOf "\n")
  P.newline
  case result of
    Left _ -> return (Dir name)
    Right size -> return (File name size)

parse_ls :: P.Parser Command
parse_ls = do
  P.string "$ ls\n"
  result <- P.many parse_dirent
  return (Ls result)

parse_input :: P.Parser [Command]
parse_input = do
  result <- P.many (P.choice [P.try parse_cd, parse_ls])
  P.eof
  return result

no_info :: DirInfo
no_info = DirInfo {
  listed = False,
  dirs = S.empty,
  files = M.empty,
  size = 0 }

dirent_compatible :: DirInfo -> DirEnt -> Bool
dirent_compatible d ent = case ent of
  Dir name -> S.member name (dirs d)
  File name size -> M.lookup name (files d) == Just size

process_dirent :: State -> DirEnt -> Either String State
process_dirent (cd, m) ent = ?

process_command :: State -> Command -> Either String State
process_command (cd, m) c = let d = m M.! cd in case c of
  Outermost -> Right ([], m)
  Out -> case cd of
    [] -> Left "cannot move out of /"
    (_ : cd) -> Right (cd, m)
  In name -> if listed d then
    if S.member name (dirs d)
      then Right (name : cd, m)
      else Left "cd into nonexistent directory"
    else
      let m2 = M.insert cd (d {dirs = S.insert name (dirs d)}) m
          m3 = M.insert (name : cd) no_info m2
      in Right (name : cd, m3)
  Ls ents -> if listed d then
    if all (map (dirent_compatible d) ents)
      then Right (cd, m)
      else Left "contents of directory changed in between ls commands"
    else

get_state :: [Command] -> Either String State
get_state cs = case cs of
  [] -> Left "no commands given"
  (Outermost : cs) -> O.foldM process_command ([], M.singleton [] no_info) cs
  _ -> Left "indeterminate initial directory"

solve1 :: [Command] -> Either String State
solve1 cs = get_state cs

solve2 :: [Command] -> Either String [Command]
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
