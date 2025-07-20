import System.IO
import Data.List (sort, foldl')

main :: IO ()
main = do
    putStr "Dateiname: "
    hFlush stdout
    filename <- getLine
    content <- readFile filename
    let (figures, shelf) = parseInput content
        sortedShelf = sort shelf
        finalFigures = countFigures sortedShelf figures
    putStrLn $ if finalFigures < 0 then "Geht nicht" else "Geht"

parseInput :: String -> (Int, [Int])
parseInput input =
    let (figs:books:rest) = lines input
        figures = read figs
        bookCount = read books
        shelf = map read (take bookCount rest)
    in (figures, shelf)

countFigures :: [Int] -> Int -> Int
countFigures [] figs = figs
countFigures (x:xs) figs = snd $ foldl' step (x, figs) xs
  where
    step (curmin, f) book
        | book - curmin > 30 = (book, f - 1)
        | otherwise          = (curmin, f)