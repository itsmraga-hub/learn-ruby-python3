=begin
Write your code for the 'Word Count' exercise in this file. Make the tests in
`word_count_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/word-count` directory.
=end

class Phrase
  def initialize(str)
    @str = str
  end

  def word_count
    hash_ans = {}
    new_arr = @str.split(" ")
    uniq_words = new_arr.uniq
    uniq_words.each do |word|
      hash_ans[word] = @str.scan(word).length
    end
    hash_ans
  end
end

# p = Phrase.new("one of each")

# p p.word_count

# phrase = Phrase.new("one,\ntwo,\nthree")
phrase = Phrase.new("car: carpet as java: javascript!!&@$%^&")

p phrase.word_count