=begin
Write your code for the 'Resistor Color Duo' exercise in this file. Make the tests in
`resistor_color_duo_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/resistor-color-duo` directory.
=end

class ResistorColorDuo
  def self.value(arr)
    output = ''
    arr.each {
      |color|
      if color == 'black'
        output += '0'
      elsif color == 'brown'
        output += '1'
      elsif color == 'red'
        output += '2'
      elsif color == 'orange'
        output += '3'
      elsif color == 'yellow'
        output += '4'
      elsif color == 'green'
        output += '5'
      elsif color == 'blue'
        output += '6'
      elsif color == 'violet'
        output += '7'
      elsif color == 'grey'
        output += '8'
      elsif color == 'white'
        output += '9'
      end
    }
    output.slice(0, 2).to_i
  end
end


puts ResistorColorDuo.resistor_color_duo(%w[black violet white])