=begin
Write your code for the 'High Scores' exercise in this file. Make the tests in
`high_scores_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/high-scores` directory.
=end

class HighScores
  def initialize(scores)
    @scores = scores
  end

  def scores
    @scores
  end

  def personal_best
    @scores.max()
  end

  def latest
    @scores.pop
  end

  def personal_top_three
    @scores.max(3)
  end

  def latest_is_personal_best?
    if @scores[-1] == @scores.max()
      true
    else
      false
    end
  end
end
