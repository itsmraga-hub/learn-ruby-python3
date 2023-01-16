=begin
Write your code for the 'Scrabble Score' exercise in this file. Make the tests in
`scrabble_score_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/scrabble-score` directory.
=end

class Scrabble
  def initialize(str)
    @str = str
  end

  def score
    score = 0
    @str.upcase!
    return 0 unless @str
    @str.split('').each do |char|
      if char === 'Q' || char === 'Z'
        score += 10
      elsif char === 'J' || char === 'X'
        score += 8
      elsif char === 'K'
        score += 5
      elsif char === 'F' || char === 'H' || char === 'V' || char === 'W' || char === 'Y'
        score += 4
      elsif char === 'B' || char === 'C' || char === 'M' || char === 'P'
        score += 3
      elsif char === 'D' || char === 'G'
        score += 2
      else
        score += 1
      end
    end
    score
  end
end

p Scrabble.new('A').score

# //=> 1