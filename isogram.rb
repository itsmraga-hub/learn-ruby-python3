=begin
Write your code for the 'Isogram' exercise in this file. Make the tests in
`isogram_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/isogram` directory.
=end

class Isogram
  def self.isogram?(str)
    len = 0
    for ch in str.delete('-').downcase.split("")
      if ch != ' '
        len = str.downcase.scan(ch).length
        if len > 1
          return false
        end
      end
    end
    return true
  end
end

# p Isogram.isogram?('isogram')
p Isogram.isogram?('Alphabet')
p Isogram.isogram?('zzyzx')