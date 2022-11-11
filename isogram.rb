=begin
Write your code for the 'Isogram' exercise in this file. Make the tests in
`isogram_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/isogram` directory.
=end

class Isogram
  def self.isogram?(str)
    str.downcase!
    len = 0
    for ch in str.split("")
      len = str.scan(ch).length
      if len > 1
        return "Expected false, '#{str}' is not an isogram"
      end
    end
    return "Expected true, '#{str}' is an isogram"
  end
end

p Isogram.isogram?('isogram')
p Isogram.isogram?('Alphabet')
p Isogram.isogram?('eleven')