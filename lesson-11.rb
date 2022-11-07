# Start simple Calculator

class SimpleCalculator
  ALLOWED_OPERATIONS = ['+', '/', '*'].freeze

  def self.calculate(first_operand, second_operand, operation)
    # raise 'Please implement the SimpleCalculator.calculate method'
    begin
      raise "Division by zero is not allowed." if second_operand == 0 and operation == '/'
      raise ArgumentError.new if second_operand.instance_of? String or first_operand.instance_of? String
      raise "UnsupportedOperation" if not ALLOWED_OPERATIONS.include?(operation)
      if operation == '*'
        "#{first_operand} #{operation} #{second_operand} = #{first_operand * second_operand}"
      elsif operation == '+'
        "#{first_operand} #{operation} #{second_operand} = #{first_operand + second_operand}"
      elsif operation == '/'
        "#{first_operand} #{operation} #{second_operand} = #{first_operand / second_operand}"
      end
    rescue => e
      e.message
    end
  end
end

puts SimpleCalculator.calculate(16, 51, "+")
# => "16 + 51 = 67"
puts SimpleCalculator.calculate(32, 6, "*")
# => "32 * 6 = 192"
puts SimpleCalculator.calculate(512, 4, "/")
# => "512 / 4 = 128"
puts SimpleCalculator.calculate(1, 2, '-')

puts SimpleCalculator.calculate(1, '2', '*')

puts SimpleCalculator.calculate(512, 0, "/")

# begin
#   if ALLOWED_OPERATIONS.include?(operation)
#     begin
#       if not second_operand.instance_of? String and not first_operand.instance_of? String
#         if operation == '*'
#           "#{first_operand} #{operation} #{second_operand} = #{first_operand * second_operand}"
#         elsif operation == '+'
#           "#{first_operand} #{operation} #{second_operand} = #{first_operand + second_operand}"
#         elsif operation == '/'
#           begin
#             if second_operand == 0 || first_operand == 0
#             raise Exception.new("Division by zero is not allowed.")
#             else
#             "#{first_operand} #{operation} #{second_operand} = #{first_operand / second_operand}"
#             end
#           rescue => e
#             e.message
#           end
#         end
#       else
#         raise Exception.new("ArgumentError")
#       end
#     rescue => e
#       e.message
#     end
#   else
#     raise "UnsupportedOperation"
#   end
# rescue => e
#   e.message
# end