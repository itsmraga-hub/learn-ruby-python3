=begin
Write your code for the 'Luhn' exercise in this file. Make the tests in
`luhn_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/luhn` directory.
=end

class Luhn
  def initialize
    
  end

  def self.valid?(str)
    mappedStr = []
    to_num(str).each_with_index do |num, i|
      if i.modulo(2) === 0
        num = num.to_i * 2
        if num.to_i > 9
          num = num.to_i - 9
        end
      end
      mappedStr.push(num)
    end
    mappedStr.reduce { |sum, num| sum + num.to_i  }
  end

  def self.to_num(str)
    newStr = str.split('').filter { |num| is_integer?(num)}
    newStr
  end

  private

  def self.is_integer?(c)
    c.to_i.to_s === c
  end
end

# p Luhn.valid?('055 444 286')
p Luhn.valid?('4539 3195 0343 6467')