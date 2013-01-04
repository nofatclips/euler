-- Factorial digit sum
-- Problem 20

-- n! means n × (n - 1) × ... × 3 × 2 × 1
-- For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
-- and the sum of the digits in the number 10! is
-- 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

-- Find the sum of the digits in the number 100!

-- toDigit :: Char -> Int
-- toDigit x = read [x] :: Int

-- In short: sum (map toDigit (show (product [1..100])))

problem20 :: Int

problem20 = sum digits
    where factorial = show (product [1..n])
          n = 100
          digits = map toDigit factorial
          toDigit x = read [x] :: Int