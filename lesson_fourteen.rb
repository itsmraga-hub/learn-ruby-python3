=begin
Write your code for the 'Acronym' exercise in this file. Make the tests in
`acronym_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/acronym` directory.
=end

class Acronym
  def self.abbreviate(str)
    output = str[0]
    str_arr = str.split('')
    str_arr.each_with_index {
      |char, i|
      if char == ' ' || char == '-'
        if str[i + 1].ord >= 97 && str[i + 1].ord <= 122 && char == '-'
          output += str[i + 1].upcase
        elsif str[i + 1] == '-' || char == '-'
          output = output
        elsif char == '-' && str[i + 1] == 'o'
          output += str[i + 1].upcase
        else
          output += str[i + 1].upcase
        end
      end
    }
    output
  end
end

puts Acronym.abbreviate('Portable Network Graphics')
puts Acronym.abbreviate('Ruby on Rails')
puts Acronym.abbreviate('Something - I made up from thin air')
puts Acronym.abbreviate('Complementary metal-oxide semiconductor')