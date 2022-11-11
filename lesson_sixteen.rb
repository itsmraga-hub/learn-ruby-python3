=begin
Write your code for the 'Matrix' exercise in this file. Make the tests in
`matrix_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/matrix` directory.
=end

class Matrix
  attr_reader :str, :matrix_arr

  def initialize(str)
    @str = str.split("\n")
    @matrix_arr = []
  end

  def convert_to_arr!
    @matrix_arr = @str.map { |arr| arr.split(" ") }
    @matrix_arr
  end

  def rows
    convert_to_arr!
    @str
  end

  def columns
    new_arr = convert_to_arr!
    output = []
    for inner_arr in new_arr
      inner_output = []
      for num in inner_arr
        for inner_arr in new_arr
          if new_arr.find_index(inner_arr) == inner_arr.find_index(num)
            inner_output.append(num)
          end
        end
      end
      output.append(inner_output)
    end

    output.to_s
  end

end

# p = Matrix.new("1 4 9\n16 25 36")
# p.convert_to_arr!
# puts p.matrix_arr
p = Matrix.new("1 2 3\n4 5 6\n7 8 9\n 8 7 6")
puts p.columns
